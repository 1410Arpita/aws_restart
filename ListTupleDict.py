'Working with Lists, Tuples, and Dictionaries'
'''In Python, string and numeric data types are often used 
in groups called collections. 
Three such collections that Python supports 
are the list, the tuple, and the dictionary.'''

'Exercise 1: Introducing the list data type'

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

'Accessing a list by position'
print(myFruitList[2])

'Changing the values in a list'
myFruitList[2] = "orange"
print(myFruitList)


'Exercise 2: Introducing the tuple data type'
'''Defining a tuple
The tuple is like a list, but it can't be changed. 
A data type that can't be changed after it's created is said to be immutable. 
define a tuple, you use parentheses instead of brackets ([]).'''

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

'Accessing a tuple by position'

print(myFinalAnswerTuple[1])


'Exercise 3: Introducing the dictionary data type'

'''Defining a dictionary
A dictionary is a list with named positions (keys). 
Imagine that your list shows people’s favorite fruit.'''

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))


'Accessing a dictionary by name'
print(myFavoriteFruitDictionary["Saanvi"])





