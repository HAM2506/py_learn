import pickle

shoplistfile = 'shoplist.txt'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')

pickle.dump(shoplist, f)

f.close()

del shoplist

f = open(shoplistfile, 'rb')

storedlist = pickle.load(f)

print(storedlist)