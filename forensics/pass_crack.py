import crypt
password='egg'
encry_pass=crypt.crypt(password,'DF')
print(f'{encry_pass}')