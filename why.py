#
#thetupleduple=(6,10,15,20)
#f=(1)
#for i in thetupleduple:
 #f*=i 
 #print(f)
 #tuples=thetupleduple+f
#print(tuples)


#foodtuples=("burger","sandwich","pizza","coffee","fries")
#print(foodtuples)
#rint(len(foodtuples))
#foodtuples[1
tries=5
guess=91
for i in range(0,5): 
  x=int(input("put a number"))
  if x>guess:
        print("too hig bruh you a goober")
  elif x<guess:
        print("too low bruh you still a goober")
  elif x==guess:
   print("congratulations")
else:
    tries==0
    print('you a goober')