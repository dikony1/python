import os 
path = 'lab6'

print('Directories:')
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path,entry)):
        print(entry)

        print('Files:')
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path,entry)):
        print(entry)

        print('all directories and files:')
for entry in os.listdir(path):
    print(entry)