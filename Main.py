import random
import os

f = open("words.txt")
data = f.read()
dict = data.split("\n")
random.seed()
word = dict[random.randrange(0, len(dict))]

numLives = 10
correct = False
missed = []

pool = [chr(letter) for letter in range(97, 123)]
right = []

while numLives > 0 :
    check = 0
    print ("lives = ", numLives)
    print ("wrong guesses so far: ", missed)

    for x in word :
        if x in right :
            print (x, end=' ')
            check += 1
        else :
            print ("_ ", end=' ')
            
    if  check == len(word):
        print("\n\n\n\nYou finally got it!!")
        correct = True
        break
        
    guess = input("\n\nenter a letter: ")
    os.system('cls||clear')

    if not guess in pool :
        print ("\nyou have already guessed " + guess)
    elif guess in word :
        right.append(guess)
        pool.remove(guess)
        print ("\nyou're one step closer")
    else :
        print("\nyou guessed wrong")
        missed.append(guess)
        pool.remove(guess)
        numLives -= 1

    pass

if not correct :
    print("Better Luck next time")

print("the Word was: " +word)
