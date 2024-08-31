with open("D:/The ultimate Python Course/Chapter 9 PS/log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")