import random

f = open("words.txt")

data = f.read()
dict = data.split("\n")

numLives = 10
correct = False

random.seed()
word = dict[random.randrange(0, len(dict))]

pool = [chr(letter) for letter in range(97, 123)]
right = []
print (word)

while numLives > 0 and correct == False :
    print ("lives = ", numLives)

    for x in word :
        if x in right :
            print (x, end=' ')
        else :
            print ("_ ", end=' ')
    guess = input("\n\nenter a letter: ")
    
    if not guess in pool :
        print ("\nyou have already guessed " + guess)
    elif guess in word :
        right.append(guess)
        pool.remove(guess)
        print ("\nyou're one step closer")
    else :
        print("\nyou guessed wrong")
        pool.remove(guess)
        numLives -= 1
    pass
    
print(word)
