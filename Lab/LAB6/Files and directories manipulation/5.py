with open("C:\\Users\\Admin\\Desktop\\pp2\\PY\\LAB6\\Files and directories manipulation\\Example.txt", "a") as txt:
    a = list(input("Write list: ").split())
    for i in a:
        txt.write(i + " ")