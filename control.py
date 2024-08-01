import sys
total=input("How many integers: ")

try:
    total=int(total)
except ValueError:
    sys.exit("You should enter an integer")
values=[]
count=0
while count<total:
    new=input("Enter integer{}: ".format(count+1))
    try:
        new=int(new)
        values.append(new)
        count+=1
    except ValueError:
        print("You should enter only an integral value: ")
i=0   
while i<count:
    print(values[i])
    i+=1



