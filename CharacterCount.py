import pprint
message='It was a bright cold day in April, and the clocks were striking thirteen.'
count={} #'r':12 if there are 12 letters r in the string

for character in message.upper():
    count.setdefault(character,0) #clear, just to be sure
    count[character]=count[character]+1
    
    
pprint.pprint(count)
print('')
rjtext=pprint.pformat(count)
print(rjtext)
