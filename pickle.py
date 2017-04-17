import pickle
a = ['a','b','c','d']
b = open('a.dat','wb')
pickle.dump(a,b)
b.close()

