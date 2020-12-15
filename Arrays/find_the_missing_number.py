""" 
Find the missing Number from the given array of size N.

Problem:
You are given a list of n-1 integers and these integers are in the
range of 1 to n. There are no duplicates in the list. One of the integers
is missing in the list.

Input:
N = 5
A[] = {4, 3, 1, 5}
Output: 2

Solution Approach:
- Find the expected summation of n elements: n(n+1)/2
- Find the summation of current elements 
- Subtract current element's sum from the expected sum to get the 
  missing value.

# https://www.geeksforgeeks.org/find-the-missing-number/
"""


def getMissingNumber(array, n):
    expected_sum = int(n*(n+1)/2)
    current_sum = sum(array)
    missing_value = expected_sum - current_sum
    return missing_value


n = 5
array = [4, 3, 1, 5]

# Missing Value
print("Missing Value: ", getMissingNumber(array, n))
