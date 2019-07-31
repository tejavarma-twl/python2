import json
import pickle
from filedb.writing import *
from filedb.reading import *

bankaccounts = {
    '1234':{ 'name':'Teja', 'phone':99999, 'balance':9999999 },
    '1235':{ 'name':'Varma', 'phone':88888, 'balance':876876 },
    '1236':{ 'name':'Raju', 'phone':77777, 'balance':786868 },
    '1237':{ 'name':'Ravi', 'phone':66666, 'balance':2342342 }
}

# with open('bankaccounts.json','w') as bank:
#     json.dump(bankaccounts, bank)
writefile(bankaccounts,'filedb/bankaccounts.json')
writefile(bankaccounts,'filedb/bankaccounts2.json')
writefile(bankaccounts,'filedb/bankaccounts3.json')
data = readfile('filedb/bankaccounts.json')
data2 = readfile('filedb/bankaccounts2.json')
data3 = readfile('filedb/bankaccounts3.json')
print(data)
print(data2)
print(data3)

# with open('bankaccounts','wb') as bank:
#     pickle.dump(bankaccounts,bank)

# with open('bankaccounts','rb') as bank:
#     val = pickle.load(mydata)
#     print(val)
