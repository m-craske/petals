#
# File: cramy021_petals.py
# Author: Marc Craske
# Email Id: cramy021
# Date: 2020.04.22
# Description: Programming Assignment 1 - Petals Around the Rose
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Printing student information to screen.
print('File     : cramy021_petals.py')
print('Author   : Marc Craske')
print('Email Id : cramy021')
print('Description: Programming Assignment 1 - Petals Around the Rose')
print('This is my own work as defined by the University\'s Academic Misconduct policy.')

# Import random and dice libraries to simulate the use of dice, and display graphics to screen.
import random
import dice

# Declare variables for number of games played, correct and incorrect guesses, and win and lose streak.
num_games = 0
num_correct = 0
num_incorrect = 0
win_streak = int()
lose_streak = int()

# Print the introduction to screen.
print('\nPetals Around the Rose')
print('----------------------')
print('\nThe name of the game is \'Petals Around the Rose\'. The name of the')
print('game is important. The computer will roll five dice and ask you to')
print('guess the score for the roll. The scope will always be zero or an')
print('even number. Your mission, should you choose to accept it, is to')
print('work out how the computer calculates the score. If you succeed in')
print('working out the secret and guess correctly four times in a row, you')
print('become a Potentate of the Rose.')

# Ask user if they'd like to play the game. If not, display text. Otherwise, continue on. Also error checks
# for correct user response.
play = input('\nWould you like to play Petals Around the Rose [y|n]? ')

while play != 'n' and play != 'y':
    print('Please enter \'y\' or \'n\'.')
    play = input('Would you like to play Petals Around the Rose [y|n]? ')
if play == 'n':
    print('No worries... another time perhaps... :\)')
else:

    # Define variable to play again. While this is true, run the program.
    play_again = 'y'
    
    while play_again == 'y':
        
        # Declare variables for each die rolled.
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        die5 = random.randint(1, 6)
    
        # Show dice roll to screen,
        dice.display_dice(die1, die2, die3, die4, die5)
    
        # Declare answer variable. Calculate the answer based on dice rolls.
        answer = 0
        if die1 == 3:
            answer += 2
        if die1 == 5:
            answer += 4
        if die2 == 3:
            answer += 2
        if die2 == 5:
            answer += 4
        if die3 == 3:
            answer += 2
        if die3 == 5:
            answer += 4
        if die4 == 3:
            answer += 2
        if die4 == 5:
            answer += 4
        if die5 == 3:
            answer += 2
        if die5 == 5:
            answer += 4
            
        # Prompt user to enter their guess, and store as an interger in a variable.
        guess = int(input('Please enter your guess for the roll: '))
        
       
        # Compare the user's guess with the answer. Output the appropriate response to screen. Depending on the response,
        # either add 1 to games/ correct/ streak variables, or reset the running streak to 0.
        if guess == answer:
            print('\nWell done! You guessed it!')
            num_correct += 1
            num_games += 1
            win_streak += 1
            lose_streak = 0
            
            # If the win streak now equals 4, display the text below.
            if win_streak == 4:
                print('\nCongratulations! You have worked out the secret!')
                print('Make sure you don\'t tell anyone!')
                
        elif guess != answer and guess % 2 != 0:
            print('\nNo sorry, it\'s', answer, 'not', guess, '. The score is always even')
            num_incorrect += 1
            num_games += 1
            win_streak = 0
            lose_streak += 1
            
            # If the lose streak now equals 4, display the text below.
            if lose_streak == 4:
                print('Hint: The name of the game is important... Petals Around the Rose.')
                
        elif guess != answer:
            print('No sorry, it\'s', answer, 'not', guess, '.')
            num_incorrect += 1
            num_games += 1
            win_streak = 0
            lose_streak += 1
            
            # If the lose streak now equals 4, display the text below.
            if lose_streak == 4:
                print('\nHint: The name of the game is important... Petals Around the Rose.')
       
        # Prompt user to play again or now. If y, the main program loop continues.
        play_again = input('\nRoll dice again [y|n]? ')
        
        # Error check for the correct text entered.
        while play_again != 'n' and play_again != 'y':
            print('Please enter \'y\' or \'n\'.')
            play_again = input('\nRoll dice again [y|n]? ')
    
    # Display summary of the game played to screen.
    print('\nGame Summary')
    print('============')
    print('\nYou played', num_games, 'games:')
    print('    |--> Number of correct guesses:     ', num_correct)
    print('    |--> Number of incorrect  guesses:  ', num_incorrect)
    print('\nThanks for playing!')

