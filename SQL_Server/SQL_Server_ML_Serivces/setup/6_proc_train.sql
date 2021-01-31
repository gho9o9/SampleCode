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

# �Q�D�f�[�^�Z�b�g�����x���i�������������ƂȂ鐫�ʁj�Ƒ����i�����𓱂����߂̐����ƂȂ�e���l�j�ɕ���
np_train = df_train.values
y_train = np_train[:, 1]	# ���x��
x_train = np_train[:, 2:]	# ����
y_1hot = keras.utils.to_categorical(y_train, num_classes=2)

# �R�D���f���̏�����
model = Sequential([Dense(200, input_dim=89, activation="relu"), Dropout(0.5), Dense(2, activation="softmax")])
model.compile(loss="categorical_crossentropy", optimizer=optimizers.SGD(lr=0.1))

# �S�D���f���̐���
model.fit(x_train, y_1hot, epochs=20, batch_size=2, verbose=2)

# �T�D���f����DB�֊i�[���邽�߂̒���
trained_model = pickle.dumps(model)
',
  -- �P�D�w�K�p�̃f�[�^�Z�b�g��DB���璊�o
  @input_data_1 = N'SELECT * FROM HumanCharacteristics WHERE ["X0�팱�ҏ��_����"] IS NOT NULL',
  @input_data_1_name = N'df_train',
  @params = N'@trained_model varbinary(max) OUTPUT',
  @trained_model = @out_trained_model OUTPUT;
  ;

END;
GO
