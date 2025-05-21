import csv
f=open("Employee.csv","w")
w=csv.writer(f)
print(type(w))
w.writerow(["eid","ename","esal"])
n=input(input("enter total employee number:"))
for i in range(n):
    id=input("enter eid:")
    name=input("enter ename:")
    print("one row inserted..")
f.close()