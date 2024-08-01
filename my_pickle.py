import pickle
f=open('data.pkl','wb')
d={'a':1,'b':2,'c':3}
pickle.dump(d,f)
f.close()
f=open('data.pkl','rb')
print(pickle.load(f))
