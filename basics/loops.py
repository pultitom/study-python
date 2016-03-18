import sys
import random

print("----- for loop -----------------")
n = 100

the_sum= 0
counter = 1
while counter <= n:
    the_sum = the_sum + counter
    counter += 1

print("The sum from 1 to %d is %d" % (n, the_sum))

print("----- while loop -----------------")
text = ""
print("Enter some text and press Enter: ")
while 1:
    c = sys.stdin.read(1)
    text = text + c
    if c == "\n":
        break

print("Input: %s" % text)

print("----- number game with 'else' ----")

n = 20
number_to_be_guessed = int(n * random.random()) + 1
guess = 0
print("Guess a number!")
while guess != number_to_be_guessed:
    guess = int(input("Enter number: "))
    if guess > 0:
        if guess > number_to_be_guessed:
            print("Number too large")
        elif guess < number_to_be_guessed:
            print("Number too small")
    else:
        print("Sorry tou're giving up")
        break
else:
    print("Congrats! You've made it!")
        

