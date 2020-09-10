#Alexis Sullivan
import random
bet = int(input('select number between 1 and 10: '))
gamble = random.randint(1,10)
print(bet)
print(gamble)
if bet==gamble:
  print('win!')
else: print('lose')