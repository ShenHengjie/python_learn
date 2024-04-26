wf = open("./team.txt", mode="w", encoding="utf-8")
wf.write("tom\n")
wf.writelines(["Hello\n", "Python"])
# rf = open("./teams.txt", mode="r", encoding="utf-8")
# print(rf.read())
# print(rf.readline())
# print(rf.readlines())
with open("./teams.txt", mode="r", encoding="utf-8") as f:
    print(f.isatty())
    # 截取两个字节
    f.truncate(2)
    print(f.read())
