'''
Create a module for managing book-related functionalities. This includes classes and functions for book attributes, book availability, and 
any other book-specific operations.
Problem Statement:
The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, price, and stock status.
'''

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def display_info(self):
        
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: $", self.price)
        print("Stock:", self.stock)

    def check_availability(self):
        
        if self.stock > 0:
            print(f"{self.title} is available.")
        else:
            print(f"{self.title} is out of stock.")


def increase_stock(book, quantity):
    
    book.stock += quantity
    print(f"Stock of {book.title} increased by {quantity} units.")

def decrease_stock(book, quantity):
    
    if book.stock >= quantity:
        book.stock -= quantity
        print(f"Stock of {book.title} decreased by {quantity} units.")
    else:
        print(f"Not enough stock of {book.title} to decrease by {quantity} units.")
