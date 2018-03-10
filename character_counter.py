import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message.upper():
	count[char] = (count.get(char, 0)) + 1

pprint.pprint(count)