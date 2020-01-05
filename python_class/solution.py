user_name = input('please enter your name:')
user_age = input('please enter your age:')
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='a' or user_name[0]=='A'):
    print('you can watch coco.')
else:
    print('sorry, you cannot watch coco.')