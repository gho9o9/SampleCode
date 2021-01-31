IF OBJECT_ID('proc_train', 'P') IS NOT NULL
DROP PROCEDURE proc_train
GO
CREATE PROCEDURE proc_train (@out_trained_model varbinary(max) OUTPUT)
AS
BEGIN
  EXEC sp_execute_external_script
  @language = N'Python',
  @script = N'
def make_keras_picklable(keras, tempfile):

    def __getstate__(self):
        print("getstate is called")
        model_str = ""
        with tempfile.NamedTemporaryFile(mode="wb+", suffix=".hdf5", delete=False) as fd:
            keras.models.save_model(self, fd.name, overwrite=True)
            model_str = fd.read()
        d = { "model_str": model_str }
        return d

    def __setstate__(self, state):
        print("setstate is called")
        with tempfile.NamedTemporaryFile(mode="wb+", suffix=".hdf5", delete=False) as fd:
            fd.write(state["model_str"])
            fd.flush()
            model = keras.models.load_model(fd.name)
        self.__dict__ = model.__dict__


    cls = keras.models.Model
    cls.__getstate__ = __getstate__
    cls.__setstate__ = __setstate__

import pickle
import numpy
# import pandas
import keras
import tempfile
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.models import Sequential
from keras import optimizers
from keras import backend as K


make_keras_picklable(keras, tempfile)

# ２．データセットをラベル（導きたい答えとなる性別）と属性（答えを導くための説明となる各種列値）に分割
np_train = df_train.values
y_train = np_train[:, 1]	# ラベル
x_train = np_train[:, 2:]	# 属性
y_1hot = keras.utils.to_categorical(y_train, num_classes=2)

# ３．モデルの初期化
model = Sequential([Dense(200, input_dim=89, activation="relu"), Dropout(0.5), Dense(2, activation="softmax")])
model.compile(loss="categorical_crossentropy", optimizer=optimizers.SGD(lr=0.1))

# ４．モデルの生成
model.fit(x_train, y_1hot, epochs=20, batch_size=2, verbose=2)

# ５．モデルをDBへ格納するための直列化
trained_model = pickle.dumps(model)
',
  -- １．学習用のデータセットをDBから抽出
  @input_data_1 = N'SELECT * FROM HumanCharacteristics WHERE ["X0被験者情報_性別"] IS NOT NULL',
  @input_data_1_name = N'df_train',
  @params = N'@trained_model varbinary(max) OUTPUT',
  @trained_model = @out_trained_model OUTPUT;
  ;

END;
GO
