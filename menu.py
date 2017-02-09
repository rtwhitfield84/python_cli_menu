import os

def mainMenu():
	print(" ******************************* \n "  
		"Welcome to the CoWmmand Line! \n " 
		"*******************************")
	print("1. Moo something kind")
	print("2. Moo something mean")
	print("3. Moo something weird")
	print("4. Moo something funny")
	print("5. Moo your fortune")
	print("6. Quit")

	choice=int(input("Enter choice: "))

	if choice==1:
		kind()
	elif choice==2:
		mean()
	elif choice==3:
		weird()
	elif choice==4:
		funny()
	elif choice==5:
		fortune()
	elif choice==6:
		quit()
	else:
		print("Please enter a valid choice")


def kind():
	os.system("cowsay You look beautiful!")
def mean():
	os.system("cowsay You look just like my Sister!")
def weird():
	os.system("cowsay Who wants a steak?")
def funny():
	os.system("cowsay What do you call a cow on the barnyard floor? Ground Beef")
def fortune():
	os.system("fortune | cowsay")
def weird():
	os.system("qui()")

mainMenu()