f = open("D:/The ultimate Python Course/Chapter 9/file.txt")

print(f.read())
      
f.close()

# the same can be written using with statemnet like this:
with open("D:/The ultimate Python Course/Chapter 9/file.txt") as f:
  print(f.read())

# you dont have to explicity close the file
