# 1. Write a Python program to create a class representing a Circle. Include methods to 
# calculate its area and perimeter.

# class Circle :
#     def __init__(self,radius):
#         self.radius = radius 
#     def area (self):
        
#         return(3.14*self.radius*self.radius)
    
#     def perimeter (self):
#         return(2*3.14*self.radius)
# c= Circle(5)
# print(c.area())
# print(c.perimeter())



# 2. Write a Python program to create a person class. Include attributes like name, country and 
# date of birth. Implement a method to determine the person's age.
#from datetime import date 
# class Person :
#     def __init__(self,name,country ,dob):
#         self.name = name 
#         self.country = country 
#         self.dob = dob
#     def age_calculator (self):
#         n= date.today()
#         print(n)
        #   age = today.year - self.dob.year
#         return(age)
        
# p1 =Person("mayu", "india",1998-11-23)
# print(p1.age_calculator())
    
# from datetime import date 
# n= date.today()
# print(n)







# 3. Write a Python program to create a calculator class. 
# Include methods for basic arithmetic operations.

# a= float(input("enter a number"))
# b= float(input("enter a number"))
# try:
# 	class Calculator:
# 		def __init__(self,a,b):
# 			self.a = a 
# 			self.b = b 
# 		def add(self):
# 			s= a+b
# 			print(s)
# 		def sub(self):
# 			m= a-b
# 			print(m)
# 		def product(self):
# 			p= a*b
# 			print(p)
# 		def dividation (self):
# 			d = a/b
# 			return (d)
# except ArithmeticError :
# 	print("please check calculations")
# c1 = Calculator(10,5)
# print(c1.add())
# print(c1.sub())
# print(c1.product())
# print(c1.dividation())


# # 4. Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square
# 
# 
# class Shape :
    
#     def areas_circle (self,radius):
#         c =(3.14*radius*radius)
#         print("area of circle is",c )
#         return(c)
    
#     def area_tringle (self,base,height):
#         d = 0.5*base*height 
#         print("area of tringle is",d )
#         return(d)
#     def area_square(self,side):
#         e = 4* side
#         print("area of square is",e )
#         return(e)
    
#     def perimeter_square(self,side):
#         f=  side * side
#         print("perimeter of square is",f )
#         return(f) 
#     def perimeter_tringle (self,side1,side2,side3):
#         g = side1+side2+side3 
#         print("perimeter of tringle is",g )
#         return(g)   
#     def perimeter_circle (self,radius):
#         i =(2*3.14*radius)
#         print("perimeter of circle is",i )
#         return(i)
# s= Shape()
# s.areas_circle(5)	
# s.area_tringle(5,10)
# s.area_square(4)
# s.perimeter_square(4)
# s.perimeter_tringle(4,5,6)
# s.perimeter_circle(5)

# print("area of circle is",s.areas_circle(5) )
# print("area of tringle is",s.area_tringle(5,10) )
# print("area of square is",s.area_square(4) )
# print("perimeter of square is",s.perimeter_square(4) )
# print("perimeter of tringle is",s.perimeter_tringle(4,5,6) )
# print("perimeter of circle is",s.perimeter_circle(5) )



    
         

        

# # 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# # 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
# 7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price. 
# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# 10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
# 	Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# 	Create a constructor with parameters: accountNumber, name, balance.
# 	Create a Deposit() method which manages the deposit actions.
# 	Create a Withdrawal() method which manages withdrawals actions.
# 	Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# 	Create a display() method to display account details. Give the complete code for the BankAccount class.
	
# 12. Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

# 	Example 1:

# 	Approach:

# 	Create a class named FlashCard.
# 	Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
# 	Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
# 	Now prompt the user to answer the color of the randomly chosen fruit.
# 	If correct print correct else print wrong.
# 	Output:

# 	welcome to fruit quiz
# 	What is the color of Strawberries
# 	pink
# 	Correct answer
# 	Enter 0, if you want to play again: 0
# 	What is the color of watermelon
# 	green
# 	Correct answer
# 	Enter 0, if you want to play again: 1
	
# 13. TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

# 	eligibility criteria:
# 	if experience is more than 3 years, average feedback should be 4.5 or more
# 	if experience is 3 years or less, average feedback should be 4 or more
# 	he/she should posses the technology skill for the course
# 	Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

# 	Note:

# 	Consider all instance variables to be private and methods to be public.
# 	An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
# 	check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
# 	allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
# 	Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
	
	
# 14. Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.

# 15. A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

# 	Age is greater than 20
# 	Marks is between 0 and 100 (both inclusive)
# 	A student qualifies for admission, if

# 	Age and marks are valid and
# 	Marks is 65 or more
# 	Write a python program to represent the students seeking admission in the university.
	
# 16. Ice-Cream Scoops and Bowl shop

# 	Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

# 	Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

# 	Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

# 	Make getter and setter method for price property.

# 	Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

# 	Make a method sold in both Scoop class and Bowl class to print no of quantity sold.
	
# 17. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.


# 18. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.

# 	Sample Employee Data:
# 	"ADAMS", "E7876", 50000, "ACCOUNTING"
# 	"JONES", "E7499", 45000, "RESEARCH"
# 	"MARTIN", "E7900", 50000, "SALES"
# 	"SMITH", "E7698", 55000, "OPERATIONS"

# 	Use 'assign_department' method to change the department of an employee.
# 	Use 'print_employee_details' method to print the details of an employee.
# 	Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# 	overtime = hours_worked - 50
# 	Overtime amount = (overtime * (salary / 50))
	
# 19. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.

# 	Perform the following tasks now:

# 	Now add items to the menu.
# 	Make table reservations.
# 	Take customer orders.
# 	Print the menu.
# 	Print table reservations.
# 	Print customer orders.
# 	Note: Use dictionaries and lists to store the data.
	
# 20. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.

# 21. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.

# class mayuri :
