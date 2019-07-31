# f = open('hello.txt','r')

# a = f.readline()
# b = f.readline()
# print(a)
# print(b)
# f.close()

# with open('hello.txt') as f:
#      read_data = f.read()
#      print(read_data)

# import json

# data = json.dumps([1, 'simple', 'list'])
# data = json.dumps({'s':'a','s1':'a','s2':{'a','b'}}})
# data = json.dumps(list({'s','s1','s2'}))

# data2 = json.load(data)

# print(data2)

# {'a':'ok','b':11}

# {"a":"ok","b":11}
# read_data = {}
# with open('hello.json') as f:
#     read_data = json.load(f)
    
# print(read_data)
# read_data['newk'] = 9878
# updateddata = read_data
# with open('hello.json','w') as f:
#     json.dump(updateddata, f)

import pickle

with open('hello.pkl','wb') as mydata:
    pickle.dump("hello",mydata)

with open('hello.pkl','rb') as mydata:
    val = pickle.load(mydata)
    print(val)

plaindata = "hello this is a sample information for pickle"
encoded = pickle.dumps(plaindata)
print(encoded)
decoded = pickle.loads(encoded)
print(decoded)