#challenges 1
#student Mark analyzer 
# Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.
# Your program should:
# 1. Let the user input multiple students with their marks (name + integer score).
# 2. After input is complete, display:
#    - Average marks
#    - Highest marks and student(s) who scored it
#    - Lowest marks and student(s) who scored it
#    - Total number of students

# Bonus:
# - Allow the user to enter all data first, then view the report
# - Format output clearly in a report-style layout
# - Prevent duplicate student names



# n= int(input("enter how many student marks you entered "))
# students={}
# for i in range(n):
#     name =input("enter a student name ")
#     marks = float(input("enter a student marks"))
#     students[name]=marks
# print(students) 
# k1=print(students.keys())
# v1=print(students.values())
# average_marks = sum(students.values())/n
# print(average_marks)
# highest_marks = [(k, v) for k, v in students.items() if v == max(students.values())]
# print(highest_marks)
# lowest_marks = [(k, v) for k, v in students.items() if v == min(students.values())]
# print(lowest_marks)
# total_no_of_student = len(students)
# print(total_no_of_student)


#challenges 2
# Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

# Your program should:
# 1. Ask the user to choose one of the following options:
#    - Add a new contact
#    - View all contacts
#    - Search for a contact by name
#    - Exit
# 2. Store contacts in a file called `contacts.csv` with columns:
#    - Name
#    - Phone
#    - Email
# 3. If the file doesn't exist, create it automatically.
# 4. Keep the interface clean and clear.


# Example:
# Add Contact
# View All Contacts
# Search Contact
# Exit

# Bonus:
# - Format the contact list in a table-like view
# - Allow partial match search
# - Prevent duplicate names from being added

# import csv 
# import os
# file_name = "mayuri.csv"
# if not os.path.exists("mayuri.csv"):
#     with open("mayuri.csv", "w", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["name", "phone", "email"])

# while True:
#     print("1.for add a new contanct")
#     print("2.for view all contanct")
#     print("3.for search a contanct")
#     print('4.for exist')
#     user_input = int(input("enter a number"))
    
#     if user_input == 1:
#         name = input("enter a name")
#         phone = input("enter a phone number")
#         email = input("enter a email")
#         with open("mayuri.csv", "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow([name, phone, email])
#     elif user_input ==2 :
#         with open ("mayuri.csv", "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 print(row)          
#     elif user_input == 3:
#         sname = input("enter a search name")
#         with open ("mayuri.csv", "r") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 if sname in row[0]:
#                     print(row)
#                 else:
#                     print("no name found ")
#     elif user_input == 4:
#         print("exit")
#         break          
          



# Challenge:  Personal Movie Tracker with JSON

# Create a Python CLI tool that lets users maintain their own personal movie database, 
# like a mini IMDb.

# Your program should:
# 1. Store all movie data in a `movies.json` file.
# 2. Each movie should have:
#    - Title
#    - Genre
#    - Rating (out of 10)
# 3. Allow the user to:
#    - Add a movie
#    - View all movies
#    - Search movies by title or genre
#    - Exit the app

# Bonus:
# - Prevent duplicate titles from being added
# - Format output in a clean table
# - Use JSON for reading/writing structured data

# import json
# import os 
# d={}
# file_name = "movies.json"
# if not os.path.exists(file_name):
#     with open(file_name, "w") as f:
#         json.dump([d], f)
# while True:
#     print("1.for add movie")
#     print("2 for view all movie")
#     print("3 for search movie")
#     print("4 for exist")
#     user_input = int(input("enter a number"))
#     if user_input ==1 :
#         title =input("enter a title of movie")
#         genre =input("enter a genere of movie")
#         rating = float(input("enter the rating out of 10"))
#         with open(file_name, "r") as f:
#             data = json.load(f)
#             data.append({"title": title, "genre": genre, "rating": rating})
#         with open (file_name ,"w") as f :
#             json.dump(data , f,indent =4)
        
#     elif user_input ==2 :
#         with  open (file_name ,"r")as f:
#             data =json.load(f)
#             for i in data :
#                 print(i)
#     elif user_input ==3:
#         search_input =input("enter a key to search") 
#         with  open (file_name ,"r")as f:
#             data =json.load(f)
#             for i in data :
#                 print(i) 
#                 if search_input in i.get("title", "") or search_input in i.get("genre", ""):
#                     print(i)
#                 else:
#                     print("no movie found")    
#     elif user_input ==4 :
#         print("exit")
#         break





# Challenge: Real-Time Weather Logger (API + CSV)

# Build a Python CLI tool that fetches real-time weather data for 
# a given city and logs it to a CSV file for daily tracking.

# Your program should:
# 1. Ask the user for a city name.
# 2. Fetch weather data using the OpenWeatherMap API.
# 3. Store the following in a CSV file (`weather_log.csv`):
#    - Date (auto-filled as today's date)
#    - City
#    - Temperature (in °C)
#    - Weather condition (e.g., Clear, Rain)
# 4. Prevent duplicate entries for the same city on the same day.
# 5. Allow users to:
#    - Add new weather log
#    - View all logs
#    - Show average, highest, lowest temperatures, and most frequent condition

# Bonus:
# - Format the output like a table
# - Handle API failures and invalid city names gracefully
# import requests
# from datetime import datetime

# url = "https://api.openweathermap.org/data/2.5/weather"
# params = {
#     "lat": 33.44,
#     "lon": -94.04,
#     "appid": "5d56f5663903e09be593cf3111a277e7",
#     "units": "metric"
# }


# import requests
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
    
#     # Extract fields
#     today = datetime.today().strftime("%Y-%m-%d")
#     city = data["name"]
#     temp = data["main"]["temp"]
#     condition = data["weather"][0]["main"]
    
#     # Print nicely
#     print(f"Date: {today}")
#     print(f"City: {city}")
#     print(f"Temperature: {temp} °C")
#     print(f"Weather: {condition}")
# else:
#     print("Error:", response.json())