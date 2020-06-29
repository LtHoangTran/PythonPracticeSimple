def boxPrint(symbol, width, height, thickness):     # Make a box with by a certain symbol, with input width, height and thickness
    if len(symbol) != 1:                            # Make sure the input string (for symbol) is one in length
        raise Exception("The 'symbol' needs to be a string of length 1")
    
    try:                                            # The input for width must be an integer
        width = int(width)
    except ValueError:
        print('Please input an integer for width')

    try:
        height = int(height)                        # The input for height must be an integer
    except ValueError:
        print('Please input an integer for height')

    try:
        thickness = int(thickness)                  # The input for thickness must be an integer
    except ValueError:
        print('Please input an integer for thickness')

    if (int(width) <2) or (int(height)<2):          # At least 3 rows and 3 columns
        raise Exception("The width and height must be >=2")

    if int(width)-int(thickness)*2 <=1:
        raise Exception('Invalid relationship between thickness and with')

    if int(thickness)<=1:                           # The thickness must be positive, and at least 1
        raise Exception('Invalid value for thickness')

    for i in range(thickness):                      # Print the top (thickness included)
        print(symbol * width)             
    
    for i in range (height-2):                      # Print the sidewall (thickness included)
        print(symbol * thickness + (' ' * (width - thickness*2) ) + symbol * thickness)
        
    for i in range(thickness):                      # Print the bottom (thickness included)
        print(symbol * width)

    input('Press enter to exit.')                   # Freeze the screen for the result, then press enter to exit

print('Please input the symbol you want to use: ')
symbol=input()

print('Please input the width: ')
width=input()

print('Please input the height: ')
height=input()

print('Please input the thickness: ')
thickness=input()

boxPrint(symbol, width, height, thickness)


