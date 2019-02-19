annual_salary = int(input('Enter your annual salary:-'))
monthly_salary = float(annual_salary/12)
sav_salary = float(input('\nEnter the percent of salary you want to save:-'))
portion_saved = monthly_salary*sav_salary
current_saving = 0.0
dream_cost = int(input('\nEnter the cost of your dream house:-'))
down_payment = dream_cost*0.25
for i in range(1, 999):
    if current_saving >= down_payment:
        break
    current_saving += portion_saved
    current_saving += (current_saving*0.04)/12
print('No of months required:-', i)
