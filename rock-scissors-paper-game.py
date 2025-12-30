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
print()

'''generate random choice'''
things= ['scissors','rock','paper']
#computer_choice= random.choice(things)
#print(computer_choice)

user_mark= 0
computer_mark=0

'''get inputs from user'''
print('To game over enter -1')
while True:
    computer_choice= random.choice(things)
    user_input= input('Enter your choice: ').lower().strip()
    if user_input == '-1':
        break

    elif user_input == 's' or user_input == 'sc' or user_input == 'sci' or user_input == 'scis' or user_input == 'sciss' \
                            or user_input == 'scisso' or user_input == 'scissor' or user_input == 'scissors':
        user_input= 'scissors'
        if user_input == 'scissors' and computer_choice == 'paper' :
            print('You won.')
            user_mark += 1
        elif user_input == computer_choice:
            print('Both are same.')
            pass
        else:
            print('You lose.')
            computer_mark += 1 

    elif user_input == 'r' or user_input == 'ro' or user_input == 'roc' or user_input == 'rock' :
        user_input= 'rock'
        if user_input == 'rock' and computer_choice == 'scissors' :
            print('You won.')
            user_mark += 1
        elif user_input == computer_choice:
            print('Both are same.')
        else:
            print('You lose.')
            computer_mark += 1

    elif user_input == 'p' or user_input == 'pa' or user_input == 'pap' or user_input == 'pape' or user_input == 'paper':
        user_input = 'paper'
        if user_input == 'paper' and computer_choice == 'rock':
            print('You won')
            user_mark += 1
        elif user_input == computer_choice:
            print('Both are same.')
            pass
        else:
            print('You lose.')
            computer_mark += 1
    else:
        print('Something Went Wrong.')
    print()
    
diff_mark = 0
if user_mark > computer_mark:
    diff_mark = user_mark- computer_mark
elif computer_mark > user_mark:
    diff_mark = computer_mark - user_mark
else:
    pass

print(f'Your mark is {user_mark}.')
print(f"The progarame's mark is {computer_mark}.")
print(f'You won by {diff_mark} marks.')
print()

print('End')
