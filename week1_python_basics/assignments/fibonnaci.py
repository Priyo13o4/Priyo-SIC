#Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2

term_number = int(input("Please Enter the number of terms :"))
term_1 = 1 
term_2 = 2

if term_number <= 0:
    print("Invalid input. Number must be greater than 0.")
elif term_number == 1:
    print(term_1)
elif term_number == 2:
    print(f"{term_1}, {term_2}")
else:
    print(f"{term_1}, {term_2}", end="")
    for i in range (3,term_number+1) :
        next_term = term_1 + term_2
        print(",",next_term , end = "")
        term_1 = term_2
        term_2 = next_term
    print()
