# def percentage(marks):
#     return(sum(marks)/400)*100
# marks=[66,87,45,39]
# percentage1=percentage(marks)

# marks=[66,87,85,79]
# percentage2=percentage(marks)
# print(percentage1,percentage2)

# def greet(name):
#     print("Good Day "+name)
# greet("Roha")
# def mysum(num1, num2):
#     return num1 + num2
# a=mysum(67, 3)
# print(a)
# def greet(name='Talha'):
#     print("Good Day "+name)
# greet("Roha")
# greet()
# n=5
# product=1
# for i in range(n):
#     product=product*(i+1)
#     i==16
# print(product)



# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product * (i+1)
#     return product
# def factorial_recursion(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial_recursion(n-1)
# a=factorial_iter(6)
# b=factorial_recursion(6)
# print(a)
# print(b)

# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3
# a=maximum(34,25,28)
# print(a)

# def farh(cel):
#     return (cel*(9/5)+32)
# cel=0
# f=farh(cel)
# print(f)
# print('Roha', end= ' ')
# print('Talha', end= ' ')
# print('loves', end= ' ')
# print('them', end= ' ')

# def natural_iter(n):
#     sum=1
#     for i in range(n):
#         sum=sum + i
#     return sum
# def natural_recursion(n):
#     if n==1 or n==0:
#         return 1
#     return n+natural_recursion(n-1)
# a=natural_iter(6)
# b=natural_recursion(6)
# print(a)
# print(b)
# Python program to find the sum of natural using recursive function

# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)

# # change this value for a different result
# num = 6

# if num < 0:
#    print("Enter a positive number")
# else:
#    print("The sum is",recur_sum(num))
# n=6
# for i in range(n):
#     print("*" * (n-i))

# def inch_to_cm(inch):
#     return inch * 2.54


# inch_value = int(input('Enter the value in inch: '))

# print('{}″ = {}cm'.format(inch_value, inch_to_cm(inch_value)))

def remove_and_split(string, word):
    newstr=string.replace(word,"")
    return newstr.strip()
this="      Roha loves me       "
a=remove_and_split(this,'me')
print(a)



