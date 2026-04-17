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
# from datetime import date 
# class Person :
#     def __init__(self,name,country ,dob):
#         self.name = name 
#         self.country = country 
#         self.dob = dob
#     def display_dob(self):
#         return(self.dob)
#     def age_calculator (self):
#         n= date.today()
#         print(n)
#         age = n - self.dob 
#         print(age)
#         year = age.days // 365
#         print(year)
#         return("done")
    
        
# p1 =Person("mayu", "india",date(1998,11,23))
# print(p1.age_calculator())
 
# # from datetime import date 
# # n= date.today()
# # print(n)
# # print(n.year)
# # print (date(2022,11,10))






# 3. Write a Python program to create a calculator class. 
# Include methods for basic arithmetic operations.

# a= float(input("enter a number"))
# b= float(input("enter a number"))

# class Calculator:
# 	def __init__(self,a,b):
# 		self.a = a 
# 		self.b = b 
# 	def add(self):
# 		s= self.a+self.b
# 		print(s)
# 	def sub(self):
# 		m= self.a-self.b
# 		print(m)
# 	def product(self):
# 		p= self.a*self.b
# 		print(p)
# 	def dividation (self):
# 		d = self.a/self.b
# 		return (d)

# c1 = Calculator(10,5)
# c2 = Calculator(10,0)
# try:
#         print(c2.add())
#         print(c2.sub())
#         print(c2.product())
#         print(c2.dividation())

# except :
#       print("please check inputs non-zero")



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



    
         

        

# # 5. Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.




# # 6. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

# 7. Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting and deleting nodes.


# 8. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price. 

# class ShoppingCart :
#     items = []
#     def __init__(self,items,prices):
#         self.items = items
#         self.prices = prices
     
#     def add_item(self,items):
#         self.items.append(items)
#         print("items added to cart",self.items)
#     def remove_item(self,items):
#         self.items.remove(items)
#         print("item removed from cart",self.items)
#     def total_price(self,prices):
#         total = sum(self.prices)
#         print("total price of items in cart",total)
#         return total
# s = ShoppingCart(["apple","banana"],[10,20])
# s.add_item("orange")
# s.remove_item("banana")
# s.total_price([10,20,30])





# 9. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping and displaying elements.


# 10. Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.


# 11. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.
# 	Create a Python class called BankAccount which represents a bank account, 
# having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# 	Create a constructor with parameters: accountNumber, name, balance.
# 	Create a Deposit() method which manages the deposit actions.
# 	Create a Withdrawal() method which manages withdrawals actions.
# 	Create an bankFees() method to apply the bank fees with a percentage 
# of 5% of the balance account.
# 	Create a display() method to display account details. 
# Give the complete code for the BankAccount class.

# class BankAccount:
#     def __init__(self,acc_no,name,balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#     def deposite (self,amount):
#         a= self.balance + amount 
#         print("total balance is ", a)
#         return(a)
#     def withdrawal (self,amount):
#         if amount > self.balance :
#             print("insufficient balance")
#         else:
#                 b= self.balance - amount 
#                 print("total balance is ", b)
#                 return(b)
#     def Bankfees (self):
#          c=self.balance * 0.05
#          print("bank fees are ", c)
#          return(c)
#     def display (self):
#         print("account number is ", self.acc_no)
#         print("account holder name is ", self.name)
#         print("balance is ", self.balance)
# b1 = BankAccount(12345,"mayuri",10000)
# b1.deposite(5000)
# b1.withdrawal(2000)
# b1.Bankfees()
# b1.display()


# 12. Build a flashcard using class in python.
#  A flashcard is a card having information on both sides, which can be used as an aid 
# in memoization. Flashcards usually have a question on one side and an answer on the other.


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

# class FlashCard:
#     def __init__(self):
#         self.fruits = {"Banana": "yellow", "Strawberries": "pink", "watermelon":"green"}
    
#     def quiz(self):
#         import random
#         print(list(self.fruits.items()))
#         fruit, color = random.choice(list(self.fruits.items()))
#         print(f"What is the color of {fruit}?")
#         user_answer = input("Your answer: ")
#         if user_answer.lower() == color:
#                 print("Correct answer!")
#         else:
#                 print ("Wrong answer!")
# flashcard = FlashCard()
# print("Welcome to the fruit quiz!")
# while True:
#         flashcard.quiz()
#         play_again = input("Enter 0, if you want to play again: ")
#         if play_again != "0":
#                 break






	
# # 13. TechWorld, a technology training center, wants to allocate courses for instructors.
#  An instructor is identified by name, technology skills, experience and average feedback.
#  An instructor is allocated a course, if he/she satisfies the below two conditions:

# # 	eligibility criteria:
# # 	if experience is more than 3 years, average feedback should be 4.5 or more
# # 	if experience is 3 years or less, average feedback should be 4 or more
# # 	he/she should posses the technology skill for the course
# # 	Identify the class name and attributes to represent instructors.
# Write a Python program to implement the class chosen with its attributes and methods.

# # 	Note:

# # 	Consider all instance variables to be private and methods to be public.
# 	An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
# 	check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
# 	allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor.
#  Else, return false.
# 	Represent a few objects of the class, initialize instance variables using setter methods, 
# invoke appropriate methods and test your program.





# class Instructor:
#     def __init__(self,name,technology_skills,experience,average_feedback):
#         self.__name = name
#         self.__technology_skills = technology_skills
#         self.__experience = experience
#         self.__average_feedback = average_feedback
    
#     def check_eligibility(self):
#         if (self.__experience > 3 and self.__average_feedback >= 4.5) or (self.__experience <= 3 and self.__average_feedback >= 4):
#             return True
#         else:
#             return False
    
#     def allocate_course(self, technology):
#         if technology in self.__technology_skills:
#             return True
#         else:
#             return False


# instructor1 = Instructor("Alice", ["Python", "Java"], 5, 4.6)
# instructor2 = Instructor("Bob", ["Python", "C++"], 2, 4.2)
# print(instructor1.check_eligibility())  
# print(instructor1.allocate_course("Python"))
# print(instructor2.check_eligibility())
# print(instructor2.allocate_course("Java"))

        

	
	
# 14. Write a program that uses datetime module within a class. 
# Enter manufacturing date and expiry date of the product.'
#  The program must display the years, months and days that are left for expiry.

# class Product:
#     def __init__(self, manufacturing_date, expiry_date):
#         self.manufacturing_date = manufacturing_date
#         self.expiry_date = expiry_date
    
#     def time_to_expiry(self):
#         from datetime import datetime
#         today = datetime.today()
#         expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d")
                
#         time_left = expiry - today
#         print(time_left)
#         years = time_left.days // 365
#         months = (time_left.days % 365) // 30
#         days = (time_left.days % 365) % 30
#         print(f"Time left for expiry: {years} years, {months} months, and {days} days.")
# p1 = Product("2024-11-11" , "2026-11-11")
# print(p1.time_to_expiry())

# 15. A university wants to automate their admission process. 
# Students are admitted based on the marks scored in the qualifying exam. 
# A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

# 	Age is greater than 20
# 	Marks is between 0 and 100 (both inclusive)
# 	A student qualifies for admission, if

# 	Age and marks are valid and
# 	Marks is 65 or more
# 	Write a python program to represent the students seeking admission in the university.
# class Student:
#     def __init__(self, student_id, age, marks):
#         self.student_id = student_id
#         self.age = age
#         self.marks = marks
    
#     def is_valid(self):
#         return (self.age > 20 and 0 <= self.marks <= 100)
    
#     def qualifies_for_admission(self):
#         return self.is_valid() and self.marks >= 65

# student1 = Student("S001", 22, 70)
# student2 = Student("S002", 19, 80)
# print(student1.qualifies_for_admission())
# print(student2.qualifies_for_admission())

# 16. Ice-Cream Scoops and Bowl shop

# 	Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

# 	Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

# 	Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

# 	Make getter and setter method for price property.

# 	Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

# 	Make a method sold in both Scoop class and Bowl class to print no of quantity/units sold.
# class scoop :
#     def __init__(self,flavour,price):
#         self.flavour = flavour
#         self.__price = price
# class bowl :
#     def __init__(self):
#         self.__scoop_list = []
#     def add_scoops(self,*scoops):
#         self.__scoop_list.extend(scoops)
#     def get_price(self):
#         price=[]
#         for scoop in self.__scoop_list :
#             price.append(scoop._scoop__price)
#         return sum(price)
    
#     def display(self):
#         for scoop in self.__scoop_list:
#             print(f"Flavour: {scoop.flavour}, Price: {scoop._scoop__price}")
#         print(f"Total price of the bowl: {self.get_price()}")
#     def sold(self):

#         print(f"Number of scoops sold: {len(self.__scoop_list)}")
# s1 = scoop("vanilla", 50)
# s2 = scoop("chocolate", 60)
# b1 = bowl()
# b1.add_scoops(s1, s2)
# b1.display()
# b1.sold()
	
# # 17. Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# # Note: The bus seating capacity is 50. so the final fare amount should be 5500. Y
# ou need to override the fare() method of a Vehicle class in Bus class.

# class vehicle:
#     def __init__(self,seating_capacity):
#         self.seating_capacity = seating_capacity
#     def fare(self):

#         return (self.seating_capacity * 100)
# class Bus(vehicle):
    

#     def __init__(self, seating_capacity):
#         super().__init__(seating_capacity)
    
#     def fare(self):
#         base_fare = super().fare()
#         maintenance_charge = base_fare * 0.10
#         return (base_fare + maintenance_charge)

# b1 = Bus(50)
# print(b1.fare())


# 18. Write a Python class Employee with attributes like 
# emp_id, emp_name, emp_salary, and emp_department and 
# methods like calculate_emp_salary, emp_assign_department, and print_employee_details.

# 	Sample Employee Data:
# 	"ADAMS", "E7876", 50000, "ACCOUNTING"
# 	"JONES", "E7499", 45000, "RESEARCH"
# 	"MARTIN", "E7900", 50000, "SALES"
# 	"SMITH", "E7698", 55000, "OPERATIONS"

# 	Use 'assign_department' method to change the department of an employee.
# 	Use 'print_employee_details' method to print the details of an employee.
# 	Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
# which is the number of hours worked by the employee. If the number of hours worked is more than 50, 
# the method computes overtime and adds it to the salary. 
# Overtime is calculated as following formula:
# 	overtime = hours_worked - 50
# 	Overtime amount = (overtime * (salary / 50))
# class Employee :
#     def __init__(self,emp_id, emp_name, emp_salary,  emp_department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department
    
#     def calculate_emp_salary(self,salary , hours_worked) :
#         if hours_worked > 50 :
#                 overtime = hours_worked - 50
#                 overtime_amount = (overtime * (salary / 50))
#                 total_salary = salary + overtime_amount
#                 print(f"Total salary including overtime: {total_salary}")
#         else:
#                 print(f"Total salary: {salary}")
#     def emp_assign_department(self, new_department):
#         self.emp_department = new_department
#         print(f'new deparrtment assign to {self.emp_name} is {new_department}')
#         return(new_department)
#     def print_emp_details (self):
#         print("employee name is " ,self.emp_name )
#         print("employee id is ",self.emp_id )
#         print("employee salary is ",self.emp_salary )
#         print("employee dept is ",self.emp_department )

# e1 = Employee("E7876", "mayu", 50000, "hr")
# print(e1.print_emp_details())
# print(e1.emp_assign_department("data science"))
# print(e1.calculate_emp_salary(50000, 55))






# 19. Write a Python class Restaurant with attributes like menu_items, book_table, and 
# customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.

# 	Perform the following tasks now:

# 	Now add items to the menu.
# 	Make table reservations.
# 	Take customer orders.
# 	Print the menu.
# 	Print table reservations.
# 	Print customer orders.
# 	Note: Use dictionaries and lists to store the data.

# class Resturant:
#     def __init__(self,menu_item ,book_table, customer_order):
#         self.menu_item = []
#         self.book_table = []
#         self.customer_order = customer_order
#     def add_item_to_menu (self,new_menu):
#         p= (self.menu_item).append(new_menu)
#         return(p)
#     def table_reservation (self, table_number):
#         if table_number in self.book_table:

#                 print(f" table  of {table_number} is reserved")
#         else:
#                 print("not reserved")
#         return("booked")
#     def customers_order_display(self):
#         print("customers order is " , self.customer_order)
# r1= Resturant(["a","b"],102,"a")
# print(r1.add_item_to_menu("l"))
# print(r1.table_reservation(201))
# print(r1.customers_order_display())


	
# 20. Write a Python class BankAccount with attributes like account_number, balance, 
# date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
# class BankAccount:
#     def __init__(self,account_number,balance,date_of_opening , customer_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.date_of_opening = date_of_opening
#         self.customer_name = customer_name
#     def deposite (self,amount):
#         self.balance +=amount
#         return(self.balance)
#     def  withdraw (self,amount):
#         if amount> self.balance:
#             print("insufficient amount")
#         else: 
#             self.balance -=amount
#             return(self.balance)
#     def check_balance(self):
#         print("the current balance is ",self.balance)
#         return(self.balance)
# b1= BankAccount(10109876,6000,"2023-11-11","mayu")
# print(b1.deposite(2000))
# print(b1.withdraw(5000))
# print(b1.check_balance())

        

# 21. Write a Python class Inventory with attributes like 
# item_id, item_name, stock_count, and price, and 
# methods like add_item, update_item, and check_item_details.
# class Inventory :
#     def __init__(self,item_id, item_name, stock_count, price):
#         self.item_id = item_id
#         self.item_name = item_name
#         self.stock_count = stock_count
#         self.price = price
#     def add_item(self, new_item):
#         self.item_id.append(new_item.item_id)
#         self.item_name.append(new_item.item_name)
#         self.stock_count.append(new_item.stock_count)
#         self.price.append(new_item.price)
#         return("item added")
#     def update_item(self, item_id, new_stock_count):
#         for i in range(len(self.item_id)):
#             if self.item_id[i] == item_id:
#                 self.stock_count[i] = new_stock_count
#                 return("stock count updated")
#         return("item not found")

#     def check_item_details(self, item_id):
#         for i in range(len(self.item_id)):
#             if self.item_id[i] == item_id:
#                 print(f"Item ID: {self.item_id[i]}, Item Name: {self.item_name[i]}, Stock Count: {self.stock_count[i]}, Price: {self.price[i]}")
#                 return
#         print("item not found")        
