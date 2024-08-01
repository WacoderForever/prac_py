import random
import time

rock=1
paper=2
scissors=3
names={rock:"Rock",paper:"Paper",scissors:"Scissors"}
rules={rock:scissors,scissors:paper,paper:rock}
player_score=0
comp_score=0
def start():
    print("Lets play a game of Rock,Paper,Scissors")
    while game():
        pass
    scores()
def game():
    player=move()
    comp=random.randint(1,3)
    result(player,comp)
    return play_again()
def move():
    while True:
        player=input("Enter 1 for Rock,2 for Paper,3 for Scissors: ")
        try:
            player=int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Ooops! I did not understand your selection.")
def result(player,comp):
    print("1....")
    time.sleep(1)
    print("2....")
    time.sleep(1)
    print("3....")
    time.sleep(0.5)
    print("The computer chose {}".format(names[comp]))
    global player_score,comp_score
    if player==comp:
        print("It is a tie")
    else:
        if rules[player]==comp:
            print("You are the winner")
            player_score+=1
        else:
            print("The computer laughs at your defeat.")
            comp_score+=1
def play_again():
    answer=input("Would you like to play the game again? (y/n): ")
    if answer in ('y','Y'):
        return answer
        try:
            answer='y'|'Y'|'n'|'N'
        except ValueError:
            print("Invalid choice")
    else:
        print("Thank you. We hope you enjoyed the game.")   
def scores():
    global player_score,comp_score
    print("HIGH SCORES:")
    print("Player: {} points".format(player_score))
    print("Computer: {} points".format(comp_score))
    
if __name__=="__main__":
    start()
    