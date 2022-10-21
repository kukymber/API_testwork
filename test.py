import os
import pathlib

#
alls = []
alls = os.listdir('src')
print(alls)
als = []
for root, dirs, files in os.walk('src'):
    print(root, dirs)
    als.append(os.path.join(root, *dirs))
print(als)
def find_all_data(word):
    all = os.listdir(word)   #  input word, which we need for find
    if word in os.listdir():
        options_of_word = {}
        for i in range(len(all)):
            options_of_word[options_of_word[i]] = f'name:{all[i]}, ' \
                f'type:{("file" if os.path.isfile(word + "/" + all[i]) else "folder")}, ' \
                                                  f'time:{ } '
    else:
        raise HTTPException(status_code=404, detail='Wrong Data')


print(os.stat('src/config.js').st_ctime)
print(os.getcwd())
# for all in alls:
#     some_val = os.path.abspath(all)
#     print(some_val)
#     print(os.stat(os.path.abspath('config.py')).st_ctime)
# print(pathlib.Path(alls[1]))
# # for all in alls:
# print(f"'{os.path.abspath('config.py')}'")



# print(os.stat('/home/anatolii/PycharmProjects/API_test/src/config.py')[-1])
# print(os.chdir('src'))
# print(os.getcwd())

