import configparser

from Services.MyOwnCNN import MyOwnCNN

config = configparser.ConfigParser()
config.read('config.ini')


myConvolutionalNeuralNetwork = MyOwnCNN()
tg_token = config['DEFAULT']['tgToken']
