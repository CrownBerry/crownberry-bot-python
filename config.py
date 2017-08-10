import configparser

from Services.MyOwnCNN import MyOwnCNN
from Services.Topwords import Topwords

config = configparser.ConfigParser()
config.read('config.ini')

myConvolutionalNeuralNetwork = MyOwnCNN()
tg_token = config['DEFAULT']['tgToken']
topwords = Topwords()
