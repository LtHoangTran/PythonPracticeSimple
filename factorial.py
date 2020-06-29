import logging
logging.basicConfig(filename='MyProgramLog.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # send the log of debug to another text file, created in the same folder as the python script
#logging.disable(logging.CRITICAL)      # delete the hastag at the beginning to deactivate the logging program

logging.debug('Start of program')


def factorial(n):
    logging.debug('Begin factorial(%s)' % (n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print('Enter the value of n:')
n=int(input())
print(factorial(n))
logging.debug('End of program')
