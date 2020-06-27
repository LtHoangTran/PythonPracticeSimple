import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy. Try again.'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again.'
    elif answerNumber == 7:
        return 'My reply is no.'
    elif answerNumber == 8:
        return 'I dont feel so good.'
    elif answerNumber == 9:
        return 'Doubtful'

print('Think of a yes/no answer. Then press Enter')
input()

while True:
    print(getAnswer(random.randint(1,9)))
    print('Continue? Y/N')
    key=input()
    if key=='n':
        input('Program Stopped.')
        break
    elif key=='y' or key=='':
        continue
    elif key!='y' or key!='n':
        input('Invalid. Program Terminated.')
        break
