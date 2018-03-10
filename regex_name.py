import re

message = 'First Name: Eoin Last Name: Graham'

regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match = regex.findall(message)
print(match)