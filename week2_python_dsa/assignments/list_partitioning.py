# List Partitioning Problem
# (Assuming the problem is: Given a list, partition it into two lists such that the sum of both is as equal as possible)

def partition_list(arr):
    arr.sort(reverse=True)
    a, b = [], []
    sum_a, sum_b = 0, 0
    for x in arr:
        if sum_a <= sum_b:
            a.append(x)
            sum_a += x
        else:
            b.append(x)
            sum_b += x
    return a, b

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    a, b = partition_list(arr)
    print("List 1:", a)
    print("List 2:", b) 