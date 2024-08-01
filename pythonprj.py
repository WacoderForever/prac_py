def check_age(age):
    if age >=18:
        print("legal age")
    else:
        print("you are under age")
        age=int(input("Enter your age:"))
        check_age(age)

check_age(12)