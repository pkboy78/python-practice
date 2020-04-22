"""
a=1
b=2
c=a+b

d='test '+str(c)+"12  "
e=d[::-1]

print (d)
print (d.strip())
print (len(d))
print (len(d.strip()))

print (d.title())

a=10
b=20.54
c=True
d="I am the best"

print (a,b,c,d)

print (a<b)

lst=[10,20,'test','test2','test3']
print (lst[1:4])
lst.append('test4')
print (lst)
lst[0]=9

lst.remove('test2')
print (lst)
del(lst[0])

print (lst)

#lst[2]=lst.append('test2')
print (lst)

#print (max(lst))
#print (min(lst))

lst.remove(20)
lst.insert(0,'test2')
print (lst)
lst.sort(reverse=True)
print (lst)

#Tuple cannot be modified

tpl_test=(1,2,3,4,4,100)
print (tpl_test)
print (tpl_test.count(2))
aa=tpl_test.index(100)
print (tpl_test[aa])


s={'test1','test2','test3','test4'}

s.update(['test10','test11'])
s.remove('test10')

f=frozenset(s)
print (f)

list1=['test1', 'test2', 'test3']
list1.sort(reverse=True)
for i in list1:
    print (i)


lst=[20,30,40,234]
b=bytes(lst)
print(type(b))    

b1=bytearray(lst)
print (type(b1))
b1[1]=9

for i in b1:
    print(i)

dict1={1:"John",2:"Peter"}

print (dict1.items())

keys=dict1.keys()

for i in keys:
    print(i)

values=dict1.values()

for j in values: print(j)

del(dict1[1])

print(dict1)


countries=['China','Italy','USA']
countries.append("Canada")
print(countries)
country1=countries[0]
del(countries[0])
print(countries)
countries.insert(0,country1)
countries.insert(2,"Hong Kong")
print(countries)

count=(len(countries)-1)/2
print(count)

a,b=10,5

print("sum:",a+b)
print("sub:",a-b)
print("multiply:",a*b)
print("div:",a/b)
print("mod:",a%b)
print("power:",a**b)
print("Floor Div:",a//b) 

a=b=c=10
c=20
print (a,b,c)

print (a==b)

print (not(a==b or b!=c))

print("Test1\nTest2")

print(a,b,sep='')

firstname="Peter"
lastname="Kam"

print ("First Name is %s, Last name is %s"%(firstname,lastname))

print ("First Name is {}, last name is {}".format(firstname,lastname))

print ("First Name is {1}, last name is {0}".format(firstname,lastname))

#%i %s %f

#input1=input("Please Enter something: ")
#print ("This is what you have entered:", input1.strip(),sep='')

#intinput1=int(input("Please enter an integer:"))
#print ("This is what you have entered:",intinput1)


list=[x for x in input("input 3 numbers by comma").split(",")]
print(list)

studentid = int(input("Enter Student ID:"))
name=input("Enter Student Name:")
marks=float(input("Enter Marks scored:"))

print ("ID:", studentid, ",Name:",name,",Marks:",marks)


list=[int(x) for x in input ("Enter Three Integer numbers: ").split()]
print (list)
print ("Average:",int((list[0]+list[1]+list[2])/3))


import math
r=float(input("Enter the radius"))
#pi=22/7
area=math.pi*r*2
print(area)


x=int(input("Input a number to check:"))
if x==0:
    print (x,"is zero")
elif x%2==0:    
    print (x,"is even")
else:
    print (x,"is odd")

"""
"""
m,p,c=(int(s) for s in input("Scores for each subject (Maths, Physics, Chemistry) separated by comma: ").split(","))
pe=True
a=0
if (m<35):
    print("Your Maths exam failed")
    pe=False
if (p<35): 
    print("Your Physics exam failed")
    pe=False
if (c<35):
    print("Your Chemistry exam failed")
    pe=False

if (pe==True):
    a=(m+p+c)/3
    if (a<=59):
        print ("Your grade is C, Average score is",a)
    elif (a<=69):
        print ("Your grade is B, Average score is",a)
    else:
        print ("Your grade is A, Average score is",a)


x=0
while (x<20):
    print(x)
    x+=1


x=int(input("Enter min number:"))
y=int(input("Enter max number:"))
i=x
while(i<=y):
    print(i)
    i+=2


for i in range(50,70):
    print (i)

lst=[1,2,3,4,5]
prod=1

for i in lst:
    prod*=i

print("product is:",prod)


lst=[3,6,9,12]
for i in lst:
    if (i==9):
        break
    print(i)


a=int(input("Enter a number: "))
x=0
while(x<a):
    x+=1
    if x==100:
        break    
    if x%10==0:
        continue
    print(x)

a=int(input("Enter a number: "))
primeFlag=True
i=2
if (a<2):
    print ("Please enter a number greater than 1")
else:
    while (i<=a-1):
        #print(a,i,a%i)
        if (a%i==0):
            primeFlag=False
            break
        i+=1
if primeFlag==True:
    print(a,"is a Prime No")     
else:
    print (a, "is NOT a Prime No")   


import sys
lst=sys.argv

for i in lst:
    print(i)



def average(a,b):
    #print("Average of 2 numbers:",(a+b)/2)
    return (a+b)/2

print (average(3,9))


def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u

lst=calc(5,10)
print(lst)

for i in lst: print(i)


x=123

def display():
    x=768
    print(x)
    print(globals()['x'])

print(x)
z=display
z()
z()
z()


def display(name):
    def message():
        return "Hello "
    result=message()+name
    return result

print(display("Peter"))


def display(fun):
    return "Hello "+fun

def name():
    return "Peter"

print(display(name()))


def display():
    def message():
        return "Hello "
    return message

fun=display()
print(fun())
            


def fun(lst):
    for i in lst:
        print(i)

fun([1,2,3,4])



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def average(a,b):
    return (a+b)/2

print(average(a=2,b=4))



def cube(n):
    return n**3

print(cube(2))


f=lambda n:n**3
print(f(2))



a=lambda x: 'YES' if x%2==0 else 'NO'
print (a(6))


def add(a,b):
    return (a+b)

print(add(2,3))


t=lambda a,b:a+b
print(t(10,20))


lst=[10,2,33,45,89,2]

result=list(filter(lambda x:x%2==0,lst))

print(result)



lst=[2,3,4,5]
result=list(map(lambda n:n*2,lst))

print(result)


from functools import reduce

lst=[5,10,15,20]
result=(reduce(lambda x,y:x+y,lst))

print(result)



def decor(fun):
    def inner():
        result = fun()
        return int(result)*2
    return inner

@decor
def num():
    return 5

#resultfun=decor(num())
#print(resultfun())
print(int(num()))


def decorfun(fun):
    def inner(n):
        result=fun(n)
        result+=" how are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print (hello("Peter"))



def customgen(x,y):
    while x<y:
        yield x
        x+=1

result=customgen(20,30)

for i in result:print(i)


lst=[]
for x in range(1,11):
    lst.append(x**3)
print(lst)


lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)

lst=[x for x in range(2,21,2)]
print (lst)

lst=[x for x in range(1,21) if x%2==0]
print (lst)

a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]

for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)

z=[a[i]*b[i] for i in range(len(a))]
print(z)

a=[2,4,6,8]
b=[1,2,3,4]
result=[]

#for i in a:
#    if i in b:
#        result.append(i)
#print(result)

result=[i for i in a if i in b]
print(result)


class Product:
    
    def __init__(self):
        self.name='IPhone'
        self.description='Good'
        self.price=700

    def display(self):
       print(self.name)
       print(self.description)
       print(self.price)



p1=Product()
p1.display()

class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings

    def average(self):
        lenRatings=len(self.ratings)
        average=sum(self.ratings)/lenRatings
        return average

test=Course("Python Course",[1,2,3,4,5])

print(test.name)
print(test.ratings)

test2=Course("Python Course 2",[1,2,3,4,6])
print(test2.name)
print(test2.ratings)

print("1st Average is:",test.average())
print("2nd Average is:",test2.average())


class Programmer:
    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.sal=sal
    
    def getSalary(self):
        return self.sal
    
    def setTechnologies(self,tech):
        self.tech=tech
    
    def getTechnologies(self):
        return self.tech

p1=Programmer()
p1.setName("Peter")
p1.setSalary(10000)
p1.setTechnologies(["Python","K8S"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())


class Student:
    major = "CSE"

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    
    @staticmethod
    def display():
        #print(self.name)
        print(Student.major)

s1=Student(1,"John")
s2=Student(2,"Bill")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
s1.display()
Student.display()


class ObjectCounter:
    nob=0

    def __init__(self):
        ObjectCounter.nob+=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.nob)

o1=ObjectCounter()

ObjectCounter.displayCount()



class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class Engine:
        def __init__(self,number):
            self.number=number

        def start(self):
            print("Engine Started:",self.number)

c=Car("BMW","2017")
e=c.Engine(123)

e.start()


#name mangling
class Student:
    def __init__(self):
        self.__id=123
        self.__name="John"
    
    def display(self):
        print(self.__id)
        print(self.__name)


s=Student()
s.display()
print(s._Student__id)
print(s._Student__name)


#encapsulation example

class Student:
    def setId(self,id):
        self.id=id
    
    def returnId(self):
        return self.id
    
    def setName(self,name):
        self.name=name

    def returnName(self):
        return self.name


s=Student()

s.setId(123)
s.setName("John")

print(s.returnId())
print(s.returnName())


class Patient:
    def setPatientId(self,id):
        self.id=id

    def setPatientName(self,name):
        self.name=name

    def setPatientSSN(self,ssn):
        self.ssn=ssn

    def getPatientId(self):
        print(self.id)

    def getPatientName(self):
        print(self.name)

    def getPatientSSN(self):
        print(self.ssn)


p=Patient()
p.setPatientId(123)
p.setPatientName("Peter")
p.setPatientSSN("123-45-6789")

p.getPatientId()
p.getPatientName()
p.getPatientSSN()


class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the Car: ",self.make)

    def stop(self):
        print("Stopping the Car: ",self.make)


class ThreeSeries(BMW):
    def __init__(self,cruiseContorlEnabled,make,model,year):
        #BMW.__init__(self,make,model,year)
        super().__init__(make,model,year)
        self.cruiseContorlEnabled=cruiseContorlEnabled

    def display(self):
        print(self.cruiseContorlEnabled)

    #def start(self):
        #print("Starting the 3 Series Car: ",self.make)

class FiveSeries(BMW):
    def __init__(self,parkAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkAssistEnabled=parkAssistEnabled

    def start(self):
        super().start()
        print("Starting the 5 Series Car: ",self.make)


ts=ThreeSeries(True,"BMW","328i","2018")
print(ts.cruiseContorlEnabled)
print(ts.make)
print(ts.model)
print(ts.year)
ts.start()
ts.stop()
ts.display()

fs=FiveSeries(False,"BMW","528i","2019")
fs.start()
#ts.start()

class Duck:
    def talk(self):
        print("Quack")

class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)

class Engine:
    def __init__(self,engine):
        self.engine=engine

    def display(self):
        self.engine.start()


class FerrariEngine:
    def start(self):
        print("Ferrari Engine")

f=FerrariEngine()
e=Engine(f)
e.display()


x=10
y=20

print(x+y)

s1="Hello"
s2="How are you"
print(s1+s2)

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)


from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the Car: ",self.make)

    def stop(self):
        print("Stopping the Car: ",self.make)
    
    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self,cruiseContorlEnabled,make,model,year):
        #BMW.__init__(self,make,model,year)
        super().__init__(make,model,year)
        self.cruiseContorlEnabled=cruiseContorlEnabled

    def display(self):
        print(self.cruiseContorlEnabled)
    
    def drive(self):
        print("Drive 3 series")

    #def start(self):
        #print("Starting the 3 Series Car: ",self.make)

class FiveSeries(BMW):
    def __init__(self,parkAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkAssistEnabled=parkAssistEnabled

    def start(self):
        super().start()
        print("Starting the 5 Series Car: ",self.make)

    def drive(self):
        print("Drive 5 series")


ts=ThreeSeries(True,"BMW","328i","2018")
print(ts.cruiseContorlEnabled)
print(ts.make)
print(ts.model)
print(ts.year)
ts.start()
ts.stop()
ts.display()

fs=FiveSeries(False,"BMW","528i","2019")
fs.start()
#ts.start()


from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
        
    def scroll(self):
        print("HP scroll")
    
    @abstractmethod
    def click(self):
        pass

class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Dell scroll")

    @abstractmethod
    def click(self):
        pass

class HPNoteBook(HP):

    def click(self):
        print("HPNoteBook click")

class DellNoteBook(Dell):

    def click(self):
        print("DellNoteBook click")

hpnb=HPNoteBook()
dnb=DellNoteBook()

hpnb.click()
dnb.click()
hpnb.scroll()
dnb.scroll()


import logging
logging.basicConfig(filename="test-log.txt",level=logging.DEBUG)

logging.critical("critical")
logging.error("error")
logging.warning("Warn")
logging.debug("debug")
logging.info("info")


try:
    f=open("test.doc","a")
    a,b=[int(x) for x in input("Enter two numbers").split()]
    c=a/b
    logging.info(c)
    print(c)
    f.write("The output is " + str(c)+"\n")
except ZeroDivisionError:
    print("Division by Zero not allowed")
    logging.error("Division by Zero not allowed")
else:
    print("Divided number is not zero")
finally:
    f.close()
print("code after the exception")


class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    pwd=input("Please enter a password: ")
    if len(pwd)<8:
        raise InvalidPasswordException("Password length must be greater than 7")
    else:
        print("Password has been successfully validated")
except InvalidPasswordException as obj:
    print(obj)



import os, sys

if os.path.isfile("test-1.txt"):
    f=open("test-1.txt","a")
else:
    sys.exit()
f.close

class Patient:
    def setPatientId(self,id):
        self.id=id

    def setPatientName(self,name):
        self.name=name

    def setPatientSSN(self,ssn):
        self.ssn=ssn

    def getPatientId(self):
        print(self.id)

    def getPatientName(self):
        return self.name

    def getPatientSSN(self):
        return self.ssn


import pickle
#from peter-practice-2 import Patient
f=open("test.dat","wb")
s=Patient()
s.setPatientName("Peter")
t=s.getPatientName()
pickle.dump(t,f)
f.close()


import pickle
f=open("test.dat","rb")
obj=pickle.load(f)
print(obj)


import re
str="take up one 1-2-2020 idea.One idea at a time 11/11/2013 onetake"
result=re.search(r'o\w\w',str)
print(result.group())

result=re.findall(r'o\w\w*',str)
print(result)


result=re.match(r't\w\w\w',str)
print(result.group())

result=re.split(r'\d+',str)
print(result)

result=re.sub(r'2020','2021',str)
print(type(result))
print(result)

result=re.findall(r'O\w{1,4}',str)
print(result)

result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

result=re.findall(r'\d{1,2}\/\d{1,2}\/\d{4}',str)
print(result)

result=re.search(r'^t\w',str)
print(result.group())


import time,datetime

epochseconds=time.time()
print(epochseconds)

t=time.ctime(epochseconds)
print(t)

dt=datetime.datetime.today()
print(dt)

print("current date is {}/{}/{}".format(dt.month,dt.day,dt.year))

from datetime import *
d=date(2018,7,21)
t=time(12,45)
dt=datetime.combine(d,t)
print(type(dt))
print(dt)


from datetime import date
import time

starttime=time.perf_counter()

ldates=[]
d1=date(2017,8,12)
d2=date(2017,7,12)
d3=date(2017,6,12)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort(reverse=True)
time.sleep(3)
for d in ldates:
    print(d)

endtime=time.perf_counter()

print("Execution time is ",endtime-starttime)


import threading

print(threading.current_thread().getName())

if threading.current_thread()==threading.main_thread:
    print("main thread")
else:
    print("other thread")


import threading
from threading import Thread

def displayNumbers():
    i=0
    print(threading.current_thread().getName())
    while (i<10):
        print(threading.current_thread().getName())
        print(i)
        i+=1

print(threading.current_thread().getName())
t=Thread(target=displayNumbers)
t.start()
print(threading.current_thread().getName())


from threading import *

class MyThread(Thread):
    def run(self):
        i=0
        while (i<10):
            print(i)
            i+=1

t=MyThread()
t.start()


from threading import *
from time import sleep

class MyThread:

    def displayNumbers(self):
        i=0
        print(current_thread().getName())
        sleep(3)
        while (i<=10):
            print(i)
            i+=1

obj=MyThread()
t=Thread(target=obj.displayNumbers)
t.start()

t2=Thread(target=obj.displayNumbers)
t2.start()

t3=Thread(target=obj.displayNumbers)
t3.start()

from threading import *

class BookMyBus:
    def __init__(self,availableSeats):
        self.availableSeats=availableSeats
        #self.l=Lock()
        self.l=Semaphore()


    def buy(self,seatsRequested):
        self.l.acquire()
        print(current_thread().getName())
        print("total seats available:",self.availableSeats)
        if (self.availableSeats>=seatsRequested):
            print("Confirming a seat")
            print("comfirming the payment")
            print("Printing the ticket")
            self.availableSeats-=seatsRequested
        else:
             print("No seat is available")
        self.l.release()


bmb=BookMyBus(10)
t1=Thread(target=bmb.buy,args=(3,))
t2=Thread(target=bmb.buy,args=(4,))
t3=Thread(target=bmb.buy,args=(9,))

t1.start()
t2.start()
t3.start()


from threading import  *
from time import *

class Producer:
    def __init__(self):
        self.products=[]
        #self.orderplaced=False
        self.c=Condition()

    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("Product"+str(i))
            sleep(1)
            print("Item Added")
        #self.orderplaced=True
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self,prod):
        self.prod=prod
    
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        #while self.prod.orderplaced==False:
        #    print("Waiting for the orders")
        #    sleep(0.2)
        print("Order Shipped ",self.prod.products)

p=Producer()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()

from threading import *
from time import *

class EvenNumbersThread:
    def __init__(self):
        self.c=Condition()

    def displayEvenNumber(self):
        self.c.acquire()
        print("Even Numbers thread:",current_thread().getName())
        for en in range(1,101):
            if en%2==0:
                print(en)
        self.c.notify()
        self.c.release()

class OddNumbersThread:
    def __init__(self,ent):
        self.ent=ent

    def displayOddNumber(self):
        self.ent.c.acquire()
        self.ent.c.wait(timeout=0)
        print("Odd Numbers thread:",current_thread().getName())
        for on in range(1,101):
            if on%2!=0:
                print(on)
        self.ent.c.notify()
        self.ent.c.release()


class AllNumbersThread:
    def __init__(self,ont):
        self.ont=ont

    def displayAllNumber(self):
        self.ont.ent.c.acquire()
        self.ont.ent.c.wait(timeout=0)
        print("All Numbers thread:",current_thread().getName())
        for an in range(1,101):
            print(an)
        self.ont.ent.c.notify()
        self.ont.ent.c.release()


ent=EvenNumbersThread()
ont=OddNumbersThread(ent)
ant=AllNumbersThread(ont)

entf=Thread(target=ent.displayEvenNumber)
ontf=Thread(target=ont.displayOddNumber)
antf=Thread(target=ant.displayAllNumber)

#main thread
print("All numbers main thread: ",current_thread().getName())
for an in range(1,101):
    print(an)

#other threads
entf.start()
ontf.start()
antf.start()



import urllib.request

try:
    url=urllib.request.urlopen("https://www.python.org")
    content=url.read()
    url.close()
except urllib.error.HTTPError:
    print("Webpage not found")
    exit()

print(content)


import urllib.request
url="image.png"
urllib.request.urlretrieve(url,"test.png")



import socket

host='localhost'
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)#no of connection
c,addr=s.accept()

filename=c.recv(1024)
try:
    f=open(filename,'rb')
    content=f.read()
    c.send(content)
    f.close
except FileMotFoundError:
    c.send(b"File does not exist")


print("Server listening on:",port)
print("connection from:",str(addr))

c.send(b"Hello, how are you")
c.send("bye",encode())
c.close()


import socket

s=socket.socket()

s.connect(("localhost",4000))
msg=s.recv(1024)

while msg:
    print("Received:",msg.decode())
    msg=s.recv(1024)
s.close()

import socket

s=socket.socket()

s.connect(("localhost",4000))
filename=input("Enter a filename: ")
s.send(filename.encode())
content=s.recv(1024)
print(content.decode())

s.close()



import smtplib
from email.mime.text import MIMEText

body="This is a test email"
msg=MIMEText(body)
msg['From']="peterkam78@gmail.com"
msg['To']="peterkam78@yahoo.com"
msg['Subject']="Test"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("peterkam78@gmail.com","p3t3rk@m78")
server.send(msg)
print("Mail Sent")
server.quit()


import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mysql',user='root',password='test1234')

if conn.is_connected():
    print("connected to mysql db")

cursor=conn.cursor()

cursor.execute("select * from emp")

row=cursor.fetchone()
rows=cursor.fetchall()

print("total rows:",cursor.rowcount())

while row is not None:
    print(row)
    row=cursor.fetchone()

for row in rows:
    print(row)

cursor.close()
conn.close()


import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mysql',user='root',password='test1234')

if conn.is_connected():
    print("connected to mysql db")

cursor=conn.cursor()

try:
    cursor.execute("insert into emp values(3,'Peter',30000)")
    conn.commit()
    print("Employee added")
except:
    conn.rollback()

cursor.close()
conn.close()

"""

import mysql.connector

conn=mysql.connector.connect(host='localhost',database='mysql',user='root',password='test1234')

def delete(id):
    if conn.is_connected():
        print("connected to mysql db")
        cursor=conn.cursor()
        delquery="delete from emp where id='%d'"
        args=(id)
        try:
            cursor.execute(delquery % args)
            conn.commit()
            print("Employee deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empid=input("Enter employeeid to delete: ")
delete(empid)






























































































    
































