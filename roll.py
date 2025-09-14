#Imagine you want to simulate a dice roll until you get a 6:
import random
roll = 0
while roll != 6:
    roll = random.randint(1,6)
    print(" You rolled a  number :",roll)