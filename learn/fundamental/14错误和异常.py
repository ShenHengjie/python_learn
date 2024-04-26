def getNum(n):
    try:
        return 10 / n
    except IOError:
        print("Error: IOError argument.")
    except ZeroDivisionError:
        print("Error: ZeroDivisionError argument.")


print(getNum(0))
