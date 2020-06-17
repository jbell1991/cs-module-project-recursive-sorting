# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    left = 0
    right = 0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # find middle point
    mid = len(arr) // 2
    # separate list into left and right
    left = arr[:mid]
    right = arr[mid:]
    # base case, if array contains 1 element it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # recursive call splits list into left and right until
        # there is one element in the left and right lists
        return merge(merge_sort(left), merge_sort(right))

# Test
# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
