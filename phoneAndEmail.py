import pyperclip
import re

# Creat a regex for phone numbers
phoneRegex = re.compile(r'''

(
((\d\d\d)|(\(\d\d\d\)))?      # area code (optional)
(\s|-)                       # first separator
\d\d\d                       # first 3 digits
-                            # second separator
\d\d\d\d                     # last 4 digits
(((ext(\.)?\s)|x)            # extension, word part (optional)
 (\d{2,5}))?                  # extension, number part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''

[a-zA-z0-9_.+]+              # name
@                            # @ symbol
[a-zA-z0-9_.+]+              # domain name

''',re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract phone and email from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)
# print(extractedEmail)

# Copy extracted email/phone to the clipboard
result =  '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(result)

