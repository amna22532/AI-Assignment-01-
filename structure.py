# IF Structure
a=12
b=12
if (a==b):
    print("we respect the elder.")
# IF Else Structure
c=9
d=7
if (c==d):
    print("Hazrat Muhammad is the last prophet of ALLAH")
elif c>d:
     print("Everything will happen at the right time")
else:
     print("we are friends")

# for loop structure(For initilization, Condition)
for x in range(6):
    print(x)

for x in range(7):
    print("Happy new years")

i=0
g="n" 
for i in range(4):
      print(g)

# PROGRAM (Nested IF-else Statments)
# program 01:
age = 20
has_id =True
if age >=18:
    print(" print all Statment")
    if has_id:
         print("you are allowed to enter")
    else:
     print("you need to show your id")
else:
   print("you are not allow to enter")

# program 02:
a=200
b=100
c=9
d=12
if a==b:
    print("a is greater then b")
    if c==d:
        print("a is positive integer")
    elif d>c:
        print("c is negative")
    else:
        print("Even numbers")
elif a>b:
    print("Odd Numbers")
else:
    print("The number is zero")

# Program (For loop statments)
# program 03:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# Program 04:
text = "Hello"
for letter in text:
    print(letter)

# Program 05:
# if condition loop
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Program 06:
#  # While condition
i = 1
while i <= 5:
    print("Number:", i)
    i += 1

