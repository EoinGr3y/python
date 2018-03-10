import re

message = '123456789'

greedyRegex = re.compile(r'(\d){3,5}')
match = greedyRegex.search(message)
print(match.group())

nonGreedyRegex = re.compile(r'(\d){3,5}?')
nonGreedyMatch = nonGreedyRegex.search(message)
print(nonGreedyMatch.group())