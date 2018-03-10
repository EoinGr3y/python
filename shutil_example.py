import shutil, os

cwd = os.getcwd()
print(cwd)
shutil.copy('hello.txt', cwd + '\\tmp\\')