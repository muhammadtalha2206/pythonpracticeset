# # def func(a):
# #     return a+5
# func=lambda a: a+5
# square=lambda x:x*x
# sum=lambda a,b,c: a+b+c
# x=6
# print(func(x))
# print(square(x))
# print(sum(x, 6, 1))

# l=['camera','ipad','phone','laptop','Nvidia 3080 carde']
# d=" or ".join(l)
# print(d)

# name='hafsa'
# company='linked'
# a="This is {} and the employee of {}. ".format(name, company)
# print(a)

# def square(num):
#     return num*num
# l=[1,2,3]
# # method 1
# l2=[]
# for item in l:
#     l2.append(square(item))
# print(l2)
# # Method 2
# print(list(map(square, l)))

# def grater_then_5(num):
#     if num>5:
#         return True
#     else:
#         return False
# l=[2,3,4,1,67,54,14,22]
# print(list(filter(grater_then_5, l)))

from functools import reduce
l=[1,2,3,4]
sum=lambda a,b : a+b
print(reduce(sum, l))
