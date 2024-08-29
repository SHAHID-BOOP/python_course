d = {} # empty dictionary
marks = {
  "shahid": 99,
  "pankaj":97,
  "shubham": 54,
  }


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"shahid":90})
print(marks)

print(marks.get("shahid2")) # prints none
print(marks["shahid2"])     # returns an error