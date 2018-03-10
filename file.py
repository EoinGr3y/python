import os

helloPath = os.path.abspath('hello.txt')
print('helloPath: ' + helloPath)

helloFile = open(helloPath)
content = helloFile.readlines()
helloFile.close()

print(content)