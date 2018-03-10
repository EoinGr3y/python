import os

path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(path)

cwd = os.getcwd()
print('cwd: ' + cwd)

absPath = os.path.abspath('error.py')
print('absPath: ' + absPath)

dirName = os.path.dirname(absPath)
print('dirName: ' + dirName)

baseName = os.path.basename(absPath)
print('baseName: ' + baseName)