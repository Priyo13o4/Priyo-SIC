#Basic Input and Salary Calculation
employee_name = input(f"Please enter the Employee Name : ")
employee_id = input(f"Please enter the Employee ID : ")
basic_monthly_salary = int(input(f"Please enter the Basic Monthly salary : "))
speical_allowances = int(input(f"Please enter the Special Allowances(monthly) : "))
bonus_percentage = float(input(f"Please enter the Bonus Percentage : "))

gross_monthly_salary = basic_monthly_salary + speical_allowances

annual_gross_salary_before_bonus = (gross_monthly_salary * 12)
bonus = (bonus_percentage/100) * annual_gross_salary_before_bonus

annual_gross_salary = annual_gross_salary_before_bonus + bonus
print(f"{'Employee Name':25s}: {employee_name}")
print(f"{'Employee ID':25s }: {employee_id}")
print(f"{'Employees Gross monthly salary':25s}: {gross_monthly_salary}")
print(f"{'Employees Annual gross salary':25s}: {annual_gross_salary}")

#Txable Income Calculation

standard_deduction = 50000
taxable_salary = annual_gross_salary - standard_deduction

print(f"{'Employees Annual gross salary':25s} : {annual_gross_salary }") 
print(f"{'Standard Deduction':25s} : {standard_deduction }")
print(f"{'Taxable Income':25s}: {taxable_salary}")

