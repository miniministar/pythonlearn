def printname(str):
    print(str)
    return


printname("张三")
printname(
    ['a', 'b', 'c']
)

class Myclass:
    i = 123
    def f(self):
        return "hello world"
    def to_string(self):
        print(self.i)
        return
    def __init__(self, i):
        self.i = i

x = Myclass(2)
print(x.i)
x.to_string()

y = Myclass(10)
print(y.to_string())