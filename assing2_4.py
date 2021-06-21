#writing a code  to find out the bonus amount they get
def bonus_for_employee(salary,year_of_work):
    bonus = 0
    if (year_of_work>5):
        bonus = int(bonus + 0.05 * (salary))
        print(f"Bonus is {bonus}")
    
    else:
        print("No Bonus")
    return salary
        

#assing variables for user inputs
salary=int(input(""))
year_of_work=int(input(""))
bonus_for_employee(salary,year_of_work)#function call