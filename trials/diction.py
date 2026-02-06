d={'goal':1,'scorer':'Haaland','assist':'DeBryune'}
print(d)
d['keeper']=['DeGea','Joe']
print(d)
d1={'toast':'cake'}
d.update(d1)
print(d)
print(d.get('toast'))
print([key for(key,value) in d.items() if value=='Haaland'])