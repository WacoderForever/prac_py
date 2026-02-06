def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False 
    if (text[3] != '-') or (text[7] != '-'):
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False 
    for i in range(8,12):
        if not text[i].isdecimal():
            return False 
    return True

def main():
    print('Is Moshi moshi a phone number')
    print(isPhoneNumber('Moshi Moshi'))

if __name__=='__main__':
    main()