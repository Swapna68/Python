annual_salary = int(input('Enter your annual salary:-'))
monthly_salary = float(annual_salary/12)
sav_salary = float(
    input('\nEnter the percent of salary you want to save:-'))
current_saving = 0.0
dream_cost = int(input('\nEnter the total cost of your house: -'))
semi_inc = float(input('Enter the semi­annual raise, as a decimal:-'))
for i in range(1, 999):
    if current_saving >= dream_cost*0.25:
        break
    if i % 6 == 0:
        monthly_salary += monthly_salary*semi_inc
    current_saving += (monthly_salary*sav_salary)
    current_saving += (current_saving*0.04)/12
print('No of months required:-', i)
