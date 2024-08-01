k=['cap','CAT','jake','abc','ABC','KHALIGRAPH']
k.sort()
print(k)
k.sort(key=str.lower)
print(k)
k.sort(key=str.lower,reverse=True)
print(k)