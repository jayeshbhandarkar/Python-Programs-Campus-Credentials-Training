"""
2. Find the Second Largest Element:
    ○ Question: Find the second largest element in an array.
    ○ Logic: Initialize two variables to store the largest and second-largest
    elements and iterate through the array.
    ○ Sample Input: [7, 3, 9, 2, 8]
    ○ Expected Output: Second Largest: 8
"""

arr = [7, 3, 9, 2, 8]

def find_second_large(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    
    largest = sec_largest = float('-111') 
    
    for num in arr:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num
    
    return sec_largest

sec_largest = find_second_large(arr)
print(f"Second Largest: {sec_largest}")
