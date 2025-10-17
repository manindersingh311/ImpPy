#join()

mytuple = ("ram","sham","krishan")

x = " = ".join(mytuple)


print(x)# ram = sham = krishan
print(mytuple)#('ram', 'sham', 'krishan')

#ljust() left just()

txt = "banana"

# x = txt.ljust(10)#banana     is my favorite fruit.
x = txt.rjust(10) #    banana is my favorite fruit.


print(x, "is my favorite fruit.") 

#(lstrip() left strip) (rstrip right strip) (strip()) this used for remove space of the string 

txt = "     banana     " 

# x = txt.lstrip() #of all fruits banana      is my favorite
#x = txt.rstrip() # of all fruits      banana is my favorite
x = txt.strip() # of all fruits banana is my favorite

print("of all fruits", x, "is my favorite")

# maketrans() The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

f = "Hello Sam"
j = f.maketrans("S", "P")
print(j) #{83: 80}
print(f.translate(j)) # Hello Pam


# partition() 

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x) # ('I could eat ', 'bananas', ' all day')


# replace() used to replace the word string.replace(oldvalue, newvalue, count) also used
text = "hello world hello world"
print(text.replace("hello", "yellow")) # yellow world yellow world


print(text.replace("o","k",2)) #hellk wkrld hello world


# split() this make asplit words and make a list

print(text.split()) # ['hello', 'world', 'hello', 'world'] convert in list
print(text.rsplit()) # ['hello', 'world', 'hello', 'world'] convert in list

# splitlines()

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x) #['Thank you for the music', 'Welcome to the jungle']


#startswith()

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x) #True


# swapcase()

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x) #hELLO mY nAME iS peter

#translate()

mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))
 
#zfill()

txt = "50"

x = txt.zfill(10)

print(x) #000,000,00,50