"""
1. Find the Maximum and Minimum Elements:
    ○ Question: Write a function to find the maximum and minimum
    elements in an array.
    ○ Logic: Iterate through the array, updating the maximum and minimum
    as you go.
    ○ Sample Input: [5, 3, 9, 2, 8]
    ○ Expected Output: Maximum: 9, Minimum: 2
"""

arr = [5, 3, 9, 2, 8]

def find_min_max(arr):
    
    min_no = arr[0]
    max_no = arr[0]

    for num in arr:
        if num < min_no:
            min_no = num
        elif num > max_no:
            max_no = num

    print("Maximum = ", max_no, " Minimum = ", min_no)
    return min_no, max_no

find_min_max(arr)     