# function practice
def last_char(name):

    return name[-1]
    
print(last_char("bikash yamphu rai"))
#last_char(9) # eerror


def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_even(10))   




def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"
print(odd_even(7)) 


def is_even(num):
    if num%2 == 0:
        return "true"
    else:
        return "false"

print(is_even(6))






def is_even(num):
    return num%2 == 0 # true

print(is_even(8))

