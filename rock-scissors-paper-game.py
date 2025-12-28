''' Rock, Scissors, Paper game'''

import random

print('Welcome to the Rock, Scissors, Paper Game !!!')

''' get the willingness to play the game from user'''
while True:
    print() #get a blank line
    playing= input('Do you want to play the game?(yes/no)\n').lower()   # get input in lowercase 
    if playing == 'yes' or playing == 'no':
        if playing == 'yes':
            print("Ok Lets' play... ")
            print()
            break
        else:
            exit()
    else:
        print('***Enter only yes/no***')
        
'''display the game rules'''
print('Winning rules of the game ROCK SCISSORS PAPER are:\n\n' \
    'Rock vs Paper     -> Paper wins\n' \
    'Rock vs Scissors  -> Rock wins\n' \
    'paper vs Scissors -> Scissors wins') 
print()
print('Enter Your Choice\n' \
      'Rock     - r\n' \
      'Scissors - s\n' \
      'paper    - p')
