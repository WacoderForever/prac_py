import struct

packed=struct.pack('>i4sh',7,b'spam',8)
f=open('tr.dat','wb')
f.write(packed)
f.close()
f=open('tr.dat','rb')
k=f.read()
f.close()
print(k)