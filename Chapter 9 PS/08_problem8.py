with open("D:/The ultimate Python Course/Chapter 9 PS/this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)