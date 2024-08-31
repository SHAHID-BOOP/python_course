f = open("D:/The ultimate Python Course/Chapter 9 PS/poem.txt")
constant = f.read()
if("twinkle" in constant):
  print("the world twinkle is present in constant")
else:
  print("world twinkle is not present in constant")
f.close()