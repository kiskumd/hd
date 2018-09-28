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
OUTPUT
enter 'r' to roll a dice 'q' to quitr
my position  3
your random value 3
enter 'r' to roll a dice 'q' to quitr
my position  6
your random value 3
enter 'r' to roll a dice 'q' to quitr
my position  12
your random value 6
enter 'r' to roll a dice 'q' to quitr
my position  13
your random value 1
congrats u got a ladder
enter 'r' to roll a dice 'q' to quitr
my position  38
your random value 4
oops snake bite
enter 'r' to roll a dice 'q' to quitr
my position  44
your random value 6
enter 'r' to roll a dice 'q' to quitr
my position  47
your random value 3
enter 'r' to roll a dice 'q' to quitr
my position  52
your random value 5
congrats u got a ladder
enter 'r' to roll a dice 'q' to quitr
my position  87
your random value 6
enter 'r' to roll a dice 'q' to quitr
my position  93
your random value 6
oops snake bite
enter 'r' to roll a dice 'q' to quitr
my position  69
your random value 5
enter 'r' to roll a dice 'q' to quitr
my position  74
your random value 5
enter 'r' to roll a dice 'q' to quitr
my position  75
your random value 1
enter 'r' to roll a dice 'q' to quitr
my position  76
your random value 1
congrats u got a ladder
enter 'r' to roll a dice 'q' to quitr
my position  101
your random value 4
u cant go beyond 100
enter 'r' to roll a dice 'q' to quitr
my position  103
your random value 6
u cant go beyond 100
enter 'r' to roll a dice 'q' to quitr
my position  100
your random value 3
u won the game
