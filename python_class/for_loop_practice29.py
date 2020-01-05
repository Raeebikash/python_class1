#practice for loop
# ask user name and count each character
#"Bikash Rai"
# B :1
#i:2
#k:3
#a:4
#s:5
#h:6


name = input("enter your name:")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp += name[i]

