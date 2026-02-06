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
def append_zero(digit):
    digit=int(digit)
    if(digit<10):
        res='0'+str(digit)
    else:
        res=digit
    return res

def main():
    day1 =input("Enter day: ")
    month1 = input("Enter month: ")
    year = input("Enter year: ")
    day=append_zero(day1)
    month=append_zero(month1)
    date = f"{day}/{month}/{year}"
    result = date_regex(date)
    if result:
        print(f"{date} is valid")
    else:
        print(f"{date} is not valid")

if __name__ == '__main__':
    main()
