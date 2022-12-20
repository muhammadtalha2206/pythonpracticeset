 

# open('poem','w'):
# f.write('Talha loves the Roha. But roha no link to talha.')    
# f.close()

# f=open('poem', 'w')
# f.write("Twinkle twinkle little star.\n")
# f.write('Talha loves the Roha. But roha no link to talha.\n') 
# f.write("i have the get 345 rupees in one miniut that a cool thing in your life.")
# f.close()

# v=open("poem")
# n=v.read()
# print(n)
# v.close()

# p=open("text","w")
# p.write("Twinkle Twinkle little star.\n How are wander what you are.")
# p.close()

# c=open("text")
# z=c.read()
# if "Twinkle" in z:
#     print("Presnt in file ")
# else:
#     print("Presnt in not file")
# c.close()


# def game():
#     return 404

# score= game()
# with open("hiscore") as f:
#     hiscoreStr=f.read()
# if hiscoreStr=='':
#     with open("hiscore", "w") as f:
#         f.write(str(score))
# elif int(hiscoreStr)<score:
#     with open("hiscore", "w") as f:
#         f.write(str(score))

# for i in range(2, 21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i}*{j}={i*j}\n")
#             if j!=10:
#                 f.write("\n") 
#     
 
# with open("sample.txt") as f:
#     contant=f.read()
# content=contant.replace("fuck","$%^@$^#")
# with open("sample.txt","w") as f:
#     f.write(content)

# words=['donkey', 'kadu', 'fuck']
# with open("sample.txt") as f:
#     contant=f.read()
# for word in words:
#     contant=contant.replace(word,"$%^@$^#")
#     with open("sample.txt","w") as f:
#         f.write(contant)

# with open("log_file.txt") as f:
#     content=f.read()
# if "python" in content.lower():
#     print("python is present in file.")
# else:
#     print("Is not present in file.")

# with open("log_file.txt") as f:
#     content=f.read()
# if "python" in content.lower():
#     print("python is present in file.")
# else:
#     print("Is not present in file.")
    
from re import T


# contant=True
# i=1
# with open("log_file.txt") as f:
#     while contant:
#         content=f.readline()
#         if "python" in content.lower():
#             print(contant)
#             print(f"python is present in file on line {i}.")
#         i+=1
    
# with open("text") as f:
#     contant=f.read()
# with open("copy.txt","w") as f:
#     f.write(contant)

# files1="copy.txt"
# files2="text"
# with open(files1) as f:
#     f1=f.read()
# with open(files2) as f:
#     f2=f.read()
# if f1==f2:
#     print("Files are identical.")
# else:
#     print("Files are not identical.")
    
# filename="poem"
# with open(filename,"w") as f:
#     f.write("")
import os
oldfile="poem"
newfile="Twinkle.txt"
with open(oldfile) as f:
    contant=f.read()
with open(newfile, "w") as f:
    f.write(contant)
os.remove(oldfile)

    



