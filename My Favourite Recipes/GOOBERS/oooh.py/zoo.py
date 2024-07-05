# ~ ~ ~ Prints Board ~ ~ ~ #
def printing(m):
     for i in range(0,3):                                # for i in unicorn:
        print('\n')                                     # Prints Newline
        for k in range(0,3):                            #     for k in i
           print(f" {m[i][k]}",end='')          # print(k) WITHOUT NEWLINE
        print("\n")



# MAIN ~~ ~ ~ ~ ~ ~ ~ ~
# print('Hello, World!', end='') # WILL NOT MAKE A NEWLINE

unicorn=[
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]

player1inputXorO=input("player1 choose X or O: ")
if player1inputXorO=="X":
    player2inputXorO="O"
elif player1inputXorO=="O":
    player2inputXorO="X"
player2inputXorO=input("player2 choose X or O: ")
print()
    
printing(unicorn)
# ~ ~ ~ Assign Shmuck ~ ~ ~ #
for k in range(0,9):
    if k%2==0:
        symbol=player1inputXorO
    else:
        symbol=player2inputXorO
    playerinputX=int(input("pick a row enter 0 for 1 row, enter 1 for 2 row, enter 2 for 3 row: " ))
    playerinputY=int(input("pick a column enter 0 for 1 column, enter 1 for 2 column, enter 2 for 3 column: "))

    


    unicorn[playerinputX][playerinputY]=symbol
    printing(unicorn)
    if unicorn[0][0]==unicorn[0][1]==unicorn[0][2]!= "*" or unicorn[1][0]==unicorn[1][1]==unicorn[1][2]!= "*" or unicorn[2][0]==unicorn[2][1]==unicorn[2][2]!= "*" or unicorn[0][0]==unicorn[1][0]==unicorn[2][0]!= "*" or unicorn[0][1]==unicorn[1][1]==unicorn[2][1]!= "*" or unicorn[0][2]==unicorn[1][2]==unicorn[2][2]!= "*" or unicorn[0][0]==unicorn[1][1]==unicorn[2][2]!= "*" or unicorn[0][2]==unicorn[1][1]==unicorn[2][0]!= "*" :
        print("congratulations")
        break
    elif  k==8  :
        print("tie")















