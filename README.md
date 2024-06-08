# Python Data Structures and Algorithms Guide

## Goal

This guide aims to provide a comprehensive overview of Python basics, data structures, and algorithms, organized in a single file for easy and quick revision. It is designed to help you prepare efficiently for coding challenges and technical interviews.

## Table of Contents

1. [Python Basics](#python-basics)
   - [Syntax and Variables](#syntax-and-variables)
   - [Data Types](#data-types)
   - [Control Structures](#control-structures)
   - [Functions and Modules](#functions-and-modules)
2. [Basic Data Structures](#basic-data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Sets](#sets)
   - [Dictionaries](#dictionaries)
3. [Advanced Data Structures](#advanced-data-structures)
   - [Arrays](#arrays)
   - [Linked Lists](#linked-lists)
   - [Stacks](#stacks)
   - [Queues](#queues)
   - [Trees](#trees)
   - [Graphs](#graphs)
   - [Heaps](#heaps)
   - [Hash Tables](#hash-tables)
4. [Common Algorithms](#common-algorithms)
   - [Sorting Algorithms](#sorting-algorithms)
   - [Searching Algorithms](#searching-algorithms)
   - [Dynamic Programming](#dynamic-programming)
   - [Graph Algorithms](#graph-algorithms)
5. [Interview Tips](#interview-tips)

## Python Basics
### Data Types

```python
integer = 5
float_number = 5.0
string = "Hello"
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
set_example = {1, 2, 3}
dictionary_example = {"a": 1, "b": 2}
```

### Control Structures

- **If-Else Statements:**

```python
if x > 0:  # checking if x is positive
elif x < 0:  # checking if x is negative
else:  # if x is zero
```

- **Loops:**

```python
# For Loop
for i in range(5):  # prints numbers 0 to 4
for i in reversed(range(5)):  # prints numbers 4 to 0
for i in range(4, -1, -1):  # prints numbers 4 to 0
for num in arr:  # iterate over elements in an array
for index, num in enumerate(arr):  # iterate with index
    print(index, num)

# Using break and continue
for i in range(10):  
    if i == 5:
        break  # exits the loop when i is 5
    print(i)  # prints 0 to 4

for i in range(10):
    if i % 2 == 0:
        continue  # skips the rest of the loop for even i
    print(i)  # prints odd numbers from 1 to 9

# While Loop
i = 0
while i < 5:  # prints numbers 0 to 4
    print(i)
    i += 1
```



### Functions and Modules

- **Functions:**

```python
def calculate_sum(a, b):  # Define a function to calculate sum
    return a + b

# Lambda functions: small anonymous functions defined with the lambda keyword
# Example: lambda input: output
multiply = lambda x, y: x * y  # Multiplies two numbers
result = multiply(2, 3)  # result is 6
# Example: Lambda function for quick sorting
sorted_arr = sorted(arr, key=lambda x: x[1])  # Sorts array of tuples based on the second element

```

- **Modules:**

```python
import heapq  # Importing heapq module for heap operations
import collections  # Importing collections module for deque

# Creating objects of heap and deque (operations shown later)
min_heap = []
heapq.heappush(min_heap, 3)  # Pushes 3 into the heap
queue = collections.deque()  # Creating a deque using package name, for better readabilty
```


## Basic Data Structures

### Lists

- **Initialization:**

```python
# Initialize an empty list
my_list = []

# Initialize a list with elements
my_list = [1, 2, 3, 4, 5]
```

- **Common Operations:**

```python
# Append an element to the end of the list
my_list.append(6)  # my_list is now [1, 2, 3, 4, 5, 6]

# Insert an element at a specific position
my_list.insert(2, 10)  # my_list is now [1, 2, 10, 3, 4, 5, 6]

# Remove an element from the list
my_list.remove(10)  # my_list is now [1, 2, 3, 4, 5, 6]

# Access elements by index
first_element = my_list[0]  # first_element is 1
last_element = my_list[-1]  # last_element is 6

# Iterate over a list
for element in my_list:
    print(element)  # prints each element in my_list

# List comprehension
squared_list = [x**2 for x in my_list]  # squared_list is [1, 4, 9, 16, 25, 36]
```

- **Slicing:**

```python
# Slicing a list (1 is inclusive, 4 is exclusive indexes)
sub_list = my_list[1:4]  # sub_list is [2, 3, 4]
```

- **Common Methods:**

```python
# Extend list by appending elements from another list
my_list.extend([7, 8])  # my_list is now [1, 2, 3, 4, 5, 6, 7, 8]

# Get the index of an element
index_of_four = my_list.index(4)  # index_of_four is 3

# Count occurrences of an element
count_of_two = my_list.count(2)  # count_of_two is 1

# Sort the list
my_list.sort()  # my_list is now [1, 2, 3, 4, 5, 6, 7, 8]

# Reverse the list
my_list.reverse()  # my_list is now [8, 7, 6, 5, 4, 3, 2, 1]
```


### Tuples

### Sets

### Dictionaries

## Advanced Data Structures

### Arrays

### Linked Lists

### Stacks

### Queues

### Trees

### Graphs

### Heaps

### Hash Tables

## Common Algorithms

### Sorting Algorithms

### Searching Algorithms

### Dynamic Programming

### Graph Algorithms

## Interview Tips

- **Strategies for Approaching Problems:** Break down the problem, understand the requirements, and think about the most efficient solution.
- **Common Patterns:** Sliding window, two pointers, recursion, backtracking, etc.
- **Optimizing Solutions:** Focus on reducing time and space complexity, and consider edge cases.
- **Practice Problems:** LeetCode problems categorized by difficulty and type.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [GeeksforGeeks Data Structures](https://www.geeksforgeeks.org/data-structures/)
- [LeetCode](https://leetcode.com/)
