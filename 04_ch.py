# creat dictionary:
mydict = {
    "fast" : "rapid, quickly, run-fast, move-on",
    "cars" : "tasla, odey, lamburginy, farari",
    "money" : [202, 45, 8, 38],
    "anotherdict" : {'fast' : 'doller states'},
    1:6
}
print(mydict.keys())
print(mydict.values())
updatemydict={
    'talha':'roha',
    'qasim':'alina',
    'cars':'Only fantastic car in pakistan is honda civic'
}
mydict.update(updatemydict)
print(updatemydict)
print(mydict.get['cars'])

b={1,2,3,5,5,5,8,5,930}
c={5,4,3,8,1,87,56}
b.add(10)
b.add(11)
b.add(983)
print(b)
b.remove(3,2)
b.pop()

print(b.clear())
print(b,c.union('comman value'))
print(b,c.intersection())
# create dictionary of urdu wards:
urdudict={
    'panka':'fan',
    'gari':'car',
    'gar':'house',
    'kilona':{'toys':'for child'},
    'panj':'five',
    'shat':'roof'
}
print(urdudict.keys())
a=input('Enter the urdu words\n ' )
print('Your word meaning is:', urdudict[a])
print('Your word meaning is', urdudict.get(a))
# create the unique set:
num1=int(input("Enter the your number1\n"))
num2=int(input("Enter the your number2\n"))
num3=int(input("Enter the your number3\n"))
num4=int(input("Enter the your number4\n"))
num5=int(input("Enter the your number5\n"))
num6=int(input("Enter the your number6\n"))
num7=int(input("Enter the your number7\n"))
num8=int(input("Enter the your number8\n"))
a={num1,num2,num3,num4,num5,num6,num7,num8}
print(a)
# print int and str both as possible in set:
d=18, '18'
print(d)
# length of the set some of the possiblities write within the only unqiue no.:
s=set()
s.add(23)
s.add(23.0)
s.add('23')
print(s)
# create the empty dictionary:
favlang={}
n=input("Enter the favourit language\n")
o=input("Enter the favourit language\n")
l=input("Enter the favourit language\n")
m=input("Enter the favourit language\n") 
favlang['roha']=n
favlang['talha']=o
favlang['hafsa']=l
favlang['zain']=m
print(favlang)
# what is possible set inside the create list:
q={8,7,2,'talha',[3,2]}
print(q)