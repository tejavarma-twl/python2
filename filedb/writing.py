import json

def writefile(data,fp):
    with open(fp,'w') as bank:
        json.dump(data,bank)