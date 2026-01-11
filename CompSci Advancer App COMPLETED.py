#Hello, welcome to my code. Please enjoy the read.

#This code is used for my app called "CompSci Advancer".

#this import connects to mysql
import mysql.connector
#used for encryption for hashing
import hashlib

#tkinter is used for the user interface
from tkinter import *
from tkinter.ttk import *
import webbrowser
import random
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import Button
from tkinter import Label

#these imports are for webscraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#this import is used for time
import time

#for opening up files and images
import os
from PIL import Image

#-----------------------------------------------------------------------------------------------------------------------
#This is the start of my code, firstly connecting to the database using mysql, and this section is used to connect
#to my MySQL account's database
try:
	mydatabase = mysql.connector.connect(host = "localhost",
										user = "N",
										password = "RalphLauren15%")
	myCursor = mydatabase.cursor()
	myCursor.execute("CREATE DATABASE mydatabase")
except Exception as e:
	print(f"Error in creating database: {e}")

mydatabase = mysql.connector.connect(
  host="localhost",
  user = "N",
  password = "RalphLauren15%",
  database="mydatabase"
)

#the next step after connected, is to create two tables for the user, which will be used later for logging in
#this users table adds a unique username and a name to identify the student
myCursor = mydatabase.cursor()
myCursor.execute("""
CREATE TABLE IF NOT EXISTS user_id (
	userID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	username VARCHAR(255) UNIQUE
)
""")

#this table is used for storing the password, which will also be used for logging in
myCursor.execute("""
CREATE TABLE IF NOT EXISTS password_id (
	passID INT AUTO_INCREMENT PRIMARY KEY,
	userID INT NOT NULL,
	password VARCHAR(255),
	FOREIGN KEY (userID) REFERENCES user_id(userID)
)
""")

#this creates the table flashcards for the flashcard section
myCursor.execute("""
	CREATE TABLE IF NOT EXISTS flashcards (
		flashID INT AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(255),
		question TEXT NOT NULL,
		answer TEXT NOT NULL,
		FOREIGN KEY (username) REFERENCES user_id(username)
)
""")

#I have saved this section in comments so that if you would like to see what is in the database, then you can run this code
# #this part of the code is used to print out the tables for the testing phase
# myCursor.execute("SELECT * FROM user_id")
# users = myCursor.fetchall() 
# print("Users table: ")
# for row in users:
# 	print(row)

# myCursor.execute("SELECT * FROM password_id")
# passwords = myCursor.fetchall()
# print("\n Passwords Table: ")
# for row in passwords:
# 	print(row)

# myCursor.execute("SELECT * FROM flashcards")
# fcards = myCursor.fetchall()
#print("\n Flashcards table: ")
# for row in fcards:
# 	print(row)

#This part of code is used for hashing, hashlib output will not change the same text input each time it is run
def hashing_pass(password):
	encode_bytes = password.encode()
	hashing = hashlib.sha256(encode_bytes)
	hexadecimal_password = hashing.hexdigest()
	return hexadecimal_password

#-----------------------------------------------------------------------------------------------------------------------
#This creates the files which store the links to the resources for the learning section, which are seperated by units
#and the type of resource, such as video or pdfs
#unit 1 files
unit1file = open("unit1.txt","w")
unit1file.write("1.1 PMT PDF https://physicsandmathstutor.co.uk/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.co.uk%2Fdownload%2FComputer-Science%2FA-level%2FNotes%2FAQA%2F01-Fundamentals-of-Programming%2FAdvanced%2F1.1.%20Programming%20-%20Advanced.pdf \n")
unit1file.write("1.2 PMT PDF https://physicsandmathstutor.co.uk/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.co.uk%2Fdownload%2FComputer-Science%2FA-level%2FNotes%2FAQA%2F01-Fundamentals-of-Programming%2FAdvanced%2F1.2.%20Programming%20Paradigms%20-%20Advanced.pdf \n")
unit1file.write("1.1 CraigNDave YT Videos https://physicsandmathstutor.co.uk/computer-science-revision/a-level-aqa/programming/programming-videos/ \n")
unit1file.write("1.2 CraigNDave YT Videos https://physicsandmathstutor.co.uk/computer-science-revision/a-level-aqa/programming/programming-paradigms-videos/ \n")
unit1file.close()

#unit 11 files
unit11file = open("unit11.txt", "w")
unit11file.write("11 PMT PDF https://physicsandmathstutor.co.uk/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.co.uk%2Fdownload%2FComputer-Science%2FA-level%2FNotes%2FAQA%2F11-Big-Data%2FAdvanced%2F11.%20Big%20Data%20-%20Advanced.pdf \n")
unit11file.write("11 CraigNDave YT Videos https://physicsandmathstutor.co.uk/computer-science-revision/a-level-aqa/big-data/big-data-videos/ \n")
unit11file.close()

#unit 1 definitions
unit1definitions = open("unit1def.txt", "w")
unit1definitions.write("1.1 PMT Definitions https://physicsandmathstutor.co.uk/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.com%2Fdownload%2FComputer-Science%2FA-level%2FNotes%2FAQA%2F01-Fundamentals-of-Programming%2FDefinitions.pdf \n")
unit1definitions.close()

#unit 11 definitions
unit11definitions = open("unit11def.txt", "w")
unit11definitions.write("11 PMT Definitions https://physicsandmathstutor.co.uk/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.com%2Fdownload%2FComputer-Science%2FA-level%2FNotes%2FAQA%2F01-Fundamentals-of-Programming%2FDefinitions.pdf \n")
unit11definitions.close()

#-----------------------------------------------------------------------------------------------------------------------
#These are the AI generated multiple choice questions, they are seperated into units with question and answer and options
#in a dictionary, that will be displayed

#unit 1 questions, options and answers
unit1 = [
	{
		"question": "Which of the following is the correct data type for storing the value of a person's age?",
		"options": ["String", "Integer", "Float", "Boolean"],
		"answer": "Integer"
	},
	{
		"question": "Which of the following statements is used to exit a loop prematurely in most programming languages?",
		"options": ["Continue", "Break", "Return", "Stop"],
		"answer": "Break"
	},
	{
		"question": "Which of the following sorting algorithms has the best average time complexity?",
		"options": ["Bubble Sort", "Selection Sort", "Merge Sort", "Insertion Sort"],
		"answer": "Merge Sort"
	},
	{
		"question": "Which of the following is the correct way to handle an exception in Python?",
		"options": ["if...else", "try...except", "switch...case", "try...finally"],
		"answer": "try...except"
	},
	{
		"question": "What will be the output of the following Python code?\n" 
			 "arr = [10, 20, 30, 40]\n" 
			 "print(arr[2])",
		"options": ["10", "20", "30", "40"],
		"answer": "30"
	}
]

#unit11 questions, options and answers
unit11 = [
	{
		"question": "Which of the following is NOT one of the 3 Vs associated with Big data?",
		"options": ["Volume", "Velocity", "Variability", "Variety"],
		"answer": "Variability"
	},
	{
		"question": "What is one of the challenges associated with Big data analytics",
		"options": ["Data compression", "Data visualisation in a useful way", "Reduced computational requirements", "Decrease in data accuracy"],
		"answer": "Data visualisation in a useful way"
	},
	{
		"question": "What does velocity refer to in Big data terms",
		"options": ["The speed at which data is generated and processed", "The amount of data generated", "The variety of data types available", "The accuracy of data"],
		"answer": "The speed at which data is generated and processed"
	},
	{
		"question": "What are ethical concerns when dealing with Big Data",
		"options": ["Increased storage costs", "Inefficiency in data processing", "Privacy and security of an individuals data", "Limited variety of data sources"],
		"answer": "Privacy and security of an individuals data"
	},
	{
		"question": "What does Variety in the context of big data refer to?",
		"options": ["The speed at which data is generated", "The different types and formats of data being processed", "The reliability of the data sources", "The size of the data set"],
		"answer": "The different types and formats of data being processed"
	}
]

#-----------------------------------------------------------------------------------------------------------------------
#This section of code is used for the hashtable
#We first have the node pointer which navigates through the linked list
class Node_pointer():
	def __init__(self, key, value):
		#each node in this linked list will have a pointer to the next
		#node and each node will have a key and value pair
		self.__key = key  
		self.__value = value 
		self.__next = None 
	
	#these functions are used to help navigate through the linked list
	#getting the key from the key value pair
	def get_key(self):
		return self.__key

	#getting the next node
	def get_next(self):
		return self.__next

	#set pointer to next node
	def set_next(self, next_node):
		self.__next = next_node

#This class is used to create the actual hash table, which is in the form of a linked list
class Hash_table():
	def __init__(self, capacity):
		#these are private attributes so that the user cannot change these
		self.__capacity = capacity 
		self.__size = 0  
		self.__table = [None] * capacity 

	#this function creates an index to store the key value pair with the input
	#of a key. using this should reduce the chance of collisions
	def _hash_key(self, key): 
		return hash(key) % self.__capacity

	#this function is used to store the key and password from the user into the hash table
	def insert(self, key, password):
		#this uses the hashing function from earlier on in the code
		#to create a hashed verison of the password to store
		hashed_password = hashing_pass(password)  
		#the index is the position to be stored, and is created through the 
		#_hash_key function
		index = self._hash_key(key)  

		#creates a node with the values and makes it as head of the list
		if self.__table[index] is None:
			self.__table[index] = Node_pointer(key, hashed_password) 
			self.__size += 1
		#otherwise, if there is a list at that index it will find the 
		#last node
		else:
			current = self.__table[index]
			while current:
				if current.get_key() == key:
					current.set_next(Node_pointer(key, hashed_password))  
					return
				current = current.get_next()
			new_node = Node_pointer(key, hashed_password)
			new_node.set_next(self.__table[index]) 
			self.__table[index] = new_node
			self.__size += 1

	#this method retrives the value that is stored with a key, by finding
	#the index it should be stored in from the _hash_key function
	#when putting in the key
	def search(self, key):
		index = self._hash_key(key)
		current = self.__table[index]

		while current:
			if current.get_key() == key:
				return True
			current = current.get_next()
		return False

	#this method removes a key value pair from the linked list inside of
	#the hash table. It does this by searching for the index that it
	#should be stored at, and then remove the node from the list
	def remove(self, key):
		index = self._hash_key(key)

		previous = None
		current = self.__table[index]

		while current:
			if current.get_key() == key:
				if previous:
					previous.set_next(current.get_next()) 
				else:
					self.__table[index] = current.get_next()
				self.__size -= 1
				return
			previous = current
			current = current.get_next()

#-----------------------------------------------------------------------------------------------------------------------
#This is the first window that will pop up to the user when running the code
class Main(Tk):
	def __init__(self):
		#initialises tkinter so that attributes and methods like title and geometry can be used
		super().__init__()
		
		#this creates the frame and title of the window to be displayed
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		#This creates the option for the main screen
		title_screen = Label(self, text = "CompSci Advancer", font=("Arial, 36"))
		#pack is used to display the label on the window
		title_screen.pack(pady=10)

		choose = Label(self, text="Welcome, please choose an option", font=("20"))
		choose.pack(pady=10)

		#the command at the end opens up the login function and runs it
		login_button = Button(self, text="Login", font = ("24"), bg = "#000090", fg = "#FFFFFF", command=self.login)
		login_button.pack(pady=10)

		#the same happens for this button, where clicking it causes the command to run and open up sign_up function
		sign_up_button = Button(self, text="Sign Up", font= ("24"), bg = "#5d8bd4", fg = "#FFFFFF", command=self.sign_up)
		sign_up_button.pack(pady=10)

	#These functions will open up the classes when they are called by clicking the buttons on the window, instantiating them
	def login(self):
		self.newWindow = Login(self)
	
	def sign_up(self):
		self.newWindow = Sign_Up()

#-----------------------------------------------------------------------------------------------------------------------
#This class will be used for the Signing up stage, we are using Toplevel, as the Main class is the root and so these will
#appear on top of it
class Sign_Up(Toplevel):
	def __init__(self):
		super().__init__()
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		#These variables will be used later on to store them in the database, using StringVar() to directly access them
		#from the entry labels
		self.__name = StringVar() 
		self.__username = StringVar()  
		self.__password = StringVar()  

		#Creates the window to display everything and get user input
		create_label_lbl = Label(self, text="Create an account", font=("32"))
		create_label_lbl.pack(pady=5)
		
		#using entry labels to collect the input from users
		create_name_lbl = Label(self, text="Enter your name")
		create_name_lbl.pack()
		create_name = Entry(self, textvariable=self.__name)
		create_name.pack(pady=5)

		create_username_lbl = Label(self, text="Enter a username")
		create_username_lbl.pack(pady=5)
		create_username = Entry(self, textvariable=self.__username)
		create_username.pack(pady=5)

		create_password_lbl = Label(self, text="Enter a password")
		create_password_lbl.pack(pady=5)
		create_password = Entry(self, textvariable=self.__password)
		create_password.pack(pady=5)

		#clicking this button opens up the function __create
		create_button = Button(self, text="Create", command=self.__create)
		create_button.pack(pady=5)

	#this subroutine is used when the user wants to create an account
	def __create(self):
		#the .strip() will get rid of whitespaces in case the user acidentally adds a space so it doesn't create an error
		#when we get to the login stage for when I have to compare the variables and a space has not been accounted for
		names = self.__name.get().strip()
		usernames = self.__username.get().strip()
		passwords = self.__password.get().strip()
		#this variable is used to keep track for when we do validation, so that we will only add the user when correct is True
		correct = True

		#this is the error handling to check that the users entry isn't empty by checking the length of variables
		if len(usernames) == 0 or len(names) == 0:
			enter_again = Label(self, text="Entry is empty. Please enter again", fg="red")
			enter_again.pack(pady=3)
			#sets correct to False so we cannot store the user's details
			correct = False

		#this is to check that the users password is longer than 8 characters, to make it more secure
		#so that the probability of another student being able to guess the password is lowered
		if len(passwords) < 8:
			enter_again = Label(self, text="Password must be 8 or more characters.", fg="red")
			enter_again.pack(pady=3)
			correct = False

		#this part of the code checks to make sure username and name are not mixed up since the name will identify which
		#student it is, and the username can be any random unique name
		if names.isalpha() == False:
			enter_again = Label(self, text="Name must not contain any numbers or special digits.", fg="red")
			enter_again.pack(pady=3)
			correct = False

		#since the username is unique, this will check if it already exists or not, since we don't want two of the same users,
		#we do this by creating an SQL query that looks for that username in the users table
		myCursor = mydatabase.cursor()
		myCursor.execute("SELECT * FROM user_id WHERE username = %s", (usernames,))
		myresult = myCursor.fetchall()

		#if they find an instance of the username in the users table then it will ask them to choose a different one
		if len(myresult) > 0:
			enter_again = Label(self, text="Username already exists. Please choose another.", fg="red")
			enter_again.pack(pady=3)
			correct = False
		
		#Creates the hashtable with a space of 30 (class size roughly), and uses the variable correct from earlier to
		#check the user has passed all the validation
		if correct == True:
			user_detail = Hash_table(30)
			key = usernames
			#using the insert function from the hash table class
			user_detail.insert(key, passwords)
			#using the hashing algorithm to create a hashed password to store

		#if it has met all the criterias, correct will stay as true and will insert it into the database
		if correct == True:
			#the try is used so that if it fails to add the user, it will not crash the program
			try:
				#using the hashing algorithm to create a hashed password to store from the user input
				encrypted_password = hashing_pass(passwords)
				#doing an SQL query to insert username and name into the table for user details
				sql = "INSERT INTO user_id (name, username) VALUES (%s, %s)"
				val = (names, usernames)
				myCursor.execute(sql, val)
				mydatabase.commit()
				print(myCursor.rowcount, "account succesfully saved")
				users_id = myCursor.lastrowid

				#doing another SQL query to store the password to the passwords table
				sql = "INSERT INTO password_id (userID, password) VALUES (%s, %s)"
				val = (users_id, encrypted_password)
				myCursor.execute(sql, val)
				mydatabase.commit()

				succesful_lbl = Label(self, text="Account created", font=("24"))
				succesful_lbl.pack(pady=5)

				close_button = Button(self, text="Close", command=self.destroy)
				close_button.pack(pady=10)
			except Exception as e:
				print(f"Error: {e}")
		else:
			fail_label = Label(self, text="Account failed to create", fg="red")
			fail_label.pack(pady=3)

#-----------------------------------------------------------------------------------------------------------------------
#This class creates the login section
class Login(Toplevel):
	def __init__(self, parent):
		super().__init__()
		self.parent = parent
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		#this count variable will be used to keep record of the number of login attemps the user has had
		self.__count = 0 
		self.__temp_username = StringVar()
		self.__temp_password = StringVar()

		login_label = Label(self, text="Login", font=("32"))
		login_label.pack(pady=10)

		username_label = Label(self, text="Username")
		username_label.pack(pady=10)
		username_entry = Entry(self, textvariable=self.__temp_username)
		username_entry.pack(pady=10)

		password_label = Label(self, text="Password")
		password_label.pack(pady=10)
		password_entry = Entry(self, show="*", textvariable=self.__temp_password)
		password_entry.pack(pady=10)

		self.login_button = Button(self, text="Login", command=self.__check_details)
		self.login_button.pack(pady=10)

	#this function will be used when the user has entered its details to login
	def __check_details(self):
		success = False
		global temp_username
		temp_username = self.__temp_username.get()
		#because hashlib produces the same output if the input is the same, we can check if the hashed input is the same
		#as the stored hashed password, comparing the two to see if there is a match
		temp_password = hashing_pass(self.__temp_password.get())

		#count limits number of login attemps, so that people cannot just guess other peoples password
		if self.__count >= 5:
			self.login_button.config(state=tk.DISABLED)
			count_label = Label(self, text="You have reached the maximum number of login attempts", fg="red")
			count_label.pack(pady=10)
			close_button = Button(self, text="Close", command=self.quit)
			close_button.pack(pady=10)
			return
		
		#A query to fetch the username and password from the joined tables to compare with
		try:
			myCursor = mydatabase.cursor()
			sql = ("""
			SELECT user_id.username, password_id.password
			FROM user_id
			INNER JOIN password_id ON user_id.userID = password_id.userID
			WHERE user_id.username = %s
			""")
			myCursor.execute(sql, (temp_username,))
			result = myCursor.fetchone()
		except Exception as e:
			print(f"Error: {e}")

		#this compares the stored hash password to the user input password that has been hashed
		if result != None:
			#result gives us a row which is stored as an array, so we can take the second item in the array, which will
			#be the password and use that to compare it
			db_password = result[1]
			if db_password == temp_password:
				success = True
				success_label = Label(self, text="Successfully logged in", fg="green")
				success_label.pack(pady=10)
			else:
				fail_label = Label(self, text="Password is wrong", fg="red")
				fail_label.pack(pady=10)
				#adding to count if they have the wrong password
				self.__count += 1
		#this is the result of a username entered by the user not being found
		else:
			fail_label = Label(self, text="Account does not exist", fg="red")
			fail_label.pack(pady=10)
			#adding to count if they have the wrong username
			self.__count += 1

		#this instantiates home if success, since the user has succesfully signed in
		if success == True:
			self.destroy()
			self.newWindow = Home(self.parent)
			#the withdraw is used so that we can hide the root window which is main, since we do not want all the windows
			#open while the user is using the app
			self.parent.withdraw()

#-----------------------------------------------------------------------------------------------------------------------
#creates the home screen as home class
class Home(Toplevel):
	def __init__(self, parent):
		super().__init__(parent) 
		self.title("CompSci Advancer")
		self.geometry("1280x720")
	
		title = Label(self, text="CompSci Advancer", font=("Arial", "36")) 
		title.place(relx = 0.5, rely = 0.2, anchor = CENTER)

		slogan = Label(self, text="'The only revision source you will ever need!'", font=("Arial", "20", "italic")) 
		slogan.place(relx = 0.5, rely = 0.3, anchor = CENTER)

		#the user is displayed with options to choose from
		revision_button = Button(self, text="Revision", command=self.openRevision)
		revision_button.place(relx=0.4, rely=0.5, anchor=CENTER)

		learning_button = Button(self, text="Learning", command=self.openLearning)
		learning_button.place(relx=0.5, rely=0.5, anchor=CENTER)

		esq_button = Button(self, text = "Exam stye questions", command = self.openESQ)
		esq_button.place(relx = 0.6, rely = 0.5, anchor=CENTER)

		flashcard_button = Button(self, text="Flashcards", command=self.openFlashcards)
		flashcard_button.place(relx=0.7, rely=0.5, anchor=CENTER)

		#this will be used if the user wishes to exit the program
		close_button = Button(self, text="Exit", command=self.exit)
		close_button.place(relx=0.5, rely=0.7, anchor=CENTER)

	#the exit function kills Main ending the program
	def exit(self):
		self.destroy()
		self.quit()
	
	#functions to instantiate other classes
	def openRevision(self):
		self.newWindow = Revision(self)

	def openLearning(self):
		self.newWindow = Learning(self)
	
	def openESQ(self):
		self.newWindow = ESQ_options(self)
	
	def openFlashcards(self):
		self.newWindow = Flashcard_sys(self)
#-----------------------------------------------------------------------------------------------------------------------
#these classes filter out which unit the user would like to do
class Revision(Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		filter_label = Label(self, text = "Please filter a unit: ", font = ("Arial", "36"))
		filter_label.pack(pady= 5, padx = 5)
		unit1 = Button(self, text="Unit 1 - Fundementals of Programming MCQs", command= self.openMCQ1)
		unit1.pack(padx=5, pady=5)

		unit11 = Button(self, text="Unit 11 - Big data MCQs", command= self.openMCQ11)
		unit11.pack(pady=5, padx=5)

	#depending on the unit, the MCQ class will be opened, with the questions stored earlier being used
	def openMCQ1(self):
		#inside of the instantiation, the dictionary storing the questions, options and answers is used within that class
		MCQ1 = MCQ(unit1)  

	def openMCQ11(self): 
		MCQ11 = MCQ(unit11)  
#-----------------------------------------------------------------------------------------------------------------------
#This is the class for the Learning option, that will also filter out the unit
class Learning(Toplevel):
	def __init__(self, parent):
		super().__init__(parent) 
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		#It will ask to filter a unit out, the pack_forget() method saves the code from having to open up a new window, and
		#instead just clears up the current window
		filter_label = Label(self, text = "Please filter a unit: ", font = ("Arial", "36"))
		filter_label.pack(pady= 5, padx = 5)
		unit1_btn = Button(self, text="Unit 1 - Fundementals of Programming", command= lambda:[unit1_btn.pack_forget(), 
																						   unit11_btn.pack_forget(), 
																						   filter_label.pack_forget(),
																						   self.openLearning1()])
		unit1_btn.pack(padx=5, pady=5)

		unit11_btn = Button(self, text="Unit 11 - Big data", command=lambda: [unit1_btn.pack_forget(), 
																		  unit11_btn.pack_forget(),
																		  filter_label.pack_forget(), 
																		  self.openLearning11()])
		unit11_btn.pack(pady=5, padx=5)

		#This function will be used later to open up URLs
	def open_url(self, url):
		webbrowser.open_new_tab(url)

	#Upon selecting a button to filter the unit, the user will be displayed with resources for the chosen option
	def openLearning1(self):
		resources_label = Label(self, text = "Here are the resources available for unit 1.1 and 1.2: ", font=("Arial, 24"))
		resources_label.pack(pady = 3, padx = 5)
		#Unit 1.1 Button for PMT PDF
		unit1_1 = Label(self, text ="1.1 PMT PDF", font=("Arial","18", "underline"))
		unit1_1.pack(pady=5, padx=5)
		#This part of the code grabs the URL from the file
		with open("unit1.txt", "r") as file:
			for line in file:
				#this is used to filter out only 1.1 PMT pdfs
				if "1.1 PMT PDF" in line:
					#using line.replace to get rid of the text and any empty spaces and only leaving the url to use
					url1_1 = line.replace("1.1 PMT PDF", "").strip()
					break
		#This binds the label with a button feature, and in our case it will open up a link, using <Button-1>, which
		#waits for a left click as a signal to open the link
		unit1_1.bind("<Button-1>", lambda e: self.open_url(url1_1))

		#The same code above is used to create links for the other resources

		#Unit 1.2 Button for PMT PDF
		unit1_2 = Label(self, text ="1.2 PMT PDF", font=("Arial","18", "underline"))
		unit1_2.pack(pady=5, padx=5)
		with open("unit1.txt", "r") as file:
			for line in file:
				if "1.2 PMT PDF" in line:
					url1_2 = line.replace("1.2 PMT PDF", "").strip()
					break
				
		unit1_2.bind("<Button-1>", lambda e: self.open_url(url1_2))
		
		#Unit 1.1 Button for YT Videos
		unit1_1YT = Label(self, text ="1.1 CraigNDave YT Videos", font=("Arial","18", "underline"))
		unit1_1YT.pack(pady=5, padx=5)
		with open("unit1.txt", "r") as file:
			for line in file:
				if "1.1 CraigNDave YT Videos" in line:
					url1_1YT = line.replace("1.1 CraigNDave YT Videos", "").strip()
					break
				
		unit1_1YT.bind("<Button-1>", lambda e: self.open_url(url1_1YT))

		#Unit 1.2 Button for YT Videos
		unit1_2YT = Label(self, text ="1.2 CraigNDave YT Videos", font=("Arial","18", "underline"))
		unit1_2YT.pack(pady=5, padx=5)
		with open("unit1.txt", "r") as file:
			for line in file:
				if "1.2 CraigNDave YT Videos" in line:
					url1_2YT = line.replace("1.2 CraigNDave YT Videos", "").strip()
					break
				
		unit1_2YT.bind("<Button-1>", lambda e: self.open_url(url1_2YT))

		keyword_label = Label(self, text = "Keyword resources for unit 1.1 and 1.2: ", font=("Arial, 24"))
		keyword_label.pack(pady = 3, padx = 5)
		#Unit 1 Button for keywords
		unit1 = Label(self, text ="1.1 & 1.2 PMT Keywords", font=("Arial","18", "underline"))
		unit1.pack(pady=5, padx=5)
		with open("unit1def.txt", "r") as file:
			for line in file:
				if "1.1 PMT Definitions" in line:
					url1def = line.replace("1.1 PMT Definitions", "").strip()
					break
				
		unit1.bind("<Button-1>", lambda e: self.open_url(url1def))

	#The same code is repeated for unit11
	def openLearning11(self):
		resources_label = Label(self, text = "Here are the resources available for unit 11 ", font=("Arial, 24"))
		resources_label.pack(pady = 3, padx = 5)
		#Unit 11 Button for PMT PDF
		unit11 = Label(self, text ="11 PMT PDF", font=("Arial","18", "underline"))
		unit11.pack(pady=5, padx=5)
		with open("unit11.txt", "r") as file:
			for line in file:
				if "11 PMT PDF" in line:
					url11 = line.replace("11 PMT PDF", "").strip()
					break
				
		unit11.bind("<Button-1>", lambda e: self.open_url(url11))

		#Unit 11 Button for YT Videos
		unit11YT = Label(self, text ="11 CraigNDave YT Videos", font=("Arial","18", "underline"))
		unit11YT.pack(pady=5, padx=5)
		with open("unit11.txt", "r") as file:
			for line in file:
				if "11 CraigNDave YT Videos" in line:
					url11YT = line.replace("11 CraigNDave YT Videos", "").strip()
					break
				
		unit11YT.bind("<Button-1>", lambda e: self.open_url(url11YT))

		#Unit 11 Button for keywords
		keyword_label = Label(self, text = "Keyword resources for unit 11: ", font=("Arial, 24"))
		keyword_label.pack(pady = 3, padx = 5)
		unit11key = Label(self, text ="11PMT Keywords", font=("Arial","18", "underline"))
		unit11key.pack(pady=5, padx=5)
		with open("unit11def.txt", "r") as file:
			for line in file:
				if "11 PMT Definitions" in line:
					url11def = line.replace("11 PMT Definitions", "").strip()
					break
				
		unit11key.bind("<Button-1>", lambda e: self.open_url(url11def))

#-----------------------------------------------------------------------------------------------------------------------
#this class is used to present the user with options for exam style questions
class ESQ_options(Toplevel):
	def __init__(self, parent):
		super().__init__(parent) 
		self.title("CompSci Advancer")
		self.geometry("1280x720")

		filter_label = Label(self, text = "Please filter a unit: ", font = ("Arial", "36"))
		filter_label.pack(pady= 5, padx = 5)

		unit1_btn = Button(self, text="Unit 1 - Fundementals of Programming", command=self.openESQ1)
		unit1_btn.pack(padx=5, pady=5)

		unit11_btn = Button(self, text="Unit 11 - Big data", command=self.openESQ11)
		unit11_btn.pack(pady=5, padx=5)

	#These functions instantiate the ESQ class with the file_path used to access the exam style questions for that unit
	def openESQ1(self):
		file_path = "esq1.txt"
		ESQ1 = ESQ(file_path)

	def openESQ11(self):
		file_path = "esq11.txt"
		ESQ11 = ESQ(file_path)

#-----------------------------------------------------------------------------------------------------------------------
#this class is used for the Multiple choice questions system
class MCQ(Toplevel):
	def __init__(self, questions):
		super().__init__()
		self.title("CompSci Advancer")
		self.geometry("720x540")

		#this random is used to shuffle up the questions, so that each time the user runs it, it appears in a different order
		random.shuffle(questions)
		
		#this variable holds the list of questions to be used
		self.questions = questions
		#this tracks the score of correct answers
		self.score = 0
		#this tracks the question the user is currently on
		self.question_number = 0
		#this will store the answers for wrong questions
		self.wrong_answers = [] 
		#this will store the questions for the wrong questions
		self.incorrect_questions = []

		self.question_label = tk.Label(self, text="", wraplength=600, justify="center")
		self.question_label.pack(pady=20)

		#self.var is used to collect the user's selected answer from the MCQ
		self.var = tk.StringVar()
		self.options_frame = tk.Frame(self)
		self.options_frame.pack(pady=20)
		self.option_buttons = []
		#this determines the number of options to display, which is always 4
		for i in range(len(self.questions[0]["options"])):
			#tk.radiobuttons are the buttons that the user can click on to answer a question
			btn = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="")
			btn.pack(anchor="w")
			self.option_buttons.append(btn)

		self.next_button = tk.Button(self, text="Next", command=lambda: [self.check_answer(), self.next_question()])
		self.next_button.pack(pady=20)

		self.close_button = tk.Button(self, text="Close", command=self.destroy)
		self.close_button.pack(pady=10)

		self.load_question()

	#this method will load the question and the options to the MCQ system
	def load_question(self):
		#this gets the current question
		question = self.questions[self.question_number]
		self.question_label.config(text=question["question"])
		#this sets all the radiobuttons to be empty
		self.var.set(None)

		#this code creates the buttons with the answers, i as the index
		#and option as the actual option text. The enumerate returns each
		#item in the list. The config is used to display
		#this text.
		for i, option in enumerate(question["options"]):
			self.option_buttons[i].config(text=option, value=option)

	#this checks if the answer selected in self.var is correct
	def check_answer(self):
		#gets the correct answer from the dictionary
		correct_answer = self.questions[self.question_number]["answer"]
		selected_answer = self.var.get()
		if selected_answer == correct_answer:
			#keeps record of the score
			self.score += 1
		else:
			#this is used to display the question and answer that are wrong later on
			self.wrong_answers.append({
				"question": self.questions[self.question_number]["question"],
				"correct_answer": correct_answer
			})
			
			#this is used in case the user wants to retry wrong answers, so it stores 
			#them into question_details
			question_details = {
				"question": self.questions[self.question_number]["question"],
				"options": self.questions[self.question_number]["options"],
				"answer": correct_answer
			}

			#question_details is then stored into incorrect_questions if it does not already
			#contain it
			if question_details not in self.incorrect_questions:
				self.incorrect_questions.append(question_details)

	#used to keep track if the user has reached the end of the questions
	def next_question(self):
		self.question_number += 1
		if self.question_number < len(self.questions):
			self.load_question()
		#if the user has reached the end, then it will display the results
		else:
			self.show_results()

	#this method shows the results to the user
	def show_results(self):
		#this checks if there is anything inside of self.wrong_answers
		if self.wrong_answers:
			wrong_answers_text = "\n".join(
				#this displays the Question (as Q:) and answer (as A:)
				#and uses list comprehension to display it all
				f"Q: {item['question']}\nRight Answer: {item['correct_answer']}"
				#this for loop moves on to the next item in the wrong_answers list 
				for item in self.wrong_answers
			)
		else:
			wrong_answers_text = "All answers were correct!"
			self.next_button.config(state=tk.DISABLED)

		#this is all displayed with a message box that will pop up
		messagebox.showinfo(
			"Quiz Finished",
			f"Your score is {self.score} out of {len(self.questions)}.\n\n"
			f"Right answers for incorrect questions:\n{wrong_answers_text}"
		)
		#this gives the user to retry incorrect questions if there are any by checking
		#in the if statement
		if self.incorrect_questions:
			retry = messagebox.askyesno(title = "CompSci Advancer",
										message = "Do you want to retry incorrect questions?")
			if retry:
				self.questions = self.incorrect_questions
				self.incorrect_questions = [] 
				self.score = 0
				self.question_number = 0
				self.wrong_answers = []
				random.shuffle(self.questions)
				self.load_question()
				#this is used to make the retry window appears above all the other
				#windows, so that the user can interact with it
				self.attributes('-topmost', 1)
				self.attributes('-topmost', 0)
			else:
				self.destroy()
		else:
			self.destroy()

#-----------------------------------------------------------------------------------------------------------------------
#this is the class for exam style questions
class ESQ(Toplevel):
	def __init__(self, file_path):
		super().__init__()
		#the file chosen is the unit the user would like to do
		self.file_path = file_path  
		self.questions = self.load_questions() 
		self.index = 0

		self.title("CompSci Advancer")
		self.geometry("960x720")

		#this is the interface for the exam style questions window
		self.question_label = tk.Label(self, text=self.questions[self.index], wraplength=500, justify="left", font=("Arial", 14))
		self.question_label.pack(pady=20)

		self.answer_text = tk.Text(self, height=10, width=50, wrap="word", font=("Arial", 12))
		self.answer_text.pack(pady=10)
		
		self.next_button = tk.Button(self, text="Next", command=self.next_question)
		self.next_button.pack(pady=10)

		self.sh_answer_btn = tk.Button(self, text="Show answer", command=self.show_answer)
		self.sh_answer_btn.pack(pady=10)

		#these buttons will only appear if the chosen file is esq1 to bring up the figuresthat are
		#used for unit 1 exam style questions 
		if self.file_path == "esq1.txt":
			self.show_figure2_btn = tk.Button(self, text="Show Figure 2", command=self.show_figure2)
			self.show_figure2_btn.pack(pady=10)

			self.show_buyer_btn = tk.Button(self, text="Show Buyer", command=self.show_buyer)
			self.show_buyer_btn.pack(pady=10)
	
	#checks if a file exists and is not empty
	def file_exists(self):
		return os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0

	#this method is for loading the questions
	def load_questions(self):
		#checking if the questions exist in a file from the file_exists function
		if self.file_exists() == False:
			#alerts the user when there are no questions
			print("No existing questions found")
			#this code is used for webscraping, first by opening up chrome and opening up
			#the url to webscrape from. A timer is there to allow the webpage to load properly
			#so that the text can be web scraped properly
			driver = webdriver.Chrome()
			driver.get("https://n95r84.wixsite.com/compsci-advancer")
			time.sleep(5)
			soup = BeautifulSoup(driver.page_source, "html.parser")
			#this selects the class of the text we are looking to webscrape
			questions1 = soup.findAll("span", attrs={"class": "wixui-rich-text__text"})

			#this unique_lines will be used to stop duplicate text from being stored
			unique_lines = []
			#we are using ecnoding utf-8 since some of the characters that we webscrape
			#need utf-8 to be displayed properly
			current_file = open(self.file_path, "w", encoding="utf-8")

			#this is used to filter out questions that are in unit 1 or in unit11
			for question in questions1:
				lines = question.text.splitlines()
				for line in lines:
					#stops duplicate text from being stored
					if line not in unique_lines:
						unique_lines.append(line)
						#once it reaches a different unit, starts storing the questions to a
						#different file
						if "Unit 11" in line:
							current_file.close()
							current_file = open("esq11.txt", "w", encoding="utf-8")
						current_file.write(line + "\n")

			current_file.close()

			driver.quit()
			print("Questions saved to file.")

		with open(self.file_path, "r", encoding="utf-8") as file:
			content = file.read()
		#this seperates each question using the closing sqaure bracket given in the bracket
		#information for the marks (e.g the "]" in [1 mark])
		questions = [segment.strip() + "]" for segment in content.split("]") if segment.strip()]
		return questions

	#this method will get the next question
	def next_question(self):
		#this resets the answer box when the user clicks on next, from 
		#the start at the 1st character all the way to the end of the text
		self.answer_text.delete("1.0", tk.END)
		#this is used to keep track of the question
		self.index += 1
		#comparing the question index to the length of questions
		if self.index < len(self.questions):
			#changing the question text to the next question in index
			self.question_label.config(text=self.questions[self.index])
		else:
			self.question_label.config(text="No more questions.")
			self.next_button.config(state=tk.DISABLED)
			self.sh_answer_btn.config(state= tk.DISABLED)

	#this method is for showing a figure used in unit 1
	def show_figure2(self):
		#we are using a toplevel window to open up the image
		top = Toplevel(self)
		top.title("Figure 2 for Unit 1.1")
		top.geometry("720x540")
		#this is the folder where the image will be stored
		folder_name = "ESQ1_Q_IMG"
		file_num = 1
		image_path = f"{folder_name}/{file_num}.png"

		#this bit of code opens up the image from the folder
		if os.path.exists(image_path):
			image = PhotoImage(file=image_path)
			image_label = tk.Label(top, image=image)
			image_label.image = image
			image_label.pack(pady=20)
	
	#this method is for shwoing a different figure in unit 1, which follows
	#the same code as the one above
	def show_buyer(self):
		top = Toplevel(self)
		top.title("Buyer Figure for Questions 1.2")
		top.geometry("960x720")
		folder_name = "ESQ1_Q_IMG"
		file_num = 2
		image_path = f"{folder_name}/{file_num}.png"

		if os.path.exists(image_path):
			image = PhotoImage(file=image_path)
			image_label = tk.Label(top, image=image)
			image_label.image = image
			image_label.pack(pady=20)

	#this method is used to show the answer for the related question
	def show_answer(self):
		#we will show the answer image in a toplevel window
		top = Toplevel(self)
		top.title("Answer Image")
		top.geometry("960x720")

		#depending on which file the questions are being used, will open up a
		#different file where different answers for different units are stored
		if "esq11" in self.file_path:
			folder_name = "ESQ11" 
		else:
			folder_name = "ESQ1" 

		#the file names are just numbers, so that it is easier to grab the images
		#using the index of the question that relates to the name of the image
		file_num = self.index + 1
		image_path = f"{folder_name}/{file_num}.png"

		#checks if the image exists
		if os.path.exists(image_path):
			image = PhotoImage(file=image_path)
			#this will open the image as a label on the topwindow
			image_label = tk.Label(top, image=image)
			image_label.image = image
			image_label.pack(pady=20)

			#this part of the code adds the users answer along with the mark scheme image answer
			user_answer = tk.Label(top, text="Your answer: " + self.answer_text.get("1.0", tk.END).strip(), font=("Arial", 12), wraplength=500, justify="left")
			user_answer.pack(pady=30)
		else:
			error_label = tk.Label(top, text=f"Image {file_num}.png not found in {folder_name}.", font=("Arial", 14))
			error_label.pack(pady=20)

#-----------------------------------------------------------------------------------------------------------------------
#this class is for the flashcard system
class Flashcard_sys(Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.username = temp_username
		self.title("Flashcard System")
		self.geometry("540x480")

		create_btn = Button(self, text="Create Flashcards", command=self.create_flashcards_window)
		create_btn.pack(pady=10)

		view_btn = Button(self, text="View Flashcards", command=self.view_flashcards_window)
		view_btn.pack(pady=10)

		#This SQL query joins the tables flashcards and user_id, uses count to count number of flashcards
		try:
			sql2 = ("""
			SELECT user_id.name, 
			COUNT(flashcards.flashID) AS num_flashcards
			FROM user_id
			LEFT JOIN flashcards ON user_id.username = flashcards.username
			WHERE user_id.username = %s
			GROUP BY user_id.name
			""")
		except Exception as e:
				print(f"Error: {e}")

		myCursor.execute(sql2, (self.username,))
		#we use the result from counting the number of flashcards that the given username has
		#to inform the user
		result = myCursor.fetchone()

		if result[1] != 0:
			user_name = result[0]
			#stores the number of flashcards found from count
			num_flashcards = result[1]
			#label displaying the information
			flashcard_info = Label(self, text = f"{user_name} has {num_flashcards} flashcards")
			flashcard_info.pack(pady=10)
		else:
			none_found = Label(self, text ="No flashcards found, try creating some")
			none_found.pack(pady=10)

	#this method is used to create the flashcards
	def create_flashcards_window(self):
		create_window = Toplevel(self)
		create_window.title("Create Flashcards")
		create_window.geometry("540x480")

		#creating the variables that will store the question and answer
		question_var = StringVar()
		answer_var = StringVar()

		#using entry labels to collect the users input
		enter_question = Label(create_window, text="Enter Question:")
		enter_question.pack(pady=5)
		question_entry = Entry(create_window, textvariable=question_var, width=50)
		question_entry.pack(pady=5)

		enter_answer = Label(create_window, text="Enter Answer:")
		enter_answer.pack(pady=5)
		answer_entry = Entry(create_window, textvariable=answer_var, width=50)
		answer_entry.pack(pady=5)

		#This method is used within the create flashcards system to store the flashcards
		#each time the save button is clicked
		def save_flashcard():
			#these variables store the questions, answers and username to store into the table
			question = question_var.get()
			answer = answer_var.get()
			username = temp_username

			#checks if the question and answer are empty or not
			if question and answer != "":
				#this SQL query inserts the variables into the table called flashcards
				try:
					myCursor.execute("INSERT INTO flashcards (username, question, answer) VALUES (%s, %s, %s)",
										(username, question, answer))
					mydatabase.commit()
				except Exception as e:
					print(f"Error: {e}")
				messagebox.showinfo("Success", "Flashcard saved successfully!")
				#this resets the entries to empty so that the user can enter again
				question_var.set("")
				answer_var.set("")
			else:
				messagebox.showerror("Empty entries", "Both question and answer are required!")

		save_button = Button(create_window, text="Save", command=save_flashcard)
		save_button.pack(pady=10)

	#this method is used for viewing the flashcards
	def view_flashcards_window(self):
		#creates a seperate window to self
		view_window = Toplevel(self)
		view_window.title("View Flashcards")
		view_window.geometry("540x480")

		question_var = StringVar()
		answer_var = StringVar()

		#these labels will display the text inside of the variables question_var and answer_var
		question_label = Label(view_window, textvariable=question_var, wraplength=350)
		question_label.pack(pady=10)

		answer_label = Label(view_window, textvariable=answer_var, wraplength=350)
		answer_label.pack(pady=10)

		#this function fetches the flashcards from the table flashcards inside the database
		def fetch_flashcards(username):
			#this query only select questions and answers where it has the users username
			try:
				myCursor.execute("SELECT question, answer FROM flashcards WHERE username = %s", (username,))
				return myCursor.fetchall()
			except Exception as e:
				print(f"Error: {e}")

		username = temp_username
		flashcards = fetch_flashcards(username)
		index = [0]

		#this function is used to display the flashcards
		def show_flashcard():
			#this checks if the current index is within the range of
			#flashcards
			if 0 <= index[0] < len(flashcards):
				#access the question and stores it to question_var to display
				question_var.set("Q: " + flashcards[index[0]][0])
				#this resets answer so that the user cannot see the answer straight away without
				#clicking a button to view the answer so that they can recall it
				answer_var.set("")
			else:
				#if the index is out of range, then they have finished all the flashcards
				messagebox.showinfo("Error","No more flashcards available")
				question_var.set("")
				answer_var.set("")
				self.destroy()

		#this function is used if the user wants to display the answer
		def show_answer():
			#checking if the index is within range
			if 0 <= index[0] < len(flashcards):
				#sets answer_var to the answer in flashcards
				answer_var.set("A: " + flashcards[index[0]][1])
			else:
				messagebox.showinfo("Error","No answer available")

		#this gets the next flashcard
		def next_flashcard():
			#checks if it is within range, and if it is the last flashcard, then
			#it will not get the next since there is no next
			if index[0] < len(flashcards) - 1:
				#sets the index to the next one to grab the next set of answers and questions
				index[0] += 1
				#runs the flashcard system to show the next set of questions and answers
				show_flashcard()
			else:
				messagebox.showinfo("Completed","There are no more flashcards, try create some more")
				question_var.set("")
				answer_var.set("")
				self.destroy()

		#these are the buttons used to trigger the functions
		btn1 = Button(view_window, text="View Answer", command=show_answer)
		btn1.pack(pady=10)
		btn2 = Button(view_window, text="Next", command=next_flashcard)
		btn2.pack(pady= 10)

		show_flashcard()
#-----------------------------------------------------------------------------------------------------------------------
#Initialises and creates the class Main
def main():
	Main().mainloop()
if __name__ == "__main__":
	main()