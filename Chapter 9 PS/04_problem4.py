word = "donkey"

with open("D:/The ultimate Python Course/Chapter 9 PS/file.txt","r") as f:
  content = f.read()

contentNew = content.replace(word,"#####")

with open("D:/The ultimate Python Course/Chapter 9 PS/file.txt", "w") as f:
  f.write(contentNew)