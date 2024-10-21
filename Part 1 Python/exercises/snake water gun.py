import random

user = int(input(("choose from snake(0) water(1) and gun(2): ")))
comp = random.randrange(1, 4) 

sol = [["Draw", "Win", "Loss"], ["Loss", "Draw", "Win"], ["Win", "Loss", "Draw"] ]


print(sol[user][comp])