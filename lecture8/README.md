# Lecture 8 – Object-Oriented Programming (OOP)

## Overview
This lecture introduced the fundamentals of Object-Oriented Programming (OOP) in Python. Instead of writing programs as collections of functions, OOP organizes code into classes that represent real-world objects, each with their own data (attributes) and behaviour (methods). The lecture also covered encapsulation, properties, special methods, exception handling, and working with third-party libraries.

---

# What I Learned

## Classes and Objects
- Creating classes with `class`
- Creating objects (instances)
- Understanding instance variables
- Using `self`
- Initializing objects with `__init__`

## Instance Methods
- Defining methods inside classes
- Modifying an object's internal state
- Calling methods on objects

## Encapsulation
- Keeping data private using naming conventions
- Accessing data through methods instead of directly
- Protecting object state from invalid modifications

## Properties
- Using the `@property` decorator
- Creating getter methods
- Controlling access to instance variables

## Special (Magic) Methods
- `__init__`
- `__str__`
- Understanding how Python automatically calls special methods

## Exception Handling
- Raising `ValueError`
- Validating object state
- Defensive programming inside classes

## External Libraries
- Using `num2words`
- Creating PDF documents with `fpdf2`

---

# Exercises Completed

## Seasons of Love
### Description
Created a program that:
- Accepts a user's date of birth
- Calculates the total number of minutes lived
- Converts the result into English words using `num2words`

### Concepts Used
- `datetime`
- Date arithmetic
- Exception handling
- External libraries

---

## Cookie Jar

### Description
Implemented a `Jar` class featuring:
- Configurable capacity
- Cookie deposits
- Cookie withdrawals
- Capacity and size properties
- String representation using cookie emojis

### Concepts Used
- Classes
- Objects
- Instance variables
- `__init__`
- `__str__`
- `@property`
- Raising exceptions

---

## CS50 Shirtificate

### Description
Created a personalised PDF certificate containing:
- A title
- A shirt image
- The user's name printed on the shirt

### Concepts Used
- `fpdf2`
- Images
- Text positioning
- Fonts
- Colours
- PDF generation

