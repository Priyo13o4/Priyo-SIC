#Solve this using recursion as well
def getMinimumCost(k, c):
    c.sort()
    i = 1
    j = 1 #number of flowers previously purchased
    minimum_cost = 0
    while i <= len(c):
        if i <= k :
            minimum_cost += c[-i] # for j = 0 we are already doing here
        else : 
            minimum_cost += (j+1) * c[-i]
            if i % k == 0 :
                j += 1
        i += 1
    return minimum_cost



if __name__ == '__main__':

    nk = input("Enter space seperated values for N and K: ").split()
    n = int(nk[0])
    k = int(nk[1])
 
    c = list(map(int, input("Enter cost of the flowers: ").rstrip().split()))

    minimum_cost = getMinimumCost(k, c)
    print(f"Minimum cost = {minimum_cost}")
