import re

def main():
    phoneRegex=re.compile(r'\d{3}-\d{3}-\d{4}')
    mo=phoneRegex.search('My number is 444-567-3267')
    print('The number is '+ mo.group())  
    batregex=re.compile(r'Bat(wo)?man')
    mo1=batregex.search("Have yo seen Batman")
    print("I have seen "+mo1.group()) 
    mo2=batregex.search("Have yo seen Batwoman")
    print("I have seen "+mo2.group()) 
if __name__=='__main__':
    main()