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
        for id in bookIds:
            self.books.append(Book(id, score[id]))
        books.sort(key=lambda x:x.score, reverse=True)

books = []
libraries = []
shippedBookIds = []
result = [] # containing library objects
       
[num_books, num_libs, days] = list(map(int, input().split()))

books_score = list(map(int, input().split()))

for i in range(0, num_libs):
    [num_books, signup_days, shipment_days] = list(map(int, input().split()))
    bookIds = list(map(int, input().split()))
    libraries.append(Library(i, num_books, signup_days, shipment_days, bookIds, books_score))
    
for j in range(0, len(books_score)):
    books.append(Book(j, books_score[j]))
    
sortedBooks = sorted(books, key=lambda x:x.score, reverse=True)

temp_days = 0

for book in sortedBooks:
    if book.id not in shippedBookIds:
        libs = [lib for lib in libraries if book.id in lib.bookIds]
        book_lib = libs[0]
        if len(libs) > 1:
            book_lib = min(libs, key=lambda l:l.signup_days)
        signup_days = book_lib.signup_days - temp_days
        if signup_days > 0:
            days -= signup_days
            temp_days = 0
        else:
            temp_days = temp_days - book_lib.signup_days
        days += temp_days
        book_lib.isSignedUp = True
        num_days = book_lib.num_books/book_lib.shipment_days
        if math.ceil(num_days) > days:
            num_days = days
        temp_days += math.ceil(num_days)
        not_shipped_books = [b.id for b in book_lib.books if b.id not in shippedBookIds]
        book_lib.booksShipped = not_shipped_books[0:int(num_days*book_lib.shipment_days)]
        shippedBookIds.extend(book_lib.booksShipped)
        if (len(book_lib.booksShipped)):
            result.append(book_lib)
        
    
print(len(result))
for lib in result:
    print(lib.id, " ", len(lib.booksShipped))
    for id in lib.booksShipped:
        print(id, end=' ')
    print()




        