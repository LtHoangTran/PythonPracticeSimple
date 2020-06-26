def numberOfCat(numCat):
    try:
        if int(numCats)<0:
            return 'Negative number input.'
        elif int(numCats)>0:
            if int(numCats)>=4:
                return 'Lots of cats.'
            else:
                return 'That is not that many cats.'
    except:
        return 'Input error'

while True:
    print('How many cats?')
    numCats=input()
    print(numberOfCat(numCats))
    print('Continue? Y/N')
    key=input()
    if key=='n':
        print('Program Stopped.')
        
        break
    elif key=='y' or key=='':
        continue
    elif key!='y' or key!='n':
        print('Invalid. Program Terminated.')
        break
