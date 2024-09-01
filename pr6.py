"""
6. Given two 0-indexed arrays nums 1 and nums 2, return a list answer of size 2 where:
   ○ answer[0] is a list of all distinct integers in nums 1 which are not present in nums 2.
   ○ answer[1] is a list of all distinct integers in nums 2 which are not present in nums 1.
   Note that the integers in the lists may be returned in any order.
   ○ Input: nums1 = [1, 2, 3], nums2 = [2, 4, 6]
   ○ Output: [[1, 3],[4, 6]] 
"""



num1 = [1, 2, 3]
num2 = [2, 4, 6]

def find_difference(num1, num2):
    set1 = set(num1)
    set2 = set(num2)

    x = list(set1 - set2)
    y = list(set2 - set1)

    return [x, y]

result = find_difference(num1, num2)
print(result)
