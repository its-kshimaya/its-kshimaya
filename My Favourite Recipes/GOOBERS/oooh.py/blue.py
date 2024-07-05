print("This is a rock paper scissors game ")
import random
rock="kills scissors but loses by paper"
paper="covers rock but gets cut by scissors"
scissors="cuts paper gets killed by rock"
computer=["rock","paper","scissors"]
rand_idx=random.randint(0,2)
playerinput1=computer[rand_idx]
print(playerinput1)

playerinput2=input("choose rock,paper or scissors")





if playerinput1=="rock" and playerinput2=="scissors" :
    print("playerinput1 wins")
elif playerinput1=="rock" and playerinput2=="paper":
    print("playerinput2 wins")
elif playerinput1=="paper" and playerinput2=="scissors":
    print("playerinput2 wins")
elif playerinput1=="paper" and playerinput2=="rock":
    print("playerinput1 wins")
elif playerinput1=="scissors" and playerinput2=="rock":
    print("playerinput2 wins")
elif playerinput1=="scissors" and playerinput2=="paper":
    print("playerinput2 wins")
else :
    playerinput1=="rock" and playerinput2=="rock" or playerinput1=="paper" and playerinput2=="paper" or playerinput1=="scissors" and playerinput2=="scissors"
    print("you have a tie whatcha wanna do")
   