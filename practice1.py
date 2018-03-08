#!python3 
'''spam = 1
if spam == 1:
	print("Hello")
elif spam == 2:
	print("Howdy")
else:
	print("Greeting")

for i in range(1,11):
	print(i)
i=1
while(i<11):
	print(i)
	i = i + 1'''
import random
secretnumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20")
for i in range(1,7):
	print("Take a guess")
	answer = int(input())
	if answer == secretnumber:
		print("Good job! You guessed my number in "+str(i)+" guesses!")
		break
	elif answer < secretnumber:
		print("Your guess is too slow")
		continue
	else:
		print("Your guess is too high")


