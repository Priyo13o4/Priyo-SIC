# Boys and Girls Arrangement Problem

def can_arrange(boys, girls):
    boys.sort()
    girls.sort()
    # Try both arrangements: boy first or girl first
    for first in [0, 1]:
        ok = True
        merged = []
        for i in range(len(boys)):
            if first == 0:
                merged.append(boys[i])
                merged.append(girls[i])
            else:
                merged.append(girls[i])
                merged.append(boys[i])
        for i in range(1, len(merged)):
            if merged[i] < merged[i-1]:
                ok = False
                break
            if i % 2 == 1 and merged[i] == merged[i-1]:
                ok = False
                break
        if ok:
            return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        boys = list(map(int, input().split()))
        girls = list(map(int, input().split()))
        print(can_arrange(boys, girls)) 