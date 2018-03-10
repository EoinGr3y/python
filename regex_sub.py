import re

message = 'Agent Alice gave the package to Agent Bob'

regex = re.compile(r'Agent \w+')
sub = regex.sub('REDACTED', message)
print(sub)

letterRegex = re.compile(r'Agent (\w)\w*')
letterSub = letterRegex.sub(r'Agent \1', message)
print(letterSub)