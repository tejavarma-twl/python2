import json

def readfile(fp):
    with open(fp) as bank:
        read_data = json.load(bank)
        return read_data