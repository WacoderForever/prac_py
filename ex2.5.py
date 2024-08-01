x=input("Enter integer:")
x_str=str(x)
count=len(x_str)
z=list(range(count))
ans=0
for k in z:
    ans+=(int)(x_str[k])
print("Sum of digits is:%d"%(ans))