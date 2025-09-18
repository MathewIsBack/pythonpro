# import json

# file_path = "C:/Users/user/Desktop/output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")



import csv

file_path = "C:/Users/user/Desktop/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")