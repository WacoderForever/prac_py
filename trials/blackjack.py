import random

cards=[1,2,3,4,5,6,7,8,9,10,10,10]
comp_score=0
your_score=0

your_1=random.choice(cards)
pl_score=[your_1]
c_score=[]
choice=input("Do you want to deal,'yes' or 'no':").lower()
while(choice=='yes'):
    your_2=[random.choice(cards)]
    pl_score=pl_score+your_2
    comp_1=[random.choice(cards)]
    c_score=c_score+comp_1
    print(f"You were dealt {pl_score}")
    print(f"The computer was dealt {c_score}")
    for i in pl_score:
        your_score=your_score+i
    for i in c_score:
        comp_score=comp_score+i
    if(your_score==21):
        print("You win")
        choice=input("Do you want to deal,'yes' or 'no':").lower()
        if(choice=='yes'):
            comp_score=0
            your_score=0
            pl_score=[]
            pl_score=[random.choice(cards)]
            c_score=[]
    elif(your_score>21):
        print("You lose")
        choice=input("Do you want to deal,'yes' or 'no':").lower()
        if(choice=='yes'):
            comp_score=0
            your_score=0
            pl_score=[]
            pl_score=[random.choice(cards)]
            c_score=[]
           
    else:
        if((21-your_score)<(21-comp_score)):
            choice=input("Do you want to deal,'yes' or 'no':").lower()
            if(choice=='no'):
                print("You win")
                comp_score=0
                your_score=0
                pl_score=[]
                pl_score=[random.choice(cards)]
                c_score=[]
            

        else: 
            choice=input("Do you want to deal,'yes' or 'no':").lower()
            if(choice=='no'):
                print("You lose")
                comp_score=0
                your_score=0
                pl_score=[]
                pl_score=[random.choice(cards)]
                c_score=[]  
            
