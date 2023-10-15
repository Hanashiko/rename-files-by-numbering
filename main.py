import os

path = 'C:\\Users\\Hp Elitebook 840 G3\\щось\\переклад\\martial peak\\розділ 30\\оріг' # specify the path to your folder
files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(index + 1))+".jpg")
