import re

message = 'Batmobilemobile lost a wheel'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)*')
match = batRegex.search(message)
print(match.group())


laughMessage = 'HaHaHaHa'

laughRegex = re.compile(r'(Ha){3,5}')
laughMatch = laughRegex.search(laughMessage)
print(laughMatch.group())