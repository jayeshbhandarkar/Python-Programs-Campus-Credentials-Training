"""
3. Remove Duplicates from Unsorted Array:
    ○ Question: Write a function to remove duplicates from an unsorted
    array.
    ○ Logic: Use a hash set to keep track of unique elements as you iterate
    through the array.
    ○ Sample Input: [3, 2, 3, 1, 2, 4]
    ○ Expected Output: [3, 2, 1, 4]
"""

arr = [3, 2, 3, 1, 2, 4]

def remove_duplicates(arr):
    unique = set()
    result = []
    for num in arr:
        if num not in unique:
            unique.add(num)
            result.append(num)
    return result

x = remove_duplicates(arr) 
print(f"Output: {x}")       
