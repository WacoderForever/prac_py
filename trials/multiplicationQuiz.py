import pyinputplus as pyip
import random,time

numberOfQuestions=10
correctanswers=0

for i in range(numberOfQuestions):
    num1=random.randint(0,20)
    num2=random.randint(0,20)
    prompt='#%s: %s x %s ='%(i,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (num1*num2)],blockRegexes=[('.*','Incorrect')],timeout=8,limit=3)

    except pyip.TimeoutException:
        print("Out of Time")
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct')
        correctanswers+=1
    time.sleep(1)    

print(f"\nScore: {correctanswers}/{numberOfQuestions}")