class Pycharm:
    def execute(self):
        print("Hello")

class Mine:
    def who(self):
        print("Hello")
        print("How are you")

class EXC:
    def fun(self, obj):
        obj.who()

# ide = Pycharm()

obj = Mine()

ex = EXC()
ex.fun(obj)