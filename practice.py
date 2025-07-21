# strip() in strings:
k ="      hello world   "
print(k.strip())
print(k.lstrip())  #remove the white spaces in left side
print(k.rstrip())   #remove the white spaces in right side

k="!--helo--!"
print(k.strip("!-"))

# split() method in strings:
k="python is easy to understand"
print(k.split())
k="python,is,easy,to!understand"
print(k.split(","))

k="python is dynamic lang"
print(k.split(" ",2)) #--> 2, is maxsplit by " " o/p: ['python' 'is' 'dynamic lang']

# odd or even num:
x=91
if x%2==0:
    print("even")
else:
    print("odd")

#adding 2 nums:
A=15
B=21
result=A+B
print(result)

#max 3 nums are in return
for x in range(1,4):
    print(x)

#length of a list:
list=[1,2,3,4,5,6] 
print(len(list))

# sum of evens:

list =[1,2,3,4,5,6,7,8,9,10]
sum =0
for i in list:
    if i%2==0:
        sum+=i

print(sum)

#string 
Z="python is easy"
print(Z.upper())

# check a given no is div 3 and 5:
x=15
if x%3==0 and x%5==0:
    print("divisible by both")
else:
    print("not divisible")

# calculate earnings :
earn_per_hour=100 
work_hours=int(input("enter the how many hours u did work:"))
result=work_hours*earn_per_hour
print(result)

# given number is positive, negative, or zero.
num = int(input("enter a number:"))
if num>0:
    print("Positive num")
elif num<0:
    print("Negative num")
elif num==0:
    print("Zero")
else:
    print("default")

# find large one:
a=[10,20,30]
large_num=max(a)
small_num=min(a)
print(large_num)
print(small_num)

# attendence:
attendence=0
if attendence==0:
    print("Absent")
elif attendence==1:
    print("Present")
else :
    print("either present nor absent")

# skip 5 multiples:
for i in range(1,51):
    if(i%5==0):
        continue
    print(i)    
    
# a number is a multiple of both 4 and 6: 
num=int(input("enter a num:"))
num=55
if num%4==0 and num%6==0:
    print("it is mul of both")
elif num%4==0:
    print("div by 4 only")
elif num%6==0:
    print("div by 6 only")
else:
    print("it cannot be div by 4&6")
    
#gen random 1 to 100 check even or odd:
num=int(input("enter a num :"))
# for x in range(1,101):
if num%2==0:
        print("Even")
else:
        print("Odd")
 
#s.i:
principle=5000 #amount
rate = 0.05 #5%=5/100=0.05
time = 36  #3y = 3*12=36
# Simple_intrest=((principle*rate*time)/(100))
S_I=((principle*rate*time/100))
print(S_I)

# flipping a coin:
import random
for num in range (5):  #for no.of outcomes
    flip=random.randint(0,1)
    if flip==0:
        print("heads")
    else:
        print("tails")
# read from input
k= input("enter ur name:")
print(k)
# addition
K1= int(input("enter ur number1:"))
K2= int(input("enter ur number2:"))
result=K1+K2
print(result)

#I/O :FILE WRITE:
with open("my_file.txt", "w") as file:
    file.write("Hello, this is a new file!\n")
    file.write("Python is easy.")  
        
# #I/O :FILE READ:
with open("my_file.txt", "r") as file:
    print(file.read())

with open("new.txt","w")as file:
    file.write("hi!good morning")

# I/O file append:
with open("new.txt","a")as file:
    file.write("have a nice day \n")

with open("new.txt","r")as file:
    print(file.read())


# functions:
def greet():
    print("hi!")
greet()    

# using parameters:
def student(name,id):
    print( f"my name is {name} and my id.no is {id}")
student("kusuma","D8")

# using default:
def student (name="kusuma", id="d8"):
      print(f"my name is {name} and my id.no is {id}")
# student()
student("ramya","d7")
student()

def add(a,b):
      return(a+b)
result=add(10,20)
print(result)

# single inheritance:        
class A:
    def showA(self):             #parent class
        print("This belongs to A")

class B(A):
    def showB(self):           #child class
        print("This belongs to B")
# creating object
k=B()
#call
k.showB()
k.showA()

# multiple inheritance:
class college:
    def college (self):
        
        print("Name:Nriit")
class teacher(college):
    def teaching(self) :
        print("working in Nriit")
class student(teacher,college):
    def study(self):
        print("studying in Nriit")
s=student()  
s.college()
s.teaching()
s.study()

# multilevel inheritance:
class grandparent:
    def car(self):
        print("i have a car")
class parent(grandparent):
      def house(self):
              print ("i have a house of my own") 
class child(parent):
     def phone(self):
        print("i have an iphone")
c=child()
c.house()
c.phone()
c.car()

# heirarichal :
class electronics:                                  #parent
        def power(self):
             print("All electronics are run by power")
class washingmachine:
        def machine(self):                #child1
               print("used for washing cloths")
class smartphone:
     def call(self):                            #child2
        print("phone is for calling")
P=smartphone()
P.power()
P.call()
    
M=washingmachine()
M.power()
M.machine()

# hybrid:
class A:
    def methodA(self):
        print("A's method")

class B(A):
    def methodB(self):
        print("B's method")

class C(A):
    def methodC(self):
        print("C's method")

class D(B, C):
    def methodD(self):
        print("D's method")
d= D() 
d.methodA()
d.methodB()
d.methodC()
d.methodD()