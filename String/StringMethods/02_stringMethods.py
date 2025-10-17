# endswith(value, start, end)

txt = "Hello, welcome to my world."

x = txt.endswith("d.",25,26)

print(x)


x = txt.endswith(("castle.", "world."))

print(x) #  true


# expandtabs(4)

a = "H\te\tl\tl\to"

print(a.expandtabs(10)) #H         e         l         l         o

# find() Searches the string for a specified value and returns the position of where it was found

print(txt.find("w")) #7

# format() Formats specified values in a string

text2 = "this is a {price:.2f} $"

print(text2.format(price = 49)) # this is a 49.00 $

# isalnum() this is used to find in string is alphabetic and numbers if there is any space in string or special character in the string return false otherwise return true

text3 = "company432343"
text4 = "company43234#3"


print(text3.isalnum())# True
print(text4.isalnum())# False


# format_map()  

myvar = {"name" : "Jane", "age" : 36, "last": "Doe"}
txt = "Happy birthday {name} you are now on level {age}! \nWishing a happy life {last}"
print(txt.format_map(myvar)) #Happy birthday Jane you are now on level 36!
#Wishing a happy life Doe

# isalpha
c = "mani"
print(c.isalpha()) #true (if there is any number in string c return false)

# isascii #The isascii() method returns True if all the characters are ascii characters  (a-z).

print(c.isascii()) # true

# isdigit() #if the string contains the digits output will be true otherwise false
d = "132324"
print(d.isdigit()) # true

# isdecimal

# e = "12.54"
e = "1254"
print(e.isdecimal()) # false
print(e.isdecimal()) # true

#isidentifier()

a = "MyFolder"
b = "Demo002"
c = "2bring" # False
d = "my demo" # False

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# islower() 	(Returns True if all characters in the string are lower case)

aa = "hello worLD"
print(aa.islower()) #False

# isupper() 	(Returns True if all characters in the string are lower case)
aa = "HELLO"
print(aa.isupper())  # True

#link for explore for methods 
# https://www.w3schools.com/python/python_ref_string.asp

#isnumeric()  # -1 and 12.4 value is not numeric values
a = "343243254" 

print(a.isnumeric()) # True

# isprintable()

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x) #true


#isspace()
txt = "   "

x = txt.isspace()

print(x) #True

# istitle()

txt = "Hello, And Welcome To My World!"

x = txt.istitle()
 
print(x) #True
 


