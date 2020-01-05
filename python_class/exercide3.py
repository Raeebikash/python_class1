#take two comomma separated inputs form user
#user's name, example -"Bikash"
#a single character


#output 2 print lines 
# users name length 
# count the character that user unputed (bonus: case insensitive count)
name, char = input("type your name and a chararcter separated by comma").split(",")
print(f"length of your name is {len(name)}")
print(f"character count:{name.count(char)}")#case sensitive
#name.lower().count()
#char.lower()
print(f"character coount:{name.lower().count(char.lower())}")



#"  Bikashssass"------->"Bikash"----->"bikash"
#"   b   "-------------->"B"----------->"b"
#name.strip().lower().count()
#char.strip().lower()

print(f"character count: {name.strip().lower().count(char.strip().lower())}")