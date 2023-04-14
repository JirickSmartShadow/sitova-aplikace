from logging import *


class TranslatePing:
    def run(self, connection, client_inet_address, dictionary, word, config):
        connection.send(bytes('TRANSLATEPONG"{}"'.format(config['program_name']), 'utf-8'))
        log(client_inet_address, 'TRANSLATEPONG"{}"'.format(config['program_name']), True)
