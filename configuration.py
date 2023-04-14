import json


def load_configuration():
    file = open("config/config.json")
    data = json.load(file)
    ip_address = data["ip_address"]
    port = data["port"]
    ip_address_start = data["ip_address_start"]
    ip_address_end = data["ip_address_end"]
    port_start = data["port_start"]
    port_end = data["port_end"]
    program_name = data["program_name"]
    return {
        "ip_address": ip_address,
        "port": port,
        "ip_address_start": ip_address_start,
        "ip_address_end": ip_address_end,
        "port_start": port_start,
        "port_end": port_end,
        "program_name": program_name
    }
