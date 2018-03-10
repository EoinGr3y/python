import shelve

shelfFile['stuff'] = ['rope', 'tyre', 'flowers']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['stuff'])