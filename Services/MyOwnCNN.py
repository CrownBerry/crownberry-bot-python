import os  # dealing with directories

import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


class MyOwnCNN:
    LR = 1e-3
    MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR, '2conv-basic')

    def __init__(self):
        self.model = None
        convolutional_network = input_data(shape=[None, 50, 50, 1], name='input')
        convolutional_network = conv_2d(convolutional_network, 32, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 64, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 128, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 256, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 128, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 64, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = conv_2d(convolutional_network, 32, 5, activation='relu')
        convolutional_network = max_pool_2d(convolutional_network, 5)
        convolutional_network = fully_connected(convolutional_network, 1024, activation='relu')
        convolutional_network = dropout(convolutional_network, 0.8)
        convolutional_network = fully_connected(convolutional_network, 2, activation='softmax')
        convolutional_network = regression(convolutional_network, optimizer='adam',
                                           learning_rate=self.LR, loss='categorical_crossentropy', name='targets')
        self.model = tflearn.DNN(convolutional_network, tensorboard_dir='log')

        if os.path.exists('{}.meta'.format(self.MODEL_NAME)):
            self.model.load(self.MODEL_NAME)

    def recongnize(self, str_pic) -> str:
        str_label = ""
        file_data = []
        path = os.path.join("./", str_pic)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (50, 50))
        file_data.append([np.array(img), 0])
        for num, data in enumerate(file_data):
            img_data = data[0]
            data = img_data.reshape(50, 50, 1)
            model_out = self.model.predict([data])[0]
            if np.argmax(model_out) == 1:
                str_label = 'Dog'
            else:
                str_label = 'Cat'
        return str_label
