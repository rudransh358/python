with open("xyz.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        print(line)
print("is closed:",f.closed)
print("with statement end...")