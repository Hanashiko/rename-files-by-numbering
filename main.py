import os

path = 'C:\\розділ 30\\оріг'
files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(index + 1))+".jpg")
