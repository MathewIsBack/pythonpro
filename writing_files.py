# employees = ["Eugene", "Gavin", "Tray", "David"]

# file_path = "C:/Users/user/Desktop/output.txt.txt"

# try:
#     with open(file=file_path, mode="a") as file:
#         for employee in employees:
#             file.write("\n" + employee)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")



# import json

# employee = {
#     "name" : "Eugene",
#     "age" : 30,
#     "job": "Cook"
# }

# file_path = "C:/Users/user/Desktop/output.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")



import csv

employees = [["Name","Age","Job"],
             ["Eugene", 30 ,"Cook"],
             ["Splint", 26 ,"Unemployed"],
             ["Andrey", 25 ,"Engineer"]]

file_path = "C:/Users/user/Desktop/output.csv"

try:
    with open(file=file_path, mode="w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")