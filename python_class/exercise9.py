#exercise one of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total form 1 to n
n = input("enter the natural number:")
n = int(n)
i = 1
total = 0
while i <= n:
    total = total + i
    i = i +1
print(f"total natural number is {total}")
