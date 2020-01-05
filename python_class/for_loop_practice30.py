#practice for loop
# ask user a number like 1235
# calculate sum of digits ---->1+2+3+4
#l#"1256"---->logic
#num = "!@56", length = 4
#int (num[0])--->1
#int(num[1])---->2
#int(num[2])---->3
#(num[3])---->6
#i--->o to 3




total =  0
num = input("enter the number:")
for i in range(0, len(num)):
    total += int(num[i])
print(total)    