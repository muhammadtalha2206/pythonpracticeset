# class Employee:
#     company="Google"
#     def getDetails(self):
#         print("This is the company of employee.")
# class programmer(Employee):
#     language="python"
#     company="Youtube"
#     def getinfo(self):
#         print(f"This is use the language {self.language}.")
#     def showDetails(self):
#         print("That's a programmer.")
# a=Employee()
# a.getDetails()
# b=programmer()
# b.getinfo()
# b.showDetails()
# b.getDetails()

# class Employee:
#     company="visa"
#     eCode=120
# class Freelancer:
#     company="Fiverr"
#     level=0
#     def upgrateLaval(self):
#         self.level=self.level+1
#         print(f"Congrajulation! Upgrade your laval {self.level}.")
# class Programmer(Employee, Freelancer):
#     worker="umar"

# p=Programmer()
# print(p.worker)
# print(p.company)
# print(p.company)
# p.upgrateLaval()



# class Person:
#     country="Pakistan"
#     def takeBreat(self):
#         print(f"Its a very beautiful country {self.country}.")
# class Employee(Person):
#     company="Honda"
#     salary=300000
#     def takeBreat(self):
#         print(f"I am employee of {self.company} and my montly salary is {self.salary}.")
# class Programmer(Employee):
#     name="Shadab"
#     company="Fiverr"
#     def takeBreat(self):
#         print(f"{self.name} is my name and i am worker of {self.company}.")
# p=Person()
# p.takeBreat()
# e=Employee()
# e.takeBreat()
# pr=Programmer()
# pr.takeBreat()

# class Person:
#     country="Pakistan"
#     def __init__(self):
#         print("Initialize person ......\n")
#     def takeBreat(self):
#         print(f"Its a very beautiful country {self.country}.")
# class Employee(Person):
#     company="Honda"
#     salary=300000
#     def __init__(self):
#         print("Initialize employee ......\n")
#     def getSalery(self):
#         print(f"I am employee of {self.company} and my montly salary is {self.salary}.")
#     def takeBreat(self):
#         print("Program was complete and lukily run.")
# class Programmer(Employee):
#     name="Shadab"
#     company="Fiverr"
#     def takeBreat(self):
#         super().takeBreat()
#         print(f"{self.name} is my name and i am worker of {self.company}.")
# p=Person()
# p.takeBreat()
# e=Employee()

# pr=Programmer()
# pr.takeBreat()

# class Employee:
#     company="Multan Gas"
#     salery=5000
#     saleryBones=50
#     @property
#     def totalSalery(self):
#         return self.salery+self.saleryBones
#     @totalSalery.setter
#     def totalSalery(self, sel):
#         self.saleryBones=sel-self.salery 
# e=Employee()
# print(e.totalSalery)
# e.totalSalery=5050
# print(e.salery)
# print(e.saleryBones)

# class Number:
#     def __init__(self, num):
#         self.num=num
    
#     def __sum__(self, num2):
#         self.num2=num2
#         return f"Let's add {self.num}+{self.num2}"
        
#     def __mul__(self, num2):
#         self.num2=num2
#         return f"Let's multiply {self.num}*{self.num2}"    

# n1=45
# n2=4
# sum=n1+n2
# print(sum)
# mul=n1*n2
# print(mul)




# class Number:
#     def __init__(self, num):
#         self.num=num
    
#     def __sum__(self, num2):
#         self.num2=num2
#         return f"Let's add: {self.num}+{self.num2}"
        
#     def __mul__(self, num2):
#         self.num2=num2
#         return f"Let's multiply: {self.num}*{self.num2}"
#     def __str__(self):
#         return f"Decimal no :{self.num}"
#     def __len__(self):
#         return 1
# n=Number(9)
# print(n)
# print(len(n))
# n1=20
# n2=2
# sum=n1+n2
# print(sum)
# mul=n1*n2
# print(mul)

# class C2dvec:
#     def __init__(self, i, j):
#         self.icap=i
#         self.jcap=j
    
#     def __str__(self):
#         return f"{self.icap}i {self.jcap}j"
    
# class C3dvec(C2dvec):    
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap=k
    
#     def __str__(self):
#         return f"{self.icap}i {self.jcap}j {self.kcap}k"
# v2d=C2dvec(5, -4)
# v3d=C3dvec(7, 7, -2)
# print(v2d)
# print(v3d)

# class Animals:
#     animalsType="camal"

# class Pet:
#     colour="Yellow"

# class Dog:
#     @staticmethod
#     def bark():
#         print("Baw Baw!")
# d=Dog()
# d.bark()

# class Employee:
#     salery=1000
#     increment=1.5
#     @property
#     def saleryAfterIncrement(self):
#         return self.salery*self .increment
#     @saleryAfterIncrement.setter
#     def saleryAfterIncrement(self, sai):
#         self.increment=sai/self.salery
# e=Employee()
# print(e.saleryAfterIncrement)

# print(e.increment)
# e.saleryAfterIncrement=2000
# print(e.increment)

# class complex:
#     def __init__(self, r, i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, c):
#         return complex(self.real+c.real, self.imaginary+c.imaginary)
#     def __mul__(self, c):
#         mulReal=self.real*c.real-self.imaginary*c.imaginary
#         mulImaginary=self.real*c.imaginary+self.imaginary*c.real
#         return complex(mulReal, mulImaginary)
#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} -{-self.imaginary}i"
#         else:
#             return f"{self.real} {self.imaginary}i"
# c1=complex(1, -4)
# c2=complex(331, -37)
# print(c1 + c2)
# print(c1 * c2)


# class Vector:
#     def __init__(self, vec):
#         self.vec=vec
   
#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1+= f"{i}a{index} "
#             index+=1
#         return str1[:-1]
    
#     def __add__(self, vec2):
#         newList=[]
#         for i in range(len(self.vec)):
#             newList.append( self.vec[i] * vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         sum=0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

# v1=Vector([1, 4])
# v2=Vector([1, 6])
# print(v1)
# print(v1+v2)
# print(v1*v2)


# class Vector:
#     def __init__(self, vec):
#         self.vec=vec
   
#     def __str__(self):
#         return f"{self.vec[0]}i {self.vec[1]}j {self.vec[2]}k"

# v1=Vector([1, 5, 9])
# v2=Vector([1, 6, 7])
# print(v1)
# print(v2)

# class Vector:
#     def __init__(self, vec):
#         self.vec=vec
   
#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1+= f"{i}a{index} "
#             index+=1
#         return str1[:-1]
    
#     def __add__(self, vec2):
#         newList=[]
#         for i in range(len(self.vec)):
#             newList.append( self.vec[i] * vec2.vec[i])
#         return Vector(newList)

#     def __len__(self):
#         return 
#     def __mul__(self, vec2):
#         sum=0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

#     def __len__(self):
#         return len(self.vec)

# v1=Vector([1, 4])
# v2=Vector([1, 6])
# print(len(v1))
# print(v1+v2)
# print(v1*v2)

