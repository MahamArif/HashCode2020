# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:03:54 2020

@author: maham
"""
import math

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        
class Library:
    isSignedUp = False
    booksShipped = []
    books = []
    
    def __init__(self, id, num_books, signup_days, shipment_days, bookIds, score):
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
    [num_books_lib, signup_days, shipment_days] = list(map(int, input().split()))
    bookIds = list(map(int, input().split()))
    libraries.append(Library(i, num_books_lib, signup_days, shipment_days, bookIds, books_score))
    
for j in range(0, len(books_score)):
    books.append(Book(j, books_score[j]))

libraries.sort(key=lambda x:x.signup_days)

temp_days = 0

for lib in libraries:
    books = [bookId for bookId in lib.bookIds if bookId <= num_books]
    if (len(books)) and days > 0:
        signup_days = lib.signup_days - temp_days
        if signup_days > 0:
            days -= signup_days
            temp_days = 0
        else:
            temp_days = temp_days - lib.signup_days
        days += temp_days
        num_days = lib.num_books/lib.shipment_days
        if math.ceil(num_days) > days:
            num_days = days
        temp_days += math.ceil(num_days)
        lib.booksShipped = books[0:int(num_days*lib.shipment_days)]
        shippedBookIds.extend(lib.booksShipped)
        if (len(lib.booksShipped)):
            result.append(lib)  
    
print(len(result))
for lib in result:
    print(lib.id, " ", len(lib.booksShipped))
    for id in lib.booksShipped:
        print(id, end=' ')
    print()
