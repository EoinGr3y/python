import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999.'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
listOfMatches = phoneNumberRegex.findall(message)
print(listOfMatches)