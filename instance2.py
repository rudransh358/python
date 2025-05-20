class employee:
    def __init__(self, id, name, sal):
        self.eno = id
        self.name = name     # changed from ename
        self.sal = sal       # changed from esal

e = employee(100, "Rudransh", 100000)
print(e.__dict__)
print("eno =", e.eno)
print("ename =", e.name)
print("esal =", e.sal)
