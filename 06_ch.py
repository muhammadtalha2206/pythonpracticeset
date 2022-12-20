# b=['mangoes','banana','apple','grapes','peach']
# i=0
# while i<len(b):
#     print('Roha understand '+b[i])
#     i=i+1
# Practice set:
# num=(int(input('Enter the number.')))
# for i in range(1, 11):
#     print(str(num) + "X" + str(i) + "=" + str(i*num))
#     print(f"{num}X{i}={num*i}")
# l1=['roha','rohan','talha','zain','manan','wise']
# for name in l1:
#     if name.startswith('r'):
#         print('Hello'+name)
# num=int(input('Enter the number.'))
# i=0
# while i<10:
#     i=i+1
#     print(num*i)    
# num=int(input('Enter the number.\n'))
# prime=True
# for i in range(2,num):
#     if(num%i==0):
#         prime=False
#         break
# if prime:
#     print('This number is prime.')    
# else:
#     print('This number is not prime.')



# num=int(input('Enter the number.\n'))
# factorial=1
# for i in range(1, num+1):
#     factorial=factorial*i
#     print(f"This number {num} is factorial {factorial}")
# num=int(input('Enter the number.\n'))
# sum=0
# for i in range(1, num+1):
#     sum=sum+i
#     print(f"This number {num} is sum {sum}")
# a=4
# for i in range(4):
#     print("*" * (i+1))
# n=4
# for i in range(4):
#     print(' '*(n-i-1),end='')
#     print('*'*(2*i+1),end='')
#     print(' '*(n-i-1),end='')
#     print(' '*(n-i-1))
# table=int(input('Enter the number. '))
# limit=int(input('Enter the encoding. '))
# for i in range(limit, 0, -1):
#     print(str(i) + 'X' + str(table) + '=' + str(table * i))
num = int(input("Enter a number: "))
sum=0
while(num > 0):
   sum += num
   num -= 1
   print("The result is", sum)
if num < 0:
   print("Please enter a positive number")
else:
   sum = 0
