try:
    print("smt-1")
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Normal Termination")
