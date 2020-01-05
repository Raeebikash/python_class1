#replace () method
#find() 
string = "she is beautiful and she is good girl"

print(string.replace("is", "was", 2))
is_pos1 = string.find("is")
is_pos2 = string.find('is',is_pos1+1)

print(is_pos2)
