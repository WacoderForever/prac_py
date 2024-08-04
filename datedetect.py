import re

def leap_year(year):
    if (year%4==0):
        if(year%100!=0):
            return True
        else:
            if(year%400==0):
                return True
            else:
                return False
    else:
        return False

def date_regex(date):
    dateRegex=re.compile(r'^[0-3][0-9]\/[0-1][0-2]\/[1-2][0-9][0-9][0-9]$')
    mo=re.findall(string)(date)
    k=mo.group()
    return k

def main():
    day=input("Enter day:")
    month=input("Enter month:")
    year=input("Enter year:")
    date=day+'/'+month+'/'+year
    result=date_regex(date)
    if result is not NULL:
        print(date+" is valid")
    else:
        print(date+" is not valid")
if __name__=='__main__':
    main()