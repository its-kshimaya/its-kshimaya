import random
print("Welcome to the ALIEN GAME! ")
print("You have stolen UFO to make your way across outer space.")
print("The aliens want their UFO back and are chasing you down!")
print("Survive and out run the Aliens!"
)
done=False
miles_traveled = 0
Thirst=0
Tiredness=0

aliens_distance=-20
water_bottle=3
while done==False:
   print ("A. Drink from your water bottle")
   print ("B. Speed up at moderate speed")
   print ("C. Speed up at full speed")
   print ("D. Rest")
   print ("E. Status check")
   print ("Q.Quit")
   print("")


   choice=input("what do you want to select").upper()


   if choice == "Q":
      done==True
   elif choice =="E":
      print("Miles travelled:0")
      print("Drinks in water bottle:3")
      print("The aliens are 10 miles behind you.")

   elif choice=="D":
      Tiredness=0
      print("You are well rested and ready to continue flying the UFO")
      aliens_distance=random.randint(7,14)
   elif choice=="C":
      goforward=random.randint(10,20)
      print("miles travelled by user=21")
      Thirst+=1
      y=random.randint(1,2)
      Tiredness+=y
      x=random.randint(8,14)
      aliens_distance += x
   elif choice=="B":
      goforward=random.randint(5,12)
      Thirst+=0.5
      Tiredness+=1
      x=random.randint(6,12)
      aliens_distance+=x

   elif choice=="A":
      water_bottle =2
      Thirst=0
      print("ERROR")





  






