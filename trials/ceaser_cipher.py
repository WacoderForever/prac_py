def encode(letters,shift):
    result=""
    let=input("Enter text to encode:")
    i=0
    while(i<len(let)):
        j=0
        while(j<=26):
            if(let[i]==letters[j]):
                if((j+shift)>25):
                    q=25-j
                    result=result+letters[shift-q-1]
                    j=27
                else:
                    result=result+letters[j+shift]
                    j=27
            else:
                j+=1
        i+=1
    return result
def decode(letters,shift):
    result=""
    let=input("Enter text to decode:")
    i=0
    while(i<len(let)):
        j=0
        while(j<26):
            if(let[i]==letters[j]):
                if((j-shift)<0):
                    q=shift-j
                    result=result+letters[26-q]
                    j=27
                else:
                    result=result+letters[j-shift]
                    j=27
            else:
                j+=1
        i+=1
    return result

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choice='yes'
while(choice=='yes'):
    func=input("Type encode or decode:").lower()
    shift=int(input("Enter number to shift:"))
    if(func=='encode'):
        k=encode(letters,shift)
        print(f"The encoded value is {k}")
        choice=input("Enter 'yes' to continue or 'no' to stop.").lower()
    if(func=='decode'):
        d=decode(letters,shift)
        print(f"The decoded value is {d}")
        choice=input("Enter 'yes' to continue or 'no' to stop.").lower()
