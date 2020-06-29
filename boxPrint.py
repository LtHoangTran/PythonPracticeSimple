def boxPrint(symbol, width, height):  # Make a box with "symbol" (like * or + or a), with width "width" and height "height"
    if len(symbol) != 1:              # Make sure the input string is one
        raise Exception("The 'symbol' needs to be a string of length 1")
    if (width <2) or (heigh<2):
        raise Exception("The width and height must be >=2")
    
    print(symbol * width)             # Make the top row
    for i in range (height-2):
        print(symbol +(' ' * (width-2)) + symbol)
    
    print(symbol * width)


boxPrint('**', 15,5)
