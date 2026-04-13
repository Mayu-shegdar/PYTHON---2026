#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


# try:
#     num1=float(input("enter a number"))
#     num2=float(input("enter a number"))
#     result =num1/num2
# except ZeroDivisionError:
#     print("num2is not 0")

# num1=float(input("enter a number"))
# num2=float(input("enter a number"))

# if num2==0:
#     raise ZeroDivisionError ("num2 is not zero")
# else:
#     result=num1/num2
#     print(result)



#2. Write a Python program that prompts the user to input an integer and raises 
# a ValueError exception if the input is not a valid integer.
# try:
#     a=int(input("enter a number"))
#     b= int(input("enter a number"))
#     result = a+b
# except ValueError:
#     print("only numbers are allowed ")

# a=input("enter a number")
# b=input("enter a number")
# if a ==" " :
#     raise ValueError("a and b is not empty")
# else:
#     a=float(a)
#     b=float(b )





#3. Write a Python program that opens a file and handles a FileNotFoundError exception
#  if the file does not exist.
# try:
#     file= open ("mayuri.txt",'r')
#     data = file.read()
# except FileNotFoundError:
#     print("file not found")



#4. Write a Python program that prompts the user to input two numbers and 
# raises a TypeError exception if the inputs are not numerical.
# try:
#     a=input("enter a number")
#     b=input("enter a number")
#     result= a-b
#     print(result)
# except TypeError:
#     print("a nd b is only number" )


# a=input("enter a number")
# b=input("enter a number")
# if a and b ==" ":
#     print("a and b is not empty")
# else:
#     a=int(a)
#     b=int(b)
#     print(a+b)
    

#5. Write a Python program that opens a file and handles a PermissionError exception if there 
# is a permission issue.

# try:
#     file_a= open ("mayurii.txt",'w')
#     file_a.write("hi i am mayuri")
#     file_a.close()
#     file_b = open("sharvi.txt","w")
#     file_b.write("hi i am sharvi") 
#     file_b.close()   
#     x=input("enter a first user name")
#     y= input("enter a second user")
#     d={x:file_a,y:file_b}
#     req_user = input("enter username")
#     req_files = input("the file which required")
#     if d[req_user]!=req_files:
#         raise PermissionError("you dont have permission to access this file")
#     else:
#         print("Accessed sucessfully")
# except PermissionError:
#     print("permission denied")
# except  :
#     print("please check inputs")

# #     #6. Write a Python program that executes an operation on a list and handles an IndexError 
# exception if the index is out of range
# try:
#     n= int(input ("enter a index"))
#     list =[1,2,3,4,5]
#     a=list[n]
#     print(a)
# except IndexError:
#     print("index is out of range")


#     #7. Write a Python program that executes division and handles an ArithmeticError exception 
# if there is an arithmetic error.
# try:

#     num1=float(input("enter a number"))
#     num2=float(input("enter a number"))
#     result =num1/num2
# except ArithmeticError:
#     print("num2is not 0")

# num1=float(input("enter a number"))
# num2=float(input("enter a number"))

# if num2==0:
#     raise ArithmeticError ("num2 is not  a zero")
# else:
#     result=num1/num2
#     print(result)