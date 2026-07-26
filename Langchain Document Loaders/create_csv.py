import csv

data = [
    ["id", "name", "age", "department"],
    [1, "Ali Khan", 21, "Computer Science"],
    [2, "Sara Ahmed", 22, "Artificial Intelligence"],
    [3, "Usman Ali", 20, "Data Science"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV created")