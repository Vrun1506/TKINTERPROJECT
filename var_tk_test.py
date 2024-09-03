import tkinter as tk
import random
import time
import os

ss=random.randint(100,500)
dmg = 1
turn = 1
defense = 0
hp = 2500
enhp = 5000
endefense = 0
a=20
burn = 1
turn2 = 0

def clickQuitButton():
	#Function for the 'quit' button
	exit()

def Shadowslice():
	global enhp
	global turn
	global dmg
	global turn2
	enhp = enhp - ss
	turn = turn - 1
	turn2 = turn2 +1
	if turn == 0:
		CPUattack()



def CPUattack():
	global turn2
	turn2 = turn2 +1
	global enhp
	global turn
	global hp
	print("The enemies health is", enhp)
	time.sleep(1.5)
	hp = hp - random.randint(50,200)
	print("Your health is" , hp)
	if hp <= 0:
		print("You lost")
		time.sleep(4)
		exit()
	else:
		if enhp <= 0:
			print("Congrats, you won!")
			exit()
		else:

			turn = turn + 1


def BurnBaby():
	global enhp
	global dmg
	global turn2
	global turn
	if turn2 >2:
		enhp = enhp-(dmg*50*turn2)
		turn = turn -1
		turn2 = turn2 -3
		if turn == 0:
			CPUattack()
	else:
		print("Your napalm is not ready, it takes 3 moves to get napalm, you are on" , turn2)

def Sharpen():
	global dmg
	global turn
	global turn2
	dmg = dmg + 75
	turn = turn - 1
	turn2 = turn2 + 1
	print("Your sword is now sharpened and your damage base is" , dmg)
	if turn ==0:
		CPUattack()

def heal():
	global hp
	global turn
	global turn2
	hp = hp + 62
	print("You have been healed, but you will be attacked!")
	turn2 = turn2+1
	turn = turn - 1
	if turn==0:
		CPUattack()

def clear():
	os.system( 'cls' )

print("Hello warrior, can you help us? We are getting attacked by those greddy goblins. Can you help save our town?")

root = tk.Tk() 
root.geometry("320x200")
#tk.TK must be capital and lowercase, as it must be in that order
#colours
root.configure(bg='black')

intro = tk.Label(root, text = "World War III") # makes a label with text
intro.configure(bg = 'red')
intro.pack(padx=20, pady=20) # puts label somewhere on the screen


quitButton = tk.Button ( text = 'Quit', command = clickQuitButton)
quitButton.place(x=0, y=0) #place allows you to choose where you put it on the screen

SButton = tk.Button ( text = 'Shadow slice', command = Shadowslice)
SButton.place(x=0, y=180) #place allows you to choose where you put it on the screen

BurnButton = tk.Button ( text = 'Burn', command = BurnBaby)
BurnButton.place(x=80, y = 180)

SharpButton = tk.Button ( text = 'Sharpen', command = Sharpen)
SharpButton.place(x=117, y = 180)

HealButton = tk.Button ( text = 'Remedy', command = heal)
HealButton.place(x=170, y = 180)


root.mainloop()
