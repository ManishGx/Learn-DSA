# Wap to find the kth smallest element in an array 

def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [7,10,4,3,20,15]
k=3
print('sorted array:', sorted(arr))
print(kth_smallest(arr, k))
    