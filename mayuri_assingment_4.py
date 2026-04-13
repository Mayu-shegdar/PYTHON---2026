# 1. Write a Python function to find the maximum of three numbers.

# num1 = int(input("enter a first number"))
# num2 = int(input("enter a first number"))
# num3 = int(input("enter a first number"))
# l=[num1,num2,num3]


# def max_num (l):
#     b=max(l)
#     return b 
# print(max_num(l))
    
# 2. Write a Python function to sum all the numbers in a list.

# 	Sample List : (8, 2, 3, 0, 7)
# 	Expected Output : 20
# List = [8, 2, 3, 0, 7]
# def sum_list (List) :
#     sum=0
#     for i in List:
#         sum+=i
#     return(sum)
# b= sum_list(List)
# print(b)




	
# 3. Write a Python function to multiply all the numbers in a list.

# 	Sample List : (8, 2, 3, -1, 7)
# 	Expected Output : -336

# List = [8, 2, 3, -1, 7]
# def product_list (List) :
#     product_list=1
#     for i in List:
#         product_list*=i
#     return(product_list)
# b= product_list(List)
# print(b)


	
# 4. Write a Python function to reverse a string. 

# Sample_String = "1234abcd"
# # 	Expected Output : "dcba4321"
# def reverse1 (sample_string):
#     return (sample_string[ : :-1])
# print(reverse1(Sample_String))
	
# 5. Write a Python function to check whether a number falls within a given range.
# a= int(input(" enter range starting point "))
# b= int(input(" enter range ending  point "))

# num =int(input("enter a number"))


# def check (num):
#     if a<=num<=b :
#         print("num is in range a to b")
#     else:
#         print("not fallen") 
#     return("done sucessfully")

# print(check(num))




# 6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# 	Sample String : 'The quick Brow Fox'
# 	Expected Output :
# 	No. of Upper case characters : 3
# 	No. of Lower case Characters : 12

# p= 'The quick Brow Fox'
# def case_check(p):
#     cl=0
#     cu=0
#     for i in p:
#         if "a"<=i<="z":
#             cl+=1
#             print("total of lower case ", cl)
#         elif "A"<=i<="Z":
#             cu+=1
#             print("total of upper case ", cu)
            
#         else:
#             print("please check")
#     return(cl,cu)


# print(case_check(p))

            
	
# # 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# # 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]
# l= [1,2,3,3,3,3,4,5]
# def unique_list (l):
#     p=[]
#     for i in l :
#         if i not in p:
#             p.append(i)
#     return(p)
# print(unique_list(l))
            
# 8. Write a Python function that checks whether a passed string is a palindrome or not.
# n=input("enter a string")
# def check_palindrome (n):
#     if ( n[ : :-1] == n) :
#         print("n is palindrome")
#     else:
#         print("n is not palindrome")
#     return("successfully executed")
# print(check_palindrome(n))
        

# 	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
	
# 9. Write a Python program that accepts a hyphen-separated sequence of words as
#  input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# 	Sample Items : green-red-yellow-black-white
# 	Expected Result : black-green-red-white-yellow

s = "green-red-yellow-black-white"
# for i in s:
#print(s.split("-"))
# def sort1 (s) :
# 	b=s.split("-")
# 	c=sorted(b)
# 	for i in c :
# 		print(i ,end ="-")
# 	return("done")
# print(sort1(s))


 #10. Write a Python program to detect the number of local variables declared in a function.
# def local_var():
# 	a=10
# 	b=20
# 	c=30
# 	d=40
# 	e=50
# 	print(locals())
# 	return(len(locals()))

# print(local_var())

# 11. Write a Python program to create a lambda function that adds 15 to a given number passed
#  in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

# 	Sample Output:
# 	25
# 	48

# num =int(input("enter a number"))
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# def check(num ,x,y):
# 	add= lambda num: 15 + num 
# 	print(add(num))
# 	products = lambda x,y : x*y
# 	print (products(x,y))
# 	return	("done")
# print(check(num,x,y))



#  12. Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.

# 	Sample Output:
#  	Double the number of 15 = 30
#  	Triple the number of 15 = 45
# 	Quadruple the number of 15 = 60
# 	Quintuple the number 15 = 75

# num =int(input("enter a number"))
# def check_num (num):
#     for i in range(1,11):
#         b= num*i
#         print(b)
#         print(f"{i} times of {num} is {b} ")
# print(check_num(num))
    
	
# 13. Write a Python program to sort a list of tuples using Lambda.

# 	Original list of tuples:
# 	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# 	Sorting the List of Tuples:
# 	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# l= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# c= sorted(l)
# b= sorted(l, key=lambda x: x[1])
# print(c)

# 14. Write a Python program to sort a list of dictionaries using Lambda.

# 	Original list of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# 	Sorting the List of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
l=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
   {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
   {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# b= sorted (l, key = lambda x : x["model"])
# 

# for i in l:
# 	#print(i)
# 	for j in i :
# 		#print(j)
# 		print(i.get("model"))



    
    

#     p=i.get("model")
#     print(c.append (p))
# print(c)
# p = sorted(c)

# print(p )
# h=  sorted(l)






# 15. Write a Python program to filter a list of integers using Lambda.

# 	Original list of integers:
# 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	Even numbers from the said list:
# 	[2, 4, 6, 8, 10]
# 	Odd numbers from the said list:
# 	[1, 3, 5, 7, 9]	

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #p=[lambda x :"even" if x %2 ==0 else "odd" ]
# even =[]
# odd =[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(l)
# print(even)
# print(odd)
#print(p(l))	



# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.

# 	Original list of integers:
# 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	Square every number of the said list:
# 	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 	Cube every number of the said list:
# 	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# l1 = [(lambda x : x*x )(x) for x in l]
# print(l1)
# l2 = [(lambda x : x*x*x ) (x)for x in l]
# print(l2)
#def square_of (l1,l):
    
	
# 18. Write a Python program to find if a given string starts with a given character using Lambda.
# n=input("enter a string ")
# b=input("enter a letter to which its start" )
# print(n.startswith(b))

# 19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

# 	Original arrays:
# 	[-1, 2, -3, 5, 7, 8, 9, -10]
# 	Rearrange positive and negative numbers of the said array:
# 	[2, 5, 7, 8, 9, -10, -3, -1]

# list = [-1, 2, -3, 5, 7, 8, 9, -10]
# b= sorted (list , reverse = True)
# print(b)
	
# 20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

# 	Original arrays:
# 	[1, 2, 3, 5, 7, 8, 9, 10]
# 	Number of even numbers in the above array: 3

# 	Number of odd numbers in the above array: 5

# list_1 =[1, 2, 3, 5, 7, 8, 9, 10]
# ce=0
# co=0
# for i in list_1 :
#     if i %2==0:
#         ce+=1
#     else:
#         co+=1
# print("even number count is ",ce)
# print("even number count is ",co)


    
	
# 21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

# 	Orginal list:
# 	19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# 	Numbers of the above list divisible by nineteen or thirteen:
# 	[19, 65, 57, 39, 152, 190]
# p=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# t=[]
# for i in p :
#     if i%19 ==0 or i%13==0 :
#         print(t.append(i))
#     print(t)
	
# 22. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
	
# n=input("enter a string")
# def check_string (n):
#     if "a"<=n<="z" :
#         print("lower case")
#     elif "A"<=n<="Z" :
#         print("upper case")
#     elif "1"<=n<="10000000" :
#         print("contain numbers")
#     return(len(n))
# print(check_string(n))
    
        


