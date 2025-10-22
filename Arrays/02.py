# Find the maximum and minimum elements in an array

def find_max_min(arr):
    if len(arr) == 0:
        return None
    
    max_elem = arr[0]
    min_elem = arr[0]

    for num in arr:
        if num > max_elem:
            max_elem = num
        if num < min_elem:
            min_elem = num

    return (max_elem, min_elem)  

# Example
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = find_max_min(arr)
print("Max and Min:", result)
