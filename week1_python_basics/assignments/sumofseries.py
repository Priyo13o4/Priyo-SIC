n = int(input("Enter N (term) value : "))
m = int(input("Enter number of terms : "))

sum_of_series = 0
sign = -1
for i in range (m):
    numerator = n ** 2 ** i #right to left
    denominator = (2 * i + 1)
    #sign = (- 1) ** i
    sign = -1 * sign
    term = numerator / denominator * sign
    sum_of_series = sum_of_series + term
print(sum_of_series)

