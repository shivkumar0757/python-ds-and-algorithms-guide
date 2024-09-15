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
integer = 5                #int
float_number = 5.0         #float
string = "Hello"           #str   : immutable
list_example = [1, 2, 3]   #list  : mutable
tuple_example = (1, 2, 3)  #tuple : immutable
set_example = {1, 2, 3}    #set   : unordered, unique elements
dictionary_example = {"a": 1, "b": 2}  #dict : key-value pairs
```

### Control Structures

- **If-Else Statements:**

```python
if x > 0:  # checking if x is positive
elif x < 0:  # checking if x is negative
else:  # if x is zero

# Ternary Operator
result = "val1" if True else "val2" 
```

- **Loops:**

```python
# For Loop
for i in range(5): pass  # prints numbers 0 to 4
for i in reversed(range(5)): pass  # prints numbers 4 to 0
for i in range(4, -1, -1): pass # prints numbers 4 to 0
for num in arr: pass  # iterate over elements in an array
for index, num in enumerate(arr):  # iterate with index
    print(index, num)
    
#single line for loop
squared_list = [x**2 for x in range(5)]  # squared_list is [0, 1, 4, 9, 16]

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

# sort object using attrgetter
from operator import attrgetter
sorted_students = sorted(students, key=attrgetter('grade', 'age'), reverse=True)
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
my_list.extend([7, 8])  # my_list is now [4, 5, 6, 7, 8]

# Remove and return last element
last_element = my_list.pop()  # complexity O(1) (average case, else can be O(n) if resizing is needed)

#combine list uisng plus operator
combined_list = my_list + [9, 10]  # combined_list is [4, 5, 6, 7, 8, 9, 10]

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
Tuples are a fundamental data structure in Python that allows for the storage of an ordered collection of elements. They are similar to lists but have some key differences, primarily that tuples are immutable, meaning once a tuple is created, its elements cannot be changed, added, or removed.

## Initialization of Tuples

**Syntax:**
```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
sample_tuple = (1, 2, 3)

# Tuple without parentheses (not recommended for readability)
sample_tuple2 = 1, 2, 3

# Single element tuple (note the comma)
single_element_tuple = (1,)
```

- **Common Methods:**
```python
# Accessing Elements
sample_tuple = (10, 20, 30, 40)
first_element = sample_tuple[0]  # first_element is 10
last_element = sample_tuple[-1]  # last_element is 40

# Slicing
sample_tuple = (10, 20, 30, 40, 50)
sliced_tuple = sample_tuple[1:4]  # sliced_tuple is (20, 30, 40)

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2  # concatenated_tuple is (1, 2, 3, 4)

# Iterating Through a Tuple
sample_tuple = (10, 20, 30)
for element in sample_tuple:
    print(element)  # prints 10, 20, 30

# Finding Length
sample_tuple = (10, 20, 30, 40)
tuple_length = len(sample_tuple)  # tuple_length is 4

# Tuple Membership
sample_tuple = (10, 20, 30, 40)
is_present = 20 in sample_tuple  # is_present is True
```


### Sets
Sets are an unordered collection data type that is iterable, mutable, and has no duplicate elements. They are commonly used for membership testing and eliminating duplicate entries.

## Initialization of Sets

**Syntax:**
```python
# Empty set
empty_set = set()

# Set with elements
sample_set = {1, 2, 3}

# Using the set() function with a list
sample_set2 = set([1, 2, 3])
```



### Dictionaries
Dictionaries are a fundamental data structure in Python that allows for the storage of key-value pairs. They are mutable, unordered collections, and each key must be unique.

## Initialization of Dictionaries

**Syntax:**
```python
# Empty dictionary
empty_dict = {}

# Dictionary with elements
sample_dict = {"key1": "value1", "key2": "value2"}

# Using the dict() function
sample_dict2 = dict(key1="value1", key2="value2")
```

- **Common Methods:**
```python
# Adding or Updating Elements
sample_dict = dict(key1="value1", key2="value2")
sample_dict["key2"] = "value2"  # sample_dict is now {"key1": "value1", "key2": "value2"}

# Removing Elements
del sample_dict["key2"]  # sample_dict is now {"key1": "value1"}
value = sample_dict.pop("key1")  # sample_dict is now {}, value is "value1"

# Accessing Elements
value1 = sample_dict["key1"]  # value1 is "value1"
value2 = sample_dict.get("key3", "default_value")  # value2 is "default_value"

# Iterating Through a Dictionary
for key in sample_dict:
    print(key, sample_dict[key])  # prints keys and values
    
for key, value in sample_dict.items():
    print(key, value)  # prints keys and values

# Checking Membership
is_present = "key1" in sample_dict  # is_present is True

# Finding Length
dict_length = len(sample_dict)  # returns the number of key-value pairs in the dictionary (2 in this case)
```


**Default Dictionary**

```python
from collections import defaultdict

# Creating a defaultdict with list as the default factory
default_dict = defaultdict(list)

# Creating a defaultdict with int as the default factory
count_dict = defaultdict(int)

# Creating a defaultdict with a custom function
default_dict_custom = defaultdict(lambda : "default_value")
```

- **Common Methods:**
```python
# Adding or Updating Elements
sample_dict = {"key1": "value1"}
sample_dict["key2"] = "value2"  # sample_dict is now {"key1": "value1", "key2": "value2"}
sample_dict["key1"] = "updated_value1"  # sample_dict is now {"key1": "updated_value1", "key2": "value2"}

# Removing Elements
sample_dict = {"key1": "value1", "key2": "value2"}
del sample_dict["key2"]  # sample_dict is now {"key1": "value1"}
value = sample_dict.pop("key1")  # sample_dict is now {}, value is "value1"

# Accessing Elements
sample_dict = {"key1": "value1", "key2": "value2"}
value1 = sample_dict["key1"]  # value1 is "value1"
value2 = sample_dict.get("key3", "default_value")  # value2 is "default_value"

# Iterating Through a Dictionary
sample_dict = {"key1": "value1", "key2": "value2"}
for key in sample_dict:
    print(key, sample_dict[key])  # prints keys and values
for key, value in sample_dict.items():
    print(key, value)  # prints keys and values

# Checking Membership
sample_dict = {"key1": "value1", "key2": "value2"}
is_present = "key1" in sample_dict  # is_present is True

# Finding Length
sample_dict = {"key1": "value1", "key2": "value2"}
dict_length = len(sample_dict)  # dict_length is 2

  ```
  
### Strings
Strings are a fundamental data type in Python that represent sequences of characters. They are immutable, meaning their elements cannot be changed after creation.

```python
# Ways to Initialize a string
my_string = "Hello, World!"
my_string = str(123)  # Convert an integer to a string
# loop through string
for char in my_string:
    print(char)
# character ascii
ascii_value = ord('a')  # ascii_value is 97
char = chr(97)  # char is 'a'

# format string
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."  # Using f-strings
formatted_string = "My name is {} and I am {} years old.".format(name, age)  # Using format method

escaped_string = "He said, \"Hello, World!\""  # Use backslash to escape quotes

# String Methods like upp
upper_case = my_string.upper()  # upper_case is "HELLO, WORLD!"
lower_case = my_string.lower()  # lower_case is "hello, world!"
```

## Advanced Data Structures

### Arrays
Arrays we can refer to list options, which are dynamic arrays.
**Sorted Containers**
The three most commonly used sorted data structures provided by the sortedcontainers module are:

1. SortedList
2. SortedDict
3. SortedSet

```python
# A SortedList is a list that maintains its elements in sorted order.
from sortedcontainers import SortedList

# Creating an empty SortedList
sorted_list = SortedList()

# Creating a SortedList with initial elements
sorted_list_with_elements = SortedList([4, 1, 5, 2])

# add and removee element
sorted_list = SortedList([3, 1, 4])
sorted_list.add(2)  # sorted_list is now [1, 2, 3, 4]

sorted_list = SortedList([1, 2, 3, 4])
sorted_list.remove(2)  # sorted_list is now [1, 3, 4]

# find and remove multiple or list
sorted_list.discard(2)  
sorted_list.index(3)  # returns the index of 3 in the list (2 in this case)
# union, intersection, difference

union = sorted_list | sorted_list2  # union is [1, 2, 3, 4, 5]
intersection = sorted_list & sorted_list2  # intersection is [3]
difference = sorted_list - sorted_list2  # difference is [1, 2]

```

### Sorted Dictionary

```python
# A SortedDict is a dictionary-like structure that maintains its keys in sorted order.
from sortedcontainers import SortedDict

# Creating an empty SortedDict
sorted_dict = SortedDict()

# Creating a SortedDict with initial elements
sorted_dict_with_elements = SortedDict({"b": 2, "a": 1, "c": 3})

# Same operation as normal dictionary
for key in sorted_dict:
    print(key, sorted_dict[key])  # prints keys in sorted order

```
###  SortedSet
```python
from sortedcontainers import SortedSet

# Creating an empty SortedSet
sorted_set = SortedSet()

# Creating a SortedSet with initial elements
sorted_set_with_elements = SortedSet([4, 1, 5, 2])

#Iterating Through a SortedSet
for element in sorted_set:
    print(element)  # prints 1, 3, 4 in order

```

### Bisect module
The bisect module in Python provides support for maintaining a sorted list in sorted order without having to sort the list repeatedly. It provides functions to insert elements into a list while maintaining its sorted order and to find the position where elements should be inserted.

```python
import bisect

# Initialize a sorted list
sorted_list = [1, 3, 4, 4, 7]

# Find the insertion point for 4 using bisect_left (inserts before any existing 4)
left_index = bisect.bisect_left(sorted_list, 4)
print(f"Insertion point for 4 using bisect_left: {left_index}")  # Output: 2

# Find the insertion point for 4 using bisect_right (inserts after any existing 4)
right_index = bisect.bisect_right(sorted_list, 4)
print(f"Insertion point for 4 using bisect_right: {right_index}")  # Output: 4

# Insert 4 into the sorted list at the position returned by bisect_left
bisect.insort_left(sorted_list, 4)
print(f"List after inserting 4 using insort_left: {sorted_list}")  # Output: [1, 3, 4, 4, 4, 7]

# Insert 4 into the sorted list at the position returned by bisect_right
bisect.insort_right(sorted_list, 4)
print(f"List after inserting 4 using insort_right: {sorted_list}")  # Output: [1, 3, 4, 4, 4, 4, 7]

# Using bisect_left to find the index to insert 5 to maintain sorted order
index_for_5 = bisect.bisect_left(sorted_list, 5)
print(f"Insertion point for 5 using bisect_left: {index_for_5}")  # Output: 6

# Using insort_right to insert 5 in the sorted list
bisect.insort_right(sorted_list, 5)
print(f"List after inserting 5 using insort_right: {sorted_list}")  # Output: [1, 3, 4, 4, 4, 4, 5, 7]

```

## Linked Lists
Python does not have a built-in linked list data structure, so we typically implement linked lists using classes. There are three main types of linked lists:

Singly Linked List: Each node points to the next node.
Doubly Linked List: Each node points to both the next and the previous node.
Circular Linked List: The last node points back to the first node, forming a circle.

**1. Singly Linked List**
A Singly Linked List is a collection of nodes where each node has two parts:

Data: The value stored in the node.
Next: A pointer/reference to the next node in the list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

```

**2. Doubly Linked List**
A Doubly Linked List is a linked list where each node has three parts:

Data: The value stored in the node.
Prev: A pointer/reference to the previous node.
Next: A pointer/reference to the next node.

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        if current:
            self.head = current.prev

```

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

*Common patterns*
1. Fibonacci Pattern: Climbing Stairs

*Identification*: 
If a problem asks for the number of ways to reach a target (like climbing stairs), or combinations involving two choices (1 or 2 steps), it often follows a Fibonacci pattern.

*Template*:
```python
def climb_stairs(n):
    if n <= 2:  # Base case
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

```

2. Knapsack Pattern: 0/1 Knapsack
- Identification: If a problem involves making decisions to maximize or minimize a value with given constraints (like capacity), it follows the Knapsack pattern.
- Template:

```python
def knapsack_recursive(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack_recursive(wt, val, W, n-1)
    return max(val[n-1] + knapsack_recursive(wt, val, W-wt[n-1], n-1), knapsack_recursive(wt, val, W, n-1))
```
3. Minimum Path Sum

Given an m x n grid filled with non-negative numbers, find a path from the top left to the bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.
```python
def dp_recursive(parameters, memo):
    # Base case check
    if base_condition:
        return base_result

    # Check memo dictionary for precomputed results
    if parameters in memo:
        return memo[parameters]

    # Compute result recursively
    result = recursive_logic(parameters)

    # Store result in memo dictionary
    memo[parameters] = result

    return result

def solve_problem():
    # Initialize memo dictionary
    memo = {}
    # Call recursive function with initial parameters
    return dp_recursive(initial_parameters, memo)

```
4. Given two strings text1 and text2, find the length of their longest common subsequence.

- Identification: If the problem involves comparing two sequences to find the longest or shortest subsequence or common pattern, it usually follows the LCS pattern.
- Template:
```python
def lcs_template(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

```

5.  Partitioning Problems Pattern: Word Break Problem
-   Given a string s and a dictionary of words wordDict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
- Identification: When the problem requires partitioning a sequence into valid parts based on a set of rules (like dictionary words or palindromes).
- Template:
```python
def word_break_recursive(s, wordDict, start, memo):
    # Base case: reached the end of the string
    if start == len(s):
        return True

    # Check if result is already computed
    if start in memo:
        return memo[start]

    # Try to partition the string
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in wordDict and word_break_recursive(s, wordDict, end, memo):
            memo[start] = True
            return True

    # If no valid partition is found
    memo[start] = False
    return False

def word_break(s, wordDict):
    memo = {}
    return word_break_recursive(s, wordDict, 0, memo)
```



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
