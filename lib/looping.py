#!/usr/bin/env python3

def happy_new_year(): 
     happy_new_year = ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
     for i in range(10, 0, -1):
         print(i)
     print('Happy New Year!') #loops
happy_new_year()

def square_integers(int_list):
    return [i**2 for i in int_list]
int_list = [1, 2, 3, 4, 5]
squared_list = square_integers(int_list)
print(squared_list) #squarelist

def fizzbuzz():
     for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()