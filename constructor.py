class A:
    def __init__(self, a, b=None):
        if b is not None:
            print("double parameterized constructor call..")
            print("one object created")
            print("Arguments are {},{}".format(a, b))
        else:
            print("single parameterized constructor call..")
            print("one object created..")
            print("argument=", a)

# Object creation
obj = A(10)
obj1 = A(100, 200)
