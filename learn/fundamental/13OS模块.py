import os
import datetime

# 查看当前路径
print(os.getcwd())
# 返回指定目录下包含的文件和目录名列表
print(os.listdir("D:/"))
# 当前路径（相对路径方式）
print(os.path.abspath("."))
# 返回 path（文件或目录） 在系统中的创建时间。
print(
    datetime.datetime.utcfromtimestamp(
        os.path.getctime("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt")
    )
)
# 返回 path（文件或目录）的最后修改时间。
print(
    datetime.datetime.utcfromtimestamp(
        os.path.getmtime("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt")
    )
)
# 返回 path（文件或目录）的最后访问时间。
print(
    datetime.datetime.utcfromtimestamp(
        os.path.getatime("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt")
    )
)
# 判断 path（文件或目录）是否存在，存在返回 True，否则返回 False。
print(os.path.exists("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt"))
# 判断 path 是否为目录。
print(os.path.isdir("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt"))
# 判断 path 是否为文件。
print(os.path.isfile("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt"))
# 返回 path 的大小，以字节为单位，若 path 是目录则返回 0。
print(os.path.getsize("C:\\Users\\SSA-User\\Desktop\\python\\teams.txt"))
# 创建一个目录。
# os.mkdir("C:\\Users\\SSA-User\\Desktop\\python\\test")
# 将当前工作目录更改为 path。
print(os.getcwd())
os.chdir("C:\\Users\\SSA-User\\Desktop\\python\\test")
print(os.getcwd())
# 调用 shell 脚本。
print(os.system("ping www.baidu.com"))
