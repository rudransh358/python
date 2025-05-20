class parent:
    def func1(self):
        print("instance method1 in parent")
    def func2(self):
        print("instance method2 in parnet")
class child(parent):
    def func1(self):
        print("instance method1 in child")
        super().func1()
ob=child()
ob.func1()
ob.func2()