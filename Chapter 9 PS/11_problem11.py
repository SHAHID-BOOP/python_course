with open("D:/The ultimate Python Course/Chapter 9 PS/old.txt") as f:
    content = f.read()

with open("D:/The ultimate Python Course/Chapter 9 PS/renamed_by_python.txt", "w") as f:
    f.write(content)