#1. Write a Python program to read an entire text file.
# file=open("mayuri.txt",'w')
# data ="i am mayuri"
# file.write(data)
# file.close()
# A=open("mayuri.txt",'r')
# data = A.read()
# print(data)
# A.close()

#2. Write a Python program to read first n lines of a file.
# n=int(input("enter a number"))
# for i in range(n):
#     with open ("mayuri.txt" ,"r") as file :
#         b=file.readlines()
#         print(b)


    
#3. Write a Python program to append text to a file and display the text.

# with open ("mayuri.txt ", "a") as file:
#     file.write("i am mayuri\n")
#     file.write("i am learning python\n")
#     file.write("i am enjoying it\n")
# with open ("mayuri.txt ", "r") as file:
#     n=3
#     for i in range(n):
#         line = file.readline()
#         print(line.strip())


#4. Write a Python program to read last n lines of a file.

# n=int(input("enter alast line number"))
# with open ("mayuri.txt ", "r") as file:
#     b=file.readlines()
#     print(b)
# for i in b [-n:1]:
#     print(b , end ="")

      
# #5. Write a Python program to read a file line by line and store it into a list.
# a=[]
# with open ("mayuri.txt ", "r") as file:
#     for i in file:a.append(i.strip())   
#     print(a)


 
                  
# #6. Write a Python program to read a file line by line store it into a variable.
# with open ("mayuri.txt ", "r") as file:
#     for i in file:
#         print(i)


# #7. Write a python program to find the longest words.

# word = input("enter a required string")
# a= word.split()
# print(a)
# long_w =[]
# for i in a :
#     for j in a:
#         if len(i)>len(j):
#             print("sucessfully")
# print("longest word is ",i)
# long_w.append(i)
# print(long_w)
    #print(i)
    # b=(len(i))
    # print(b)
    # print(list(b))
    # if len(i) > len(long_w):
    #     i== long_w
    #     print(i)
    

 





#8. Write a Python program to count the number of lines in a text file.


# with open ("xyz.txt",'w') as f:
#     f.write("hi")
#     f.write("/n hello")
#     f.write("/n godd")
# f=open ("xyz.txt" ,'r') 
# # a=f.read()
# # print(a)
# c=0
# for i in f:
#     c+=1
# print(c) 

#9. Write a Python program to count the frequency of words in a file.
# with open ("mayuri.txt ",'w') as f:
#     f.write("hi i am mayuri")
#     f.write("\n hi i am learning python")
#     f.write("\n hi i am enjoying it")
# with open ("mayuri.txt ",'r') as f:
#     a=f.read()
#     print(a)
# print(a.split())

# word_freq={}
# for word in a.split():
#     if word in word_freq:
#         word_freq[word] +=1
#     else:
        


#         word_freq[word] =1

#print(word_freq)

#10. Write a Python program to get the file size of a plain file.
# with open ("mayuri.txt ",'r') as f:
#     a=f.read()
#     print(len(a))

#11. Write a Python program to write a list to a file.
# my_list = ["apple", "banana", "cherry"]
# with open("my_list.txt", "w") as file:
#     file.writelines(my_list)
# with open("my_list.txt", "r") as file:
#     print(file.read())



# #12. Write a Python program to copy the contents of a file to another file .

# with open ("mayuri.txt" ,'r') as f:
#     l=[]
#     #p= open ("maya.txt" ,'w') 
#     for i in f:
#        l.append(i)
#     print(l)
# with open ("mayu.txt" ,'w') as p:
#     p.writelines(l)
# with open ("mayu.txt" ,'r') as p:
#     p.read()
# p= open ("maya.txt" ,'w')
# with open ("mayuri.txt" ,'r') as f:
    
#     for i in f :
#         print(i)
#         p.write(i)
# with open ("maya.txt" ,'r') as p:
#     data=p.read()
#     print(data)



        

        

# #13. Write a Python program to read a random line from a file.

# n=int(input("enter a no of line"))
# with open ("maya.txt" ,'r') as p:
#     h=p.read(n)
#     print(h)

# import random 


# with open ("maya.txt" ,'r') as p:
#     h=p.readlines()
#     a=random.choice(h)
#     print(a)






# 14. Write a Python program to assess if a file is closed or not.
# with open ("mayuri.txt ",'r') as f:
#     a=f.read()
#     print(a)
#     print(f.closed)
# f.write("hi i am mayuri")


 #15.Write a Python program that takes a text file as input and returns the number of words of a 
 #given text file.
# n=input("enter a required file name")
# print(n)
# p={}
# with open (n,"r") as f :
#     h=f.read()
#     c=0
#     print(h.split())
#     for i in (h.split()):
#         if i in p:
#             p[i]+=1
#         else:
#             p[i]=1
# print(p)
