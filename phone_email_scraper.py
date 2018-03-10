#! python3

import re, pyperclip

message = 'Agent Alice gave the package to Agent Bob'

phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?			#area code
(\s|-)								#first separator
(\d\d\d)							#first 3 digits
-									#separator
(\d\d\d\d)							#last 4 digits
(((\s(ext(\.)?\s)|x))(\d{2,5}))?	#extention
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+		#name
@					#@symbol
[a-zA-Z0-9_.+]+		#domain
''', re.VERBOSE)

text = pyperclip.paste()

extractedNumbers = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedNumbers:
	allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmails)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmails)

pyperclip.copy(results)