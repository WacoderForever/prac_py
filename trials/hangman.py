import random
stages=['''
        +++++
        0    |
        /\   |
        |    |
        /\   |

        #####
       ''' ,
       '''
        +++++
        0    |
        /\   |
        |    |
        /\   |
        #####
       ''' ,
       '''
           +++
        0    |
        /\   |
        |    |
        /\   |
        #####
       ''' ,
       '''
           
        0    |
        /\   |
        |    |
        /\   |
        #####
       ''' ,
       '''
           
        0    
        /\   
        |    |
        /\   |
        #####
       ''' ,
         '''
           
        0    
        /\   
        |    
        /\   
        #####
       '''
       ]
lives=5
words=['argam','caleidoscope','ganji']
k=random.choice(words)
num=len(k)
out=["_"]*num
string1=''.join(str(e) for e in out)
string2=""
print(f"Chosen word:{k}")
while ((lives >=0) and (string2 !=k)):
    c=input("Guess the letter:")
    i=0
    while (i<num):
        if(c==k[i]):
            out[i]=c
            i+=1
        else:
            i+=1
    string2=''.join(str(e) for e in out)
    if(string1 != string2):
        print(string2)
        print(stages[lives])
    else:
        lives-=1
        print(string2)
        print(stages[lives])
        
        
    string1=string2
if(lives>0):
    print("You win congrats")
else:
    print("You lost")