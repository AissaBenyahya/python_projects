#!/usr/bin/python3
from random import random

print(" ================== Guess Game =================")
while True:
	desired_range = input("Enter the desired range: ")
	try:
		max_range = int(desired_range)
		passed = 1
	except:
		passed = 0

	if passed == 1:
		if int(max_range) > 0:
			randN = int(random()*max_range)
			break
		else:
			print(" :::: You should put a number greater than 0 ::::")
	else:
		print(" :::: You should put a number ::::")

print(":::: Guess a number between 0 and :::: ",max_range)
while True:
	while True:
		guessed = input("::: Write your guess:")
		try:
			guess_num = int(guessed)
			error = 0
		except:
			error = 1
		if error == 0:
			if guess_num in range(max_range+1):
				if guess_num < randN:
                			print("::: the number you guess is small :::")
				elif guess_num > randN:
                			print(":::: the number is high ::::")
				else:
                			print(":::: Congratulation! you got the magic number ::::")
                			print(":::: The magic number is",randN,"the number you guessed is",guess_num," ::::")
                			break
			else:
				print(":::: The number shoud be between 0 and",max_range,"::::")
		else:
			print("::: !!! you have to write a number between 0 and 20 :::")


	while True:	
		choice = input("::: Do you play again? y/n :")
		if choice in ('y','n'):
			break
		else:
			print("::: write letter 'y' or 'n' :::")
	if choice == 'n':
		break


