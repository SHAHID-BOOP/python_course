a = int(input("Enter you age: "))

# if statement no:1
if(a%2 == 0):
  print("a is even")
# End of if statement no:1

# if statement no:2
if(a>=18):
  print("You are above the age of consent")
  print("Good for you")

elif(a<0):
  print("You are entering an invalid age")

elif(a==0):
  print("You are entering 0 which ia not a valid age")

else:
  print("You are below the age of consent")


print("End of program")
