class Calculator:
    name = "Good Name"
    price = 20

    def __init__(self, name, price, H, width=10, weight=5):
        self.n = name
        self.p = price
        self.h = H
        self.wi = width
        self.we = weight

    # 定义内部函数,实现功能
    def add(self, x, y):  # self 表示本类
        print(self.name)  # 在类中使用self调用它的名字
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x - y
        print(result)

    def times(self, x, y):
        result = x * y
        print(result)

    def divide(self, x, y):
        result = x / y
        print(result)


if __name__ == "__main__":
    c = Calculator("小明", 20, 10)
    print(c.we)
    c.add(10, 20)
    c.minus(10, 20)
    c.times(10, 20)
    c.divide(10, 20)
