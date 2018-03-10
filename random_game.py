#Random number guessing game
import random

print('Hello, what is your name?')
name = input()
print('Well ' + name + ', I am thinking of a number between 1 and 20.')
randomNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
	print('Take a guess')
	guess = int(input())
	if guess > randomNumber:
		print('Your guess is too high.')
	elif guess < randomNumber:
		print('Your guess is too low.')
	else:
		break

if guess == randomNumber:
	print('Good job, ' + name + ' you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
	print('Nope. The number I was thinking of was ' + str(randomNumber))