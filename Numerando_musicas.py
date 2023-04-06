import os

folder = r'Musicas\\'

def numerando():
    cont = 1
    for file_name in os.listdir(folder):
        old_name = folder + file_name
        new_name = folder + '{0:03d} - '.format(cont) + file_name
        cont+=1
        os.rename(old_name, new_name)

def rm_numeracao():
    for file_name in os.listdir(folder):
        old_name = folder + file_name
        parte = file_name.split(".")
        new_name = folder + parte[1] + ".mp3"
        os.rename(old_name, new_name)

# rm_numeracao()
numerando()
print(os.listdir(folder))