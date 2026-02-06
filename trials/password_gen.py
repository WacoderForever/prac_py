import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
numbers=['0','1','2','3','4','5','6','7','8','9']
let_no=input("How many letters would you like your password to have:")
let_no=(int)(let_no)
sy_no=input("How many symbols would you like your password to have:")
sy_no=(int)(sy_no)
num_no=input("How many numbers would you like your password to have:")
num_no=(int)(num_no)
i=0
pos=random.randint(1,4)
pas=""
if(pos==1):
    pas=pas+random.choice(letters)
    i+=1
elif(pos==2):
    pas=pas+random.choice(symbols)
    i+=1
else:
    pas=pas+random.choice(numbers)
    i+=1
while (i<(let_no+sy_no+num_no)):
    pos=random.randint(1,4)
    if(pos==1):
        pas=pas+random.choice(letters)
        i+=1
    elif(pos==2):
        pas=pas+random.choice(symbols)
        i+=1
    else:
        pas=pas+random.choice(numbers)
        i+=1
print(f"Your password is:{pas}")