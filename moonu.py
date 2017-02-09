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

	while True:
		try:
			choice=int(input("Enter choice: "))

			if choice==1:
				kind()
				break
			elif choice==2:
				mean()
				break
			elif choice==3:
				weird()
				break
			elif choice==4:
				funny()
				break
			elif choice==5:
				fortune()
				break
			elif choice==6:
				quit()
				break
			else:
				print("Please enter a valid choice")
		except ValueError:
				print("Please enter a valid choice")
	exit

def kind():
	os.system("cowsay You look beautiful!")
	anykey=input("Press Enter to return to Main Menu")
	mainMenu()
def mean():
	os.system("cowsay You look just like my Sister!")
	anykey=input("Press Enter to return to Main Menu")
	mainMenu()
def weird():
	os.system("cowsay Have some steak!")
	anykey=input("Press Enter to return to Main Menu")
	mainMenu()
def funny():
	os.system("cowsay What do you call a cow on the barnyard floor? Ground Beef")
	anykey=input("Press Enter to return to Main Menu")
	mainMenu()
def fortune():
	os.system("fortune | cowsay")
	anykey=input("Press Enter to return to Main Menu")
	mainMenu()
def quit():
	exit

mainMenu()