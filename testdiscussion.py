# Loops
# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
def even_numbers():
    for x in range(2,21,2):
        print(x)
even_numbers()

# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
def number_greater_than10():
    while True:
        number=int(input("Enter the number greater than 10: "))
        if number>10:
            print("okay")
            break
        else:
            print("Try again.")
number_greater_than10()

# Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
for i in range(1,6):
  for j in range(1,11):
      print(f"{i}x{j}={i*j}\t",end="")
      print()

# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the results.
  numbers = [4, 7, 2, 9, 12, 15]
sum_of_odds = 0

for number in numbers:
    if number % 2 != 0:  # Check if the number is odd
        sum_of_odds += number  # Add the odd number to the sum

print(f"The sum of all odd numbers is: {sum_of_odds}")



# Lists
# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
list_of_5fruits=("apple","mango","avocado","pawpaw","guava")
for v in list_of_5fruits:
   print(v)

# Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def square_numbers(num_list):
    return [num ** 2 for num in num_list]

# Example usage:
result = square_numbers([1, 2, 3])
print(result)  # Output: [1, 4, 9]

# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = []
for i in range(len(list1)):
    combined.append(list1[i])
    combined.append(list2[i])

print(combined)  #  [1, 4, 2, 5, 3, 6]

# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.
numbers = [3, 1, 4, 1, 5, 9, 2]

first = second = float('-inf')

for number in numbers:
    if number > first:
        second = first
        first = number
    elif number > second and number != first:
        second = number

print(f"The two largest numbers are: {first} and {second}")

# Dictionaries
# Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
students_information={
    "name":"Ampurire",
    "age":22,
    "grade":"A"}
for key,value in students_information.items():
 print(key,value)

# Intermediate: Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def get_adult_names(people):
    return [name for name, age in people.items() if age >= 21]

# Example
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
adult_names = get_adult_names(people)
print(adult_names)  #  ['Alice', 'Charlie']

# Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
store_items = {
    'apple': 0.5,
    'banana': 0.3,
    'orange': 0.7
}

items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = sum(store_items[item] for item in items_bought)

print(f"The total cost is: ${total_cost:.2f}")

# Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

sentence = "hello world hello"
result = count_words(sentence)
print(result)  #  {'hello': 2, 'world': 1}

# Object-Oriented Programming (OOP)
# Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car('Toyota', 'Red')
print(f"Brand: {my_car.brand}, Color: {my_car.color}")
# Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("The engine has started.")

my_car = Car('Toyota', 'Red')
my_car.start_engine()  # Output: The engine has started.

# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def print_balance(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount('123456789')
account.deposit(100)
account.withdraw(50)
account.print_balance()  # Output: Current balance: $50



# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{title}'.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned '{title}'.")
                return
        print(f"'{title}' was not borrowed.")

# Example usage
library = Library()
book1 = Book('1984', 'George Orwell')
library.add_book(book1)
library.borrow_book('1984')
library.return_book('1984')
