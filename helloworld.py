print("hello", "world", "welome", "python" ,sep=" ")
print("leptop","mouse","keyboard",sep="|")
name="ravi" 
age="22"
city="chennai"
print(name,age,city,sep='-')
name="meena" 
age="20"
student="true"
print(name)
print(age)
print(student)
word="python" 
print("First letter:",word[0])
print("Third letter",word[2])
print("last letter",word[-1])
print(25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)
print(3+2*5**2)
num=100
num/=10
print(num)
print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)
a = "apple"
b ="Apple"
print(a ==b)
print(10>5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))
numbers =[10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)
a = 6
b = 3
print(a^b)
a= 10
b= 6
print(a & b)
x=12
y=5
print(x | y)
num = 8
print(~num)
a = 15
b = 9
print(a ^ b)
num = 7
print(num << 2)
num = 20
print(num >> 1)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = a & b
print("And result:", result)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = a ^b
print("XOR result:", result)
s = "hi"
print(s * 5)
s = "phthon"
print(s *3 )
s1 = "super"
s2 = "man"
print(s1 + s2)
a = "hello"
b = " "
c = "world"
print(a + b + c)
name = input("Enter your name:")
print(name * 5)
str1 = input("Enter first string: ") 
str2 = input("Enter second string: ")
print(str1 + str2)
name = input("enter your name: ")
print(type(name))
age = input("enter your age: ")
age = int(age)
print(age)
print(type(age))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a+b 
print("sum =",sum)
m1 = int(input("Enter first mark: "))
m2 = int(input("Enter second mark: "))
avg = (m1 + m2) / 2
print("average =", avg)
a = int(input("Enter first number (a): "))
b = int(input("Enter second marnumber (b): "))
result = 3*a*2+b-2
print("result:",result)
num = input("Enter a number: ")
print("Before type casting:")
print("Value:", num)
print("Data type:", type(num))
num = int(num)
print("\nAfter type casting:")
print("Value:", num)
print("Data type:", type(num))
num = input("Enter a number: ")
print("Last digit:", num[-1])
num = int(input("Enter a number: "))
unit_digit = num 
print("Unit digit:", unit_digit)

num = int(input("Enter a number: "))
print("Number after removing last digit:", num //10) 
num = int(input("Enter a number: "))
print("Second last digit:", (num // 10) % 10)

num = int(input("Enter a 5 digit number: "))
print("Last digit:", num % 10)

if 10 >= 5:
    print("10 is greater than or equal to 5")

num = int(input("Enter a number: "))
if num > 50:
    print("Number is greater than 50")
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
num = int(input("Enter a number: "))
if num > 100:
    print("Number is greater than 100")
num = int(input("Enter a number: "))
if num >= 0:
    print("Number is greater than or equal to 0")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")
num = int(input("Enter a number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Rejected")
else:
    print("Rejected")
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
num = int(input("Enter number (1-7): "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
num = int(input("Enter number (1-3): "))
match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
num = int(input("Enter number (1-4): "))
match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")

