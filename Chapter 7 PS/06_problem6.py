# factorial using while loop
n = int(input("Enter a number"))

product = 1
for i in range(1,n+1):
  product = product * i


print(f"the factorial of {n} is {product}")

