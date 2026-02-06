import pyinputplus as pyip

response=pyip.inputMenu(["Cofee","Tea","Juice"],prompt="What would you like?: \n")
print(f"You selected: {response}")