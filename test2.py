import os

word = 'src'
alls = os.listdir(word)
print(alls)
print(('file' if os.path.isfile(word+'/'+alls[0]) else 'folder'))
# print(os.path.isdir(os.path.abspath(word)))
# print(os.path.abspath(word))