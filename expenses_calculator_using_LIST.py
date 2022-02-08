import time

# FUNCTION METHOD

total_budget = 0

def calculations():
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
                print("Your expenses:", *expense_list, sep = ',')
                print(*expense_list, sep = ', ')
                remaining_budget = total_budget - total_expense
                if (total_expense > total_budget):
                    print("Its " + str(remaining_budget) + "$." + (" Things just got out of hand!"))
                    break
                else:
                    print("Remaining budget is:", remaining_budget, "$.")
                    break
    else: 
        print("Its still $", total_budget, ". Spend a penny first mate!!!")

def time_range():
    time_list = ['week', 'month']
    global total_budget
    day_range = input("Please enter if you either want to manage your budget in weekly basis or monthly basis: ")
    if (day_range == time_list[0]):
        week_budget = float(input("ENTER YOUR BUDGET (IN CAD): "))
        total_budget += week_budget
        print("Your this " + time_list[0] + "'s budget is $", total_budget)
        calculations()
    elif (day_range == time_list[1]):
        month_budget = float(input("ENTER YOUR BUDGET (IN CAD): "))
        total_budget += month_budget
        print("Your this " + time_list[1] + "'s budget is $", total_budget)
        calculations()
    else: 
        print("Please select if either you want to manage your weekly or monthly budget...")
        time_range()

time_range()

# NORMAL METHOD

# total_budget = float(input("Enter your this month's budget (in CAD): "))
# print("Your budget as a whole is $", total_budget)

# print("******** Please add your expense ********")
# option = input("Do you want to add an expense, please select: ")
# i = 0
# total_expense = 0
# expense_list = []
# if (option == 'yes'):
#     while (True):
#         expense = (input("Please add title: "))
#         expense_list.append(expense)
#         expense_budget = float(input("Please enter how much was the expense: "))
#         print("The expense of", expense, "is $", expense_budget)
#         total_expense += expense_budget
#         i =+ 1
#         loop_option = input("do you want to add another expense??? ")
#         if (loop_option == 'yes'):  
            
#             continue
#         else:
#             print("calculating remaining of the total budget...")
#             time.sleep(2)
#             print("Your expenses:")
#             print(*expense_list, sep = ', ')
#             remaining_budget = total_budget - total_expense
#             if (total_expense > total_budget):
#                 print("Its " + str(remaining_budget) + "$." + (" Things just got out of hand!"))
#                 break
#             else:
#                 print("Remaining budget is:", remaining_budget, "$.")
#                 break
# else: 
#     print("Its still $", total_budget, "you cunt. Spend a penny first!!!")
