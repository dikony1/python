import os 
file_path ='A.txt'

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"ERROR: You do not have permission to delete {file_path}.")
else:
    print(f"ERROR: {file_path} does not exist.")