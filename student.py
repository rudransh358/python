import csv
f = open("Student.csv", "w", newline='')
w = csv.writer(f)
print(type(w))
w.writerow(["sid", "sname", "sadd"])
n = int(input("Enter total student number: "))
for i in range(n):
    id = input("Enter sid: ")
    name = input("Enter sname: ")
    add = input("Enter sadd: ")
    w.writerow([id, name, add])
    print("One row inserted..")
f.close()
f = open("Student.csv", "r")
r = csv.reader(f)
rowlist = list(r)
for row in rowlist:
    for value in row:
        print(value, "\t", end="")
    print()
f.close()
