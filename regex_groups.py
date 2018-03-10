import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999.'

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phoneNumberRegex.search(message)
print(match.group(1))
print(match.group(2))