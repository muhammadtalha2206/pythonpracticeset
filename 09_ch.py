
class Number:
    def sum(self):
        return self.a + self.b
num=Number()
num.a=34
num.b=65
s=num.sum()
print(s)

class RailwayForm:
    applicationForm="Railway"
    def data(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Seat is {self.seat}")
railwayApplication=RailwayForm()
railwayApplication.name="Maqsood"
railwayApplication.train="Pakistan Express"
railwayApplication.seat="80"
railwayApplication.data()

class remote:
    pass
class player:
    def moveright():
        pass
    def leftright():
        pass
    def topright():
        pass
remote1=remote()
player1=player()
if(player1.isrightPressed):
    player1.moveright()

class Employee:
    company= "Google"
Zain=Employee()
Ali=Employee()
Zain.Salary="300"
Ali.salary="450"
Employee.company="Insta"
print(Zain.company)
print(Zain.Salary)
print(Ali.company)
print(Ali.salary)

class Employee:
    company="Rabic"
    def getSalery(self):
        print(f"That's Company name is {self.company} and Salery {self.salery}.")
zain=Employee()
zain.salery=100000
zain.getSalery()

class Employee:
    company="Rabic"
    def getSalery(self,signature):
        print(f"That's Company name is {self.company} and Salery {self.salery}.\n{signature}")
    @staticmethod
    def greet(): # if "self" write then no @staticmethode.
        print("Hy Sir, Good Morning.")
zain=Employee()
zain.salery=100000 
zain.greet()
zain.getSalery("Thanks!")  # Employee.getSalery(zain)

class Employee:
    company="Rabic"
    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Rabic is a new company.And interduced whole our the world.")
    def getDetail(self):
        print(f"The employee name is {self.name}.")
        print(f"The monthly salary is {self.salary}.")
        print(f"The subunit name is {self.subunit}.")
    def getSalery(self,signature):
        print(f"That's Company name is {self.company} and Salery {self.salery}.\n{signature}")
    @staticmethod
    def greet(): # if "self" write then no @staticmethode.
        print("Hy Sir, Good Morning.")
    @staticmethod
    def time():
        print("On this time is 9:00 A.M .")
zain=Employee("Ali", "300k", "Google Colab")
zain.getDetail()

class Programmer:
    company="Microsoft"
    def __init__(self, name, product):
        self.name=name
        self.product=product
        
    def info(self):
        print(f"The name of company is {self.company} employee name is {self.name} and product of the company {self.product}.")
zain=Programmer("zain", "Excel")
ali=Programmer("ali", "Github")
zain.info()
ali.info()




class Calculater:
    def __init__(self, number):
        self.number=number
    def square(self):
        print(f"This value of square is {self.number**2}.")
    def squareroot(self):
        print(f"This value of squareroot is {self.number**1/2}.")
    def cube(self):
        print(f"This value of cube is {self.number**3}.")
a=Calculater(4)
a.square()  
a.squareroot() 
a.cube()  

class sample:
    a='burrak'
obj=sample()
obj.a='bamsi'
print(sample.a)
print(obj.a)

class Calculater:
    def __init__(self, number):
        self.number=number
    def square(self):
        print(f"This value of square is {self.number**2}.")
    def squareroot(self):
        print(f"This value of squareroot is {self.number**1/2}.")
    def cube(self):
        print(f"This value of cube is {self.number**3}.")
    @staticmethod    
    def greet():
        print("Hello, this calculater is very nice!")
a=Calculater(4)
a.square()  
a.squareroot() 
a.cube()  
a.greet()

class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getstates(self):
        print(f"The train name is {self.name} and the seats no. is {self.seats}.")
    def getinfo(self):
        print(f"The ticket price is {self.fare}.")
    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket is conform! and your seat no. is {self.seats}.")
            self.seats=self.seats-1
        else:
            print("Sorry! all seats have already book! Try to another train.")
intercity=Train('Pakistan Express', 900, 360)
intercity.getstates()
intercity.getinfo()
intercity.bookTicket()
        