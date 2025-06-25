"""Accept the average score from the student and give her the results as follows :
(for ease of understanding let the input be int).
Also check for invalid input
0 to 69 Fail
70 to 84 Second class
85 to 95 First class
96 to 100 Excellent
"""
#str input()
#str input(str)
#In python there is no function Overloading , but that function must work for different number of arguements.

average_score = int(input("Enter the student average score : "))

if average_score < 70 :
    print('Result is Fail')
elif average_score >= 70 and average_score <=84 : # we can remove the first condtion as its ordered and the reuslt is unaffected
    print('Second class')
elif average_score >= 85 and average_score <=95 :
    print('First class')
elif average_score >= 96 and average_score <=100 :
    print('Excellent')
else :
    print("Invalid Average Score")
    