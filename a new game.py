
def printing(m):
     for i in range(0,8):                                # for i in unicorn:
        print('\n')                                     # Prints Newline
        for k in range(0,8):                            #     for k in i
         print(f" {m[i][k]}",end='')          # print(k) WITHOUT NEWLINE
        print("\n")



print("THIS IS THE DINO GAME")
x=1
y=1




unicorn=[
["#","#","#","#","#","#","#","#"],
["#","&","%","_","#","#","#","#"],
["#","#","%","_","_","#","#","#"],
["#","#","_","_","%","_","^","#"],
["#","^","_","%","_","_","%","_"],
["#","#","#","_","_","_","_","_"],
["#","#","_","%","_","_","%","_"],
["#","^","_","%","_","_","_","E"]]
                              

coins=0


while True:

    printing(unicorn)
    playerinput=input("which way do you want to go right=d,left=a,up=w,down=s:      ")


    try:
        if playerinput=="w" and unicorn[x-1][y]=="_":
            x-=1
            unicorn[x][y]="&"
            unicorn[x+1][y]="_"



        elif playerinput=="w" and unicorn[x-1][y]=="^":
            x-=1
            unicorn[x][y]="&"
            unicorn[x+1][y]="_"
            coins+=1


        elif playerinput=="a"and unicorn[x][y-1]=="_":
            y-=1
            unicorn[x][y]="&"
            unicorn[x][y+1]="_"

        elif playerinput=="a"and unicorn[x][y-1]=="^":
            y-=1
            unicorn[x][y]="&"
            unicorn[x][y+1]="_"
            coins+=1

        elif playerinput=="d" and unicorn[x][y+1]=="_":
            y+=1
            unicorn[x][y]="&"
            unicorn[x][y-1]="_"


        elif playerinput=="d" and unicorn[x][y+1]=="^":
            y+=1
            unicorn[x][y]="&"
            unicorn[x][y-1]="_"
            coins+=1

        elif playerinput=="s" and unicorn[x+1][y]=="_":
            x+=1
            unicorn[x][y]="&"
            unicorn[x-1][y]="_"

        elif playerinput=="s" and unicorn[x+1][y]=="^":
            x+=1
            unicorn[x][y]="&"
            unicorn[x-1][y]="_"
            coins+=1

        elif playerinput=="d" and unicorn[x][y+1]=="%" and unicorn[x][y+2]=="_":
            y+=1
            unicorn[x][y]="&"
            unicorn[x][y-1]="_"
            unicorn[x][y+1]="%"

        elif playerinput=="a"and unicorn[x][y-1]=="%" and unicorn[x][y-2]=="_":
            y-=1
            unicorn[x][y]="&"
            unicorn[x][y+1]="_" 
            unicorn[x][y-1]="%"

        elif playerinput=="s"and unicorn[x+1][y]=="%" and unicorn[x+2][y]=="_":
        
            x+=1
            unicorn[x][y]="&"
            unicorn[x-1][y]="_"
            unicorn[x+1][y]="%"


        elif playerinput=="w"and unicorn[x-1][y]=="%" and unicorn[x-2][y]=="_":
            x-=1    
            unicorn[x][y]="&"
            unicorn[x+1][y]="_"
            unicorn[x-1][y]="%" 

        else:
            unicorn[8][8]=="E"
            print("congratulations")
         

    except IndexError:
        print("wrong move, try again ")
    








