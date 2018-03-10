import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

# https://www.google.ie/maps/place/870+Valencia+St,+San+Francisco,+CA+94110,+USA/
webbrowser.open('https://www.google.ie/maps/place/' + address)