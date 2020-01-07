import os

while true:
    directory = input('Enter the full, absolute path of the directory with files whose names you want to fix:\n')
    if os.path.isdir(directory):
        break
    else:
        print(directory + 'is not a valid directory path, please try again.\n')

for x in os.listdir(directory):
    if " " in x:
        os.rename(x, x.replace(' ', '_'))

print('Done!')
