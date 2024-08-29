s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))

# check for total percentage
total_percentage = (100*(s1+s2+s3))/300
if(total_percentage >= 40 and s1>=33 and s2>=33 and s3>=33):
  print("You are Passed", total_percentage)


else:
  print("You are failed", total_percentage)