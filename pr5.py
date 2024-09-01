"""
5. Intersection of Two Arrays:
    ○ Question: Find the intersection of two arrays.
    ○ Logic: Use a hash set to store one array's elements and check for
    common elements in the second array.
    ○ Sample Input: [1, 2, 2, 1] and [2, 3, 4]
    ○ Expected Output: [2]
"""

arr1 = [1, 2, 2, 1]
arr2 = [2, 3, 4]

def find_intersection(arr1, arr2):
    set1 = set(arr1)
    intersection = []

    for num in arr2:
        if num in set1:
            intersection.append(num)
            
    return intersection

result = find_intersection(arr1, arr2)
print(f"Intersection: {result}")
