class A:
    def f1(self):
        print("self parametrize instance method..")

    def f2(self, a):
        print("value of a:", a)
        self.f1()

    def f3(ob, a, b):
        print("value of a and b are {},{}".format(a, b))
        ob.f2(a + b)

obj = A()
obj.f3(10, 5)
input("Press Enter to exit...")  # k
