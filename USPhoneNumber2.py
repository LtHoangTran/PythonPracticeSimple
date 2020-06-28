import re

message='Call me 415-555-1011 tomorrrow, or 415-555-9999 for phone office'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message) # match object
print(mo)
