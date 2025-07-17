# Array Transport Problem
# (Assuming the problem is: Given n, x, y, and an array, count how many p values can split the array into x elements > p and y elements < p)

def count_valid_p(n, x, y, arr):
    arr.sort()
    count = 0
    # p must be between arr[x-1] and arr[x] (exclusive)
    for p in range(arr[x-1]+1, arr[x]+1):
        count += 1
    return count

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_valid_p(n, x, y, arr)) 