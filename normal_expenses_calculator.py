import time

total_budget = float(input("Enter your this month's budget (in CAD): "))
print("Your budget as a whole is $", total_budget)

print("******** Please add your expense ********")
option = input("Do you want to add an expense, please select: ")
i = 0
total_expense = 0
expense_list = []
if (option == 'yes'):
    while (True):
        expense = (input("Please add title: "))
        expense_list.append(expense)
        expense_budget = float(input("Please enter how much was the expense: "))
        print("The expense of", expense, "is $", expense_budget)
        total_expense += expense_budget
        i =+ 1
        loop_option = input("do you want to add another expense??? ")
        if (loop_option == 'yes'):  
            
            continue
        else:
            print("calculating remaining of the total budget...")
            time.sleep(2)
            print("Your expenses:")
            print(*expense_list, sep = ', ')
            remaining_budget = total_budget - total_expense
            if (total_expense > total_budget):
                print("Its " + str(remaining_budget) + "$." + (" Things just got out of hand!"))
                break
            else:
                print("Remaining budget is:", remaining_budget, "$.")
                break
else: 
    print("Its still $", total_budget, "you cunt. Spend a penny first!!!")
