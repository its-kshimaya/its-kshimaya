def getUserIn(unicorn):
    # Get input from user
    


   return unicorn
def bold_text(text):
  text+='*'
  return text


def printing(m):
     for i in range(0,6):                                # for i in unicorn:
        # print('\n')                                     # Prints Newline
        for k in range(0,5):                            #     for k in i
           print(f" {m[i][k]}",end='')          # print(k) WITHOUT NEWLINE
        print("\n")

print("WELCOME TO WORDLE\n")
# gameboard="|_|_|_|_|_|\n|_|_|_|_|_|\n|_|_|_|_|_|\n|_|_|_|_|_|\n|_|_|_|_|_|\n|_|_|_|_|_|"

unicorn=[
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"],
    ["|_|","|_|","|_|","|_|","|_|"]
    
]

# printing(unicorn)

SecretWord="sushi"
for s in range(0,6):
    printing(unicorn)
    playerinput=input("guess a word")
    unicorn[s][0]=" "+playerinput[0] +" "
    unicorn[s][1]=" "+playerinput[1] +" "
    unicorn[s][2]=" "+playerinput[2] +" "
    unicorn[s][3]=" "+playerinput[3] +" "
    unicorn[s][4]=" "+playerinput[4] +" "
    if SecretWord==playerinput:
        print("congratulations")
    elif playerinput!= SecretWord:
        for q in range(0,5):
            if playerinput[q]==SecretWord[q]:
                unicorn[s][q]=playerinput[q].upper()
            elif playerinput[q] in SecretWord:
                unicorn[s][q]=playerinput[q]+"*"
    