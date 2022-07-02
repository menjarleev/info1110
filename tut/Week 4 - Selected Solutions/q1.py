import sys

word_to_guess = sys.argv[1]

guess = input("Guess the word!")

while guess != word_to_guess:
	print("Wrong! Guess again!")
	guess = input("Guess again")

print("Correct congratulations")
