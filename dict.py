m={'a':1,'c':2,'b':3}
k=list(m.keys())
print(k)
k.sort()
print(k)
for key in k:
    print(key ,'=>',m[key])
