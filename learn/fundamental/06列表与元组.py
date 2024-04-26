# 列表
l = [1024, 0.5, "Python"]
print("l[0] -->", l[0])
print("l[1:] -->", l[1:])
# 修改列表中第二个元素
l[1] = 5
# 向列表中添加新元素
l.append("Hello")
print("l[1] -->", l[1])
print("l -->", l)
# 删除列表中第二个元素
del l[1]
print("l -->", l)
# 元组
t = (1024, 0.5, "Python")
print("t[0] -->", t[0])
print("t[1:] -->", t[1:])
# 元组中元素不能被修改，我们要用重新赋值的方式操作
t = (1024, 0.5, "Python", "Hello")
print("t -->", t)

# 练习
listA = [54, 33, 10, 9, 77, 22]
listB = []
for item in listA:
    if item > 20:
        listB.append(item)
listB.append(28)
listB.sort()
listB.pop()
for item in listB:
    print(item)
