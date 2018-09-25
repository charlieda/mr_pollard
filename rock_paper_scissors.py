#!/bin/python3
print('''Let\'s play a game.
''')
def playgame():
  player = input('Rock (1), paper (2) or scissors (3)?')
  player = int(player)
  if player ==1:
    print ('You choose rock.')
  elif player ==2:
    print ('You choose paper.')
  elif player ==3:
    print ('You choose scissors.')
  else:
    print ('Please type 1, 2, or 3.')
    playgame()
  import time
  time.sleep(1)
  print('''Nice.
  ''')
  time.sleep(2)
  print('1...')
  time.sleep(1)
  print('2...')
  time.sleep(1)
  print('''3!
  ''')
  time.sleep(1)
  from random import randint
  chosen = randint(1,3)
  if chosen==1:
    print('Your opponent chooses rock.')
  elif chosen==2:
   print('Your opponent chooses paper.')
  elif chosen==3:
    print('Your opponent chooses scissors.')
  time.sleep(1)
  if player==chosen:
    print('''It was a draw.
    ''')
    victory=2
  if (player==1 and chosen==2) or (player==2 and chosen==3) or (player==3 and chosen==1):
    victory=0
  elif (player==1 and chosen==3) or (player==2 and chosen==1) or (player==3 and chosen==2):
    victory=1
  if victory==1:
    print('''Awesome sauce! You won!
    ''')
  elif victory==0:
    print('''Bad luck...
    ''')
  again = input('Would you like to play again? y/n')
  if again == 'y':
    print('''Great!
    ''')
    playgame()
  elif again == 'n':
    print('''
    Thanks for playing Rock, Paper, Scissors.''')
  else:
    print('Please type \'y\' or \'n\'.')
playgame()
