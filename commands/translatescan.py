from logging import *
import ipaddress
import socket


class TranslateScan:
    def run(self, connection, client_inet_address, dictionary, word, config):
        # pokud slovo je v mem slovniku, vratit preklad
        if word in dictionary.keys():
            translation = dictionary[word]
            connection.send(bytes('TRANSLATEDSUC"{translation}"'.format(translation=translation), 'utf-8'))
            log(client_inet_address, 'TRANSLATEDSUC"{translation}"'.format(translation=translation), True)
            return

        ip_start = ipaddress.IPv4Address(config['ip_address_start'])
        ip_end = ipaddress.IPv4Address(config['ip_address_end'])
        ip_temp = ip_start

        port_start = config['port_start']
        port_end = config['port_end']
        port_temp = port_start

        # projet ip adresy
        while ip_temp <= ip_end:
            # pripojit se na adresu a port
            while port_temp <= port_end:
                try:
                    s = socket.socket()
                    s.settimeout(0.1)
                    s.connect((str(ip_temp), port_temp))
                    s.send(bytes('TRANSLATELOCL"{}"'.format(word), 'utf-8'))
                    response = s.recv(50).decode('utf-8').strip()
                    if response[:13] == 'TRANSLATEDSUC':
                        connection.send(bytes(response, 'utf-8'))
                        log(client_inet_address, response, True)
                        return
                except:
                    pass
                port_temp += 1
            ip_temp += 1
            port_temp = port_start
        connection.send(bytes('TRANSLATEDERR"unknown word"', 'utf-8'))
