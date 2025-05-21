import csv
f=open("Employee.csv","r")
r=csv.reader(f)
rowlist=list(r)
for row in rowlist:
    for value in row:
        print(value,"\t",end="")
    print()
f.close()
