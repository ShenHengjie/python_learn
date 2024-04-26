d = dict(name="小明", age="18")
print(d["name"])
print(d.get("name"))
# 集合
s = {"a", "b", "c"}
# 使用 set 函数
s = set(["a", "b", "c"])
# 空集合
s = set()

# 练习
dict1 = {}
dict2 = {"name": "小明", "age": 18, "height": 20}
print(dict2["name"])
print(dict2.get("name"))

dictA = {"name": "Xiaoming", "weight": "65", "height": "173"}
dictB = {}
for key, val in dictA.items():
    dictB[val] = key
print(dictB)

dictB["nickname"] = "mingming"
print(dictB)
