words = ["donkey","bad","dummy"]

with open("D:/The ultimate Python Course/Chapter 9 PS/file.txt","r") as f:
  content = f.read()
for word in words:
  content = content.replace(word,"#" * len(word))

with open("D:/The ultimate Python Course/Chapter 9 PS/file.txt", "w") as f:
  f.write(content)