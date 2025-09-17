import os

file_path1 = "C:/Users/user/Desktop/test.txt.txt"

file_path = "C:/Users/user/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("The location doesn't exist")





    