""" 
Find the Duplicate Number
 => Given an array of integers nums containing n + 1 
 => There is only one duplicate number in nums, return this duplicate number.
"""
# METHOD 1: USING DICTIONARY
def findDuplicateUsinDict(arr, arr_size):
    dict = {}
    for el in arr:
        try:
            dict[el] += 1
        except:
            dict[el] = 1
    

    for item in dict:
        if dict[item] > 1:
            return item

# METHOD 2: USING SORT
def findDuplicateUsingSort(arr, arr_size):
    arr.sort()
    for i in range(1, arr_size):
        if arr[i] == arr[i-1]:
            return arr[i]


# METHOD 3: USING SET
def findDuplicateUsingSet(arr, arr_size):
    seen = set()
    for i in range(0, arr_size):
        if arr[i] in seen:
            return arr[i]
        seen.add(arr[i])

# Driver code 
arr = [1, 2, 3, 4, 5, 6, 4] 
arr_size = len(arr) 
# findDuplicateUsinDict(arr, arr_size)
# findDuplicateUsingSet(arr, arr_size)
print(findDuplicateUsingSet(arr, arr_size))