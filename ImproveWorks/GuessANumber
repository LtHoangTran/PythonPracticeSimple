# Self-improved version. Guess A Number game.

import random
import sys
    
print('Guten Tag Kamerade. Please input your name: ')
name=input()
print('So, ' + name + ', you want to play a Guess the Number game?')
print('Of course you do. If not, why do you run this script?')
print('')
print('Oh, and remember, this game also feature negative whole numbers. Have fun. And good luck.')

print('Enter the lower limit of the range: ')
lowLim=input()
print('Enter the upper limit of the range: ')
upLim=input()


try:
    if int(lowLim)>int(upLim):
        print('Error input. Lower limit must be smaller than upper limit.')
        input('Program terminated.')
        sys.exit()
except:
    print('Error input. Please input numerical data')
    input('Program terminated')
    sys.exit()


print('A number has been randomly selected between ' + lowLim + ' and ' + upLim + '. Take a guess.')
print('How many times do you want to guess? Number bigger than 1, please.')
turnLim=input()

try:
    if int(turnLim)<1:
        print('Error input. The guess tries must be two times or bigger')
        input('Program terminated')
        sys.exit()
except:
    print('Error input. Please input numerical data')
    input('Program terminated')
    sys.exit()
    

secretNumber=random.randint(int(lowLim),int(upLim))
for guessTaken in range(1,int(turnLim)+1):
    print('What is your guess?')
    guess=int(input())
    if guess<secretNumber:
        print('Your guess is too low.')
    elif guess>secretNumber:
        print('Your guess is too high.')
    else:
        break # Correct guess
print('')
            
if guess==secretNumber:
    print('Good job, ' + name + '! You guess my number in ' +str(guessTaken)+ ' turn(s)')
else:
    print('Nope. The number I was thinking of was ' +str(secretNumber))

print('')
input('Program terminated. Press enter to exit')  
                
    




