
def SUM(array):
    k=0
    for i in range(0,len(array)):
        k+=array[i]
    
    return k



JACK=10
QUEEN=JACK
KING=JACK
ACE=11
Done = False
playerinput=input("how much do you wanna bet")
import random
# import time
currentHand=[]
currentDealerHand=[]
why=[]
brainrot=[]
CARDS=[1,2,3,4,5,6,7,8,9,10,10,10,10]

currentHand=[random.choice(CARDS),random.choice(CARDS)]
currentDealerHand=[random.choice(CARDS),random.choice(CARDS)]






print(currentHand)
print(currentDealerHand)


while Done == False:
    print(SUM(currentHand))
    print(SUM(currentDealerHand))
 
    time=3
   

    if SUM(currentHand)==21 or SUM(currentDealerHand)==21:
        print("you won the bet amount", playerinput)
        break

    elif SUM(currentHand)<21 and  SUM(currentDealerHand)<21 :

        playerchoice=input("do you want to hit or stand")


        if playerchoice=="hit":
            currentHand.append(random.choice(CARDS))

        if playerchoice=="stand":
            break
            
    elif SUM(currentHand)>21:
        print("you lost")
        break

while SUM(currentDealerHand)<17:
 if SUM(currentHand)<21 and SUM(currentDealerHand)>SUM(currentHand):
    print("dealer wins")

    if SUM(currentHand)<21 and SUM(currentDealerHand)<SUM(currentHand):
         currentHand.append(random.choice(CARDS))