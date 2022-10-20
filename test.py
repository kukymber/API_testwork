import os
# if 'src' in os.listdir():
#     print(os.listdir('src'))
all = []
for root, dirs, files in os.walk('src'):
    all.extend(files)
    all.extend(dirs)
print(all)

