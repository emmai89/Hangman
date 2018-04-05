import random
import os

os.system('cls||clear')

def drawMan(numLives):
    hangman =("""\n\t\t\t 122222222222222\n
             1  2         2\n
             1 2          33\n
             12          3  3\n
             1            33\n
             1            3\n
             1         5  4  5\n
             1          5 4 5\n
             1           545\n
             1            4\n
             1            4\n
             1            4\n
             1           6 6\n
             1          6   6\n
             1         6     6\n
             1\n
             1\n
             0000000000000000000\n\n""")

    for char in hangman:
        try:
            if int(char) < (7-numLives) :
                print (char, end=' ')
            else :
                print (" ", end=' ')
        except Exception as e:
            print(char, end=' ')


f = open("words.txt")
data = f.read()
dict = data.split("\n")
random.seed()
word = dict[random.randrange(0, len(dict))]

numLives = 6
correct = False
missed = []

pool = [chr(letter) for letter in range(97, 123)]
right = []

while numLives > 0 :
    check = 0
    drawMan(numLives)
    print ("lives = ", numLives-1)
    print ("wrong guesses so far: ", ', '.join(missed))

    for x in word :
        if x in right :
            print (x, end=' ')
            check += 1
        else :
            print ("_ ", end=' ')

    if  check == len(word):
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

os.system('cls||clear')
drawMan(numLives)

if not correct :
    print("\n\nBetter Luck next time")
else :
    print("\n\n\n\nYou finally got it!!")

print("the Word was: " +word)
