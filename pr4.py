"""    **** CISCO ****

4. Find Missing Number in Array:
   Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
   Find the missing element.
"""

def find_missing_element(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    missing_number = total_sum - arr_sum

    return missing_number

n = 5
arr = [1, 2, 3, 5]
print(f"Example 1 Output: {find_missing_element(arr, n)}")

n1 = 10
a1 = [6, 1, 2, 8, 3, 4, 7, 10, 5]
print(f"Example 2 Output: {find_missing_element(a1, n1)}")
