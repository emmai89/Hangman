import os
from Game import begin

os.system('cls||clear')

while True :
    option = input("""\n\nWhat do you want to do?
    1. Play
    2. quit\n >>>> """)

    if option == "1":
        begin()
    else:
        print("bye")
        break
