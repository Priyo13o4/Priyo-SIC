# Missing Numbers Problem
from collections import Counter

def find_missing(arr, brr):
    count_a = Counter(arr)
    count_b = Counter(brr)
    missing = []
    for num in count_b:
        if count_b[num] > count_a.get(num, 0):
            missing.append(num)
    return sorted(missing)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    brr = list(map(int, input().split()))
    print(*find_missing(arr, brr)) 