Learn more or give us feedback
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense

class VGGNetSmall():
    def __init__(self, input_shape, num_classes, final_activation):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.final_activation = final_activation
    def build(self):
        model = Sequential()
        model.add(Conv2D(filters=32, kernel_size = (3, 3), input_shape = self.input_shape, activation='relu'))







        return model