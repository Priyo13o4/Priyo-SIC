def quick_sort(array,low,high) :
    if low<high :
        pivot_index = partition(array,low,high)
        quick_sort(array,low,pivot_index-1)
        quick_sort(array,pivot_index+1,high)

def partition(array,low,high):
    pivot = array[high]
    k = low
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[k] = array[k], array[i]
            k += 1
    array[k], array[high] = array[high], array[k]
    return k


arr1 = [1,5,10,12,9,6,2,8,4,11,7,3] # average case
arr2 = [1,2,3,4,5,7,6,8] # best case , or if the pivot ends up dividng exactly in the middle as recursion call reduce
arr3 = [6,5,4,3,2,1] # We get the worst case here O(n^2)


for arr in [arr1, arr2, arr3]:
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)


# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         povit = arr[-1]
#         l_arr=[]
#         r_arr=[]
#         for i in range(len(arr)-1):
#             if arr[i]<povit:
#                 l_arr.append(arr[i])
#             else:
#                 r_arr.append(arr[i])
#         return quick_sort(l_arr)+[povit]+quick_sort(r_arr)
# arr=[1,5,3,2,9,7,5,4,0,9,8,7,5,4,3]
# arr2 =[5,5,5,5,5,5,5]
# print(quick_sort(arr))
# print(quick_sort(arr2))