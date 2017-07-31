import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import config

class MyOwnCNN:

    @staticmethod
    def init_model():
        LR = 1e-3
        MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR, '2conv-basic')

        convnet = input_data(shape=[None, 50, 50, 1], name='input')
        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 128, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 256, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 128, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)
        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)
        convnet = fully_connected(convnet, 2, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy',
                             name='targets')
        config.model = tflearn.DNN(convnet, tensorboard_dir='log')

        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            config.model.load(MODEL_NAME)

    @staticmethod
    def who_is_it(str_pic):
        file_data = []
        path = os.path.join("./", str_pic)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (50, 50))
        file_data.append([np.array(img), 0])
        for num, data in enumerate(file_data):
            img_data = data[0]
            data = img_data.reshape(50, 50, 1)
            model_out = config.model.predict([data])[0]
            if np.argmax(model_out) == 1:
                str_label = 'Dog'
            else:
                str_label = 'Cat'
        return str_label