from logging import *


class TranslateLocl:
    def run(self, connection, client_inet_address, dictionary, word, config):
        if word in dictionary.keys():
            translation = dictionary[word]
            connection.send(bytes('TRANSLATEDSUC"{translation}"'.format(translation=translation), 'utf-8'))
            log(client_inet_address, 'TRANSLATEDSUC"{translation}"'.format(translation=translation), True)
        else:
            connection.send(bytes('TRANSLATEDERR"unknown word"', 'utf-8'))
            log(client_inet_address, 'TRANSLATEDERR"unknown word"', False)
