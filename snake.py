#program to roll  and quit the dice
import random
count=0
while(count<=100):
	n=input("enter 'r' to roll a dice 'q' to quit")
	if (n=='r'):
		a=random.randint(1,6)
		count=count+a
		print ("my position ",count)
		print("your random value",a)
	if(count==8):
		count=37
		print("congrats u got a ladder")
	elif(count==11):
		count=2
		print("oops snake bite")
	elif(count==13):
		count=34
		print("congrats u got a ladder")
	elif(count==25):
		count=4
		print("oops snake bite")
	elif(count==38):
		count==9
		print("oops snake bite")
	elif(count==40):
		count=68
		print("congrats u got a ladder")
	elif(count==52):
		count=81
		print("congrats u got a ladder")
	elif(count==65):
		count=46
		print("oops snake bite")
	elif(count==76):
		count=97
		print("congrats u got a ladder")
	elif(count==89):
		count=70
		print("oops snake bite")
	elif(count==93):
		count=64
		print("oops snake bite")
	elif(count>100):
		print("u cant go beyond 100")
		count=count-a
	elif(count==100):
		print("u won the game")
		break
