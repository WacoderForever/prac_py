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
    mo=re.findall(date)
    return mo.group()

def main():
    
if __name__=='__main__':
    main()