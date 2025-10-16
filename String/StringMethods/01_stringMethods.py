# capitalize()
text = "hello World"

a = text.capitalize()

print(a) #Hello world # only first word is upper case other words convert in lower case

b = text.upper()

print(b) # HELLO WORLD 


c = text.lower()

print(c) #hello world

d = text.count("h")  

print(d) #output = 1  (to find how many letters in the string)


e = text.title()

print(e) #Hello World (in string every words first character is convert in upper case)

f = text.casefold()

print(f) # hello world using this string convert in lower case

g = text.center(33,"*")

print(g)  #***********hello World***********

h = text.endswith("d")

print(h) # True (return true and false)
