import random
people=input("Enter your names(separating them using commas):")
people=people.split(",")
size=len(people)-1
payer=people[(random.randint(0,size))]
print(payer)