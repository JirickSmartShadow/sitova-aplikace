import re
import time
from commands.translateping import *
from commands.translatelocl import *
from commands.translatescan import *
from logging import *
from configuration import *
from threading import Thread


def client_handle(connection, client_inet_address, commands, dictionary, config):
    try:
        # client handling
        connection_input = connection.recv(50).decode("utf-8").strip()
        # print(connection_input)

        # check input
        result = re.match('([A-Z]{13})"(.+)"', connection_input)

        if result and result.group(1) in commands.keys():
            commands[result.group(1)].run(connection, client_inet_address, dictionary, result.group(2), config)
        else:
            connection.send(bytes('unknown command', 'utf-8'))
            log(client_inet_address, 'unknown command', False)
    finally:
        # aby se stihla odelat message
        time.sleep(0.001)
        connection.close()


if __name__ == '__main__':
    config = load_configuration()

    # init server
    server_inet_address = (config["ip_address"], config["port"])
    server_socket = socket.socket()
    server_socket.bind(server_inet_address)
    server_socket.listen()
    is_running = True

    # init command palette
    commands = dict()
    commands['TRANSLATEPING'] = TranslatePing()
    commands['TRANSLATELOCL'] = TranslateLocl()
    commands['TRANSLATESCAN'] = TranslateScan()

    # init dictionary
    dictionary = {
        'dog': 'pes',
        'mug': 'hrnek',
        'sugar': 'cukr',
        'darkness': 'temnota',
        'sun': 'slunce'
    }

    # listening loop
    try:
        while is_running:
            # accept client
            connection, client_inet_address = server_socket.accept()

            # call client loop
            thread = Thread(target=client_handle,
                            args=(connection, client_inet_address, commands, dictionary, config))
            thread.start()
    finally:
        server_socket.close()
