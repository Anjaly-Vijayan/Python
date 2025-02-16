import random
print("Snake Water Gun game")

'''Snake drinks Water → Snake wins
Water drowns Gun → Water wins
Gun kills Snake → Gun wins
If both players choose the same option, it's a tie.'''

choices=["snake","water","gun"]
computer=random.choice(choices)
user=input("Enter your choice (snake/gun/water):")
#print("Computer choice  : ",computer)
if user==computer:
    print("Its a draw !")
elif(user not in choices):
    print("invalid choice")

elif((user=="snake" and computer=="water") or  (user=="water" and computer=="gun") or (user=="gun" and computer=="snake")):
    print("You win !")
else:
    print("Computer win!")
        