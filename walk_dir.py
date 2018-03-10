import os

for foldername, subfolders, filenames in os.walk('c:\\Users\\eoing\\git\\udemy\\python'):
	print('The folder is ' + foldername)
	print('The subfolders in ' + foldername + ' are: ' + str(subfolders))
	print('The filenames in ' + foldername + ' are: ' + str(filenames))
	print('---------------------------------------------------------------------------------')