# name = input("Enter your name: "). lower()
# name = name.lower()   # it will work because we are giving name 
# name.lower()  it will not change because string is immutable
# print(type(name))

# name = name.upper()
# name = name.capitalize()
# name = name.title()
# print(name)

# something = "Hello world"
# print(something.find("l"))  esli net v tekste to vyvodit -1
# print(something.rfind("l"))
# print(something.index("o"))
# print(something.rindex("0"))  esli net bukvy to lomaet vyvodit error

# print(something.count("l"))    if there will not be the letter it will show 0
# print(dir (""))          # it shoows all methods, versions of this, methods
# some_str = input("Enterr your string: ").replace(" ",  "")
# some_str = input("Enterr your string: ").upper().strip()
# some_str = input("Enterr your string: ").upper().split(" ")
# .split("_")
# .replace("a",  "o")
# # .strip()                
# print(some_str)
# print(type(some_str))
# print(len(some_str))

# name = "\tAdelina \n Abdykanyeva" 
# print(dir(""))
# print(name.isalpha())
# print(name.isdigit())
# print(name.strip())
# name = input("Enter your name: ")
# age = 23
# print("Hello ", name , ". Your age is", age)
# print(f"Hello, {name}. Your age is {age}.")
# print( "hello, {0}. Your age is {1}.".format(name, age))
# a = "-".join(["a","b","c"])
# print(a)