# Binary Search Algorithm in Python

## Project Overview

This project demonstrates how to implement the Binary Search algorithm in Python to efficiently locate a target value in a sorted list. Binary Search is a fundamental algorithm in computer science that significantly improves search performance compared to linear search.

The program takes a sorted list and a target value as input and returns the index of the element if it exists in the list.

## Problem Statement

Searching for an element in large datasets can be slow if done sequentially. Binary Search provides an efficient way to find elements by repeatedly dividing the search interval in half.

This project implements a Python program that searches for a target value in a sorted list using the Binary Search algorithm.

## Technologies Used

Python

Basic algorithms and data structures

### How the Algorithm Works

Binary Search works only on sorted lists.

Steps:

Start with the entire sorted list.

Find the middle element.

Compare the target value with the middle element.

If the target equals the middle element → element found.

If the target is smaller → search the left half.

If the target is larger → search the right half.

Repeat until the element is found or the list is exhausted.

#### Python Implementation
""" def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = [3, 7, 12, 18, 25, 31, 42, 56, 63]

target = int(input("Enter number to search: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
#### Example
Input
Enter number to search: 31
Output
Element found at index 5 """ 

### Time Complexity
Algorithm	Time Complexity
Linear Search	O(n)
Binary Search	O(log n) 

Binary Search is much faster for large datasets because it reduces the search space by half at each step.

### Project Structure
binary-search-python
│
├── binary_search.py
└── README.md


### Skills Demonstrated

This project demonstrates:

Python programming

Algorithm design

Efficient search techniques

Problem-solving skills

Understanding of time complexity

### Why This Project Is Useful

Binary Search is widely used in software development, data structures, and large-scale data processing systems where efficient searching is required.

Understanding this algorithm helps developers write faster and more optimized programs.

### Author

Jumma Mohammad

GitHub:
https://github.com/jumma786

LinkedIn:
https://www.linkedin.com/in/jumma-mohammad/
