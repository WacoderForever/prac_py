import re

def leap_year(year):
    if (year % 4 == 0):
        if (year % 100 != 0):
            return True
        else:
            if (year % 400 == 0):
                return True
            else:
                return False
    else:
        return False

def date_regex(date):
    dateRegex = re.compile(r'^[0-3][0-9]/[0-1][0-2]/[1-2][0-9]{3}$')
    mo = dateRegex.search(date)
    if mo:
        return mo.group()
    else:
        return None

def main():
    day = input("Enter day: ")
    month = input("Enter month: ")
    year = input("Enter year: ")
    date = f"{day}/{month}/{year}"
    result = date_regex(date)
    if result:
        print(f"{date} is valid")
    else:
        print(f"{date} is not valid")

if __name__ == '__main__':
    main()
