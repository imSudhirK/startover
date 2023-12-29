#!/usr/bin/python3

# python is open source programming language 

# convention
    #Class, __strongly, _private, special__, identifiers

# blocks of codes are denoted by line identation

'''
statements contained within [], {}, () brackets do not need to 
use line continuation character '\'
'''

# ('), ("), (''' or """) quotes used to denote string literals 
# where triples quotes are used to span string across multiple lines

input("\nPress Enter to exit.")

# (;) semicolon allows multi statement in single line unless
# statement starts new code block

# multi assigment 
a = b = c = 1   # single object is assigned to multi vars simultaneously
p, q, r = 1, 2, "pqr" # multi vars multi objets assigment

del a, q    # deleting  objects

# python have five standard data types 
    # numbers, string, list, tuple, dictionary

# python supports three numerical types
    # int, float, complex

# Strings 
str = 'Hello World'
str0 = str[0]; str1 = str[1:5]; str2 = str[3:]
str3 = str*3; str4= str + " Four"

# Lists -  items can be of different datatype 
lst = ['abcd', 123, 3.21]
lst0 = lst[0]; lst1 = lst[1:3]; lst2 = lst *2
lst3 = lst + lst; lst4 = lst[-1]

# tuples - same as list but can't be updated
tple = ('abcd', 1234, 3.21)
tple0 = tple[0]; tple1 = tple[1:3]; tple3 = tple[-1]
tple4 = tple * 2; tple5 = tple + tple
# tple[0] = 'updated value'


# Dictionary - {key: value} pair
dict = {'name': 'john', 'code': 123}
dict[2] = 'this is two'; dict1 = dict
# print(dict.keys()); print(dict.values())

# Arithmetic operator: +, -, *, /, 
# % modulus, ** expo, // floor division
# Logical operator: and, or, not
# Comparison operator: ==, !=, >, <, >=, <=
# Assignment operator: =, +=, -=, *=, /=, %=, **=, //=
# Bitwise operator:  binary
# & and, | or, ^ xor, ~ 1's compliment, 
# << left shift, >> right shift
# Membership operator: in, not in
# Identity operator: is, not is, -----compares memory

# Decision making
# python assumes non-zero, non-null values TRUE
# and zero or null values FALSE

# IF statement 
# if expression1:
#     statements
# elif expression2:
#     statements
#     if expr3:
#         stmts
#     if expr4:
#         stmts
# else:
#     statements

# single line suite clause of if could be in-line


# LOOPS
# while expression:
#     statements
# else:
#     statements

# for iter in sequence:
#     statements
#     break
# else:
#     statements


# NUMBERS
print("abs(-100.23) =", abs( -100.23))
print("max(1,8,4,7,2) =", max(1,8,4,7,2))
print("min(8,4,1,7,2) =", min(8,4,1,7,2))
print("pow(2, 6) =", pow(2, 6))


from math import ceil, floor, sqrt
print("floor(-100.23) =", floor( -100.23))
print("ceil(-100.23) =", ceil( -100.23))
print("sqrt(64) =", sqrt(64))


from math import exp, log, log10
print("exp(1) =", exp(1))
print("log(9) =", log(9))
print("log10(1000) =", log10(1000))


from random import choice, random, randrange
print("random number in range(100) =", choice(range(100)))
print("random odd number between 1-100 =", randrange(1, 100, 2))
print("random number between 0-99 =", randrange(100))
print("random float number between 0-1 =", random())

from random import seed, uniform, shuffle
print("uniform(1, 10) =", uniform(1, 10))
lst = [1,2,3,4,5,6]; shuffle(lst); print("shuffle(lst) =", lst)
seed(); print("default seed random num =", random())
seed(10); print("seed(10) random number =", random())

#STRINGS
str = 'Hello World'
print('len(str) =',  len(str))
print('str.lower() =', str.lower())
print('str.upper() =', str.upper())
print('str.issapce()=', str.isspace())
print('str.isalpha() =', str.isalpha())
print('str.isalnum() =', str.isalnum())
print('str.isdigit() =', str.isdigit())
print('str.islower() =', str.islower())
print('str.isupper() =', str.isupper())

#LISTS
list = ['item1', 123, 32.1, 'lastitem']
print('list =', list)
print('len(list) =', len(list))
print('list[0] =', list[0])
print('list[-1] =', list[-1])
print('list[:3] =', list[:3])
print('list[1:] =', list[1:])
print('list[1:3] =', list[1:3])
list[2] = 222; print('updating list[2] =', list)
del list[2]; print('deleting list[2] =', list)

list = [3, 7, 4, 1, 9, 2, 3]
print('list=', list)
print('max(list) =', max(list))
print('min(list) =', min(list))

lst0 = list[:3]; lst1 = list[4:]
lst0.append(4); print('lst0.append(4) =', lst0)
print('lst0.count(4) =', lst0.count(4))
lst0.extend(lst1); print('lst0.extend(lst1); lst0 =', lst0)
print('min index of 4 in list =',lst0.index(4))
lst0.insert(2, 9); print('lst0.insert(2, 9); lst0 =', lst0)
lst0.pop(2); print('lst0.pop(2); lst0 =', lst0)
lst0.remove(4); print('lst0.remove(4); lst0 =', lst0)
lst0.reverse(); print('lst0.reverse(); lst0 =', lst0)
lst0.sort(); print('lst0.sort(); lst0 =', lst0)

#TUPLES
tup = ('python', 'cplus')
tup0 = (123, 4.56)
tup += tup0; print("tup += tup0 :=", tup)

print("len(tup) =", len(tup))
print("min(tup0) =", min(tup0))
print("max(tup0) =", max(tup0))
print("tuple([1,2,3,4]) =", tuple([1,2,3,4]))

#DICTIONARY
dict = {"name": "zara", 'age': 7.5, 'class': 2}
print(dict)
print(dict['name'])
dict['age'] = 8; print(dict['age'])
dict['school'] = 'agps'
# dict.clear(); print(dict) ; del dict; print(dict)
print("len(dict) =", len(dict))
# del dict['name'] ; print(dict['name'])

# dictionary values have no restrictions 
# no duplicate key are allowed 
# key must be immutable 

sequence = ('name', 'age', 'sex')
dict0 = dict.fromkeys(sequence);print(dict0)
dict0 = dict.fromkeys(sequence, 10); print(dict0)

dict = { 'name': "zara", "age": 27}
print("dict.get('age') =", dict.get("age"))
print("dict.get('school', 'none') =", dict.get("school", "none"))
print("'age' in dict =", "age" in dict)
print("'sex' in dict =", "sex" in dict)

print(dict.items())
print(dict.values())
print(dict.keys())
dict2 = { "sex": "female"}
dict.update(dict2)
print(dict)