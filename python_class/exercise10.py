# problem
# ask user to input a number conatining more than one digit
# example - 1234
# calculate 1+2+3+4 and print


# algorithm -(method to solve problem in human language)
# ask input in string, i.e. don't change string to int]
# example- "12345"
# pick string character one by one and change to int
# int(example[0])+int(exmaple[1])....go upto len(examle)
number = input("enter a number")
# "12345", #length = 5, last index = 4
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i +=1
print(f"total numbers are{total}")