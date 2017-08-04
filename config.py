import configparser

from Services.DTO import DTO


def init():
    config = configparser.ConfigParser()
    config.read('config.ini')
    global model
    global tg_token
    tg_token = config['DEFAULT']['tgToken']
    global list_of_word
    list_of_word = {}
