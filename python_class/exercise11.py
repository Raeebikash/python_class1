# ask a user for name
# Example _ Bikash rai
# print count of each words
# output:
    #B:1
    #i:2
    #k:3
    #a:4
    #s:5
    #h:6
    # :7
    #r:8
    #a:9
    #i:10
name = input("enter your name:")
#bikash rai
#name.count("h"), name.count(name[0])
#name.count("i"),name.count(name[1])
# name.count("k"), name.count(name[2])
#name.count("a"), name.count(name[3])
# name.count("s"), name.count(name[4])
#name.count("h"), name.count(name[5])
# name.count(" "), name.count(name[6])
# name.count("r"), name.count(name[7])
# name.count("a"), name.count(name[8])
#name.count('i'), name.count(name[9])


#output:
#name[0] = h:2
 

temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}: {name.count(name[i])}")

    i +=1
