import time

total_budget = float(input("Enter your this month's budget (in CAD): "))
print("Your budget as a whole is $", total_budget)

print("******** Please add your expense ********")
option = input("Do you want to add an expense, please select: ")
i = 0
expense_budget_total = 0
expense_list = []
if (option == 'yes'):
    while (True):
        expense = (input("Please add title: "))
        expense_list.append(expense)
        expense_budget = float(input("Please enter how much was the expense: "))
        print("The expense of", expense, "is $", expense_budget)
        expense_budget_total += expense_budget
        i =+ 1
        loop_option = input("do you want to add another expense??? ")
        if (loop_option == 'yes'):  
            
            continue
        else:
            print("calculating remaining of the total budget...")
            time.sleep(2)
            print(*expense_list, sep = ', ')
            print("Remaining budget is: $", total_budget-expense_budget_total)
            break
else: 
    print("Its still $", total_budget, "you cunt. Spend a penny first!!!")


    


