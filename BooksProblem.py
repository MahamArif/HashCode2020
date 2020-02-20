# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:03:54 2020

@author: maham
"""

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        
class Library:
    isSignedUp = False
    booksShipped = []
    
    def __init__(self, id, num_books, signup_days, shipment_days, bookIds):
        self.id = id
        self.num_books = num_books
        self.signup_days = signup_days
        self.shipment_days = shipment_days
        self.bookIds = bookIds

books = []
libraries = []
shippedBookIds = []
result = [] # containing library objects
       
[num_books, num_libs, days] = list(map(int, input().split()))

books_score = list(map(int, input().split()))

for i in range(0, num_libs):
    [num_books, signup_days, shipment_days] = list(map(int, input().split()))
    bookIds = list(map(int, input().split()))
    libraries.append(Library(i, num_books, signup_days, shipment_days, bookIds))
    
for j in range(0, len(books_score)):
    books.append(Book(j, books_score[j]))
    
print(len(result))
for lib in result:
    print(lib.id, " ", len(lib.booksShipped))
    for id in lib.booksShipped:
        print(id, end=' ')




        