from collections.abc import Iterable

#  迭代器
for i in "Hello":
    print(i)

print(isinstance("abc", Iterable))
print(isinstance({1, 2, 3}, Iterable))
print(isinstance(1024, Iterable))

"""

迭代器需要具有 __iter__() 和 __next__() 两个方法，这两个方法共同组成了迭代器协议，通俗来讲迭代器就是一个可以记住遍历位置的对象，迭代器一定是可迭代的，反之不成立。

__iter__()：返回迭代器对象本身
__next__()：返回下一项数据
迭代器对象本质是一个数据流，它通过不断调用 __next__() 方法或被内置的 next() 方法调用返回下一项数据，当没有下一项数据时抛出 StopIteration 异常迭代结束。上面我们说的 for 循环语句的实现便是利用了迭代器。

"""


class MyIterator:
    def __init__(self):
        self.s = "程序之间"
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 4:
            n = self.s[self.i]
            self.i += 1
            return n
        else:
            raise StopIteration


mi = iter(MyIterator())
for i in mi:
    print(i)


# 生成器
def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        print(i)
        yield data[i]


for char in reverse("Hello"):
    print(char)
