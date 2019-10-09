IF OBJECT_ID('proc_predict', 'P') IS NOT NULL
DROP PROCEDURE proc_predict
GO
CREATE PROCEDURE proc_predict
AS
BEGIN
  -- ２．DBに格納したモデルの取り出し
  DECLARE @trained_model varbinary(max) = (select model from models);
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

# ３．データセットから属性（答えを導くための説明となる各種列値）を抽出
np_test = df_test.values
x_test = np_test[:, 2:]

# ４．モデルを利用するための復元
model = pickle.loads(trained_model)

# ５．モデルに属性をセットし性別値を予測
y_pred_np = model.predict(x_test)
y_pred_cls = numpy.argmax(y_pred_np, 1)

# ６．返却値に対して予測結果をセット
df_label = df_test.iloc[:, 0:1]
df_label["y_pred"] = y_pred_cls

',
  -- １．性別値を削除してしまったデータセットをDBから抽出
  @input_data_1 = N'SELECT * FROM HumanCharacteristics WHERE ["X0被験者情報_性別"] IS NULL',
  @input_data_1_name = N'df_test',
  @output_data_1_name = N'df_label', 
  @params = N'@trained_model varbinary(max)',
  @trained_model = @trained_model
    WITH RESULT SETS ((
    ID int not null,
    予測値 int not null));
  ;
END;
GO
