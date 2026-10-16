# Personal Expense Tracker

while True:
    number = int(input("Number of expenses:"))
    if number > 0:
        break

while True:
    budget = int(input("What is your budget?"))
    if budget > 0:
        break


expenses = [] # An empty list to store the items
amounts = [] # An empty list to store the amounts

num = 1
while num <= number:
    expense = str(input("What is the expense?"))
    expenses.append(expense)

    while True:
        amount = float(input("How much did your spend on it?"))
        if amount >= 0:
            break
    amounts.append(amount)

    num +=1

total = sum(amounts)
Average = total/number

if total > budget:
    exceeding_amount = total-budget

if total < budget:
    remaining_amount = budget-total

count = 0
no = 0
while no <= number-1:
    if amounts[no] > 1000:
        count += 1
    no +=1
    
highest = max(amounts)
highest_index = amounts.index(highest)
highest_item = expenses[highest_index]


lowest = min(amounts)
lowest_index = amounts.index(lowest)
lowest_item = expenses[lowest_index]

print()

no = 1
while no <= number:
    print(f"Expense: {expenses[no-1]} - Amount :Rs.{amounts[no -1] }")
    no += 1
print()
print(f"Total :Rs.{total}")
print(f"Average :Rs.{Average}")
print()
if total > budget:
    print(f"Exceeding amount : Rs.{exceeding_amount}")
if total < budget:
    print(f"Remaining amount : Rs.{remaining_amount}") 
print()
print(f"The expenses exceeding Rs.1000: {count}")
print(f"Highest amount was spent on: {highest_item}, Amount :Rs.{highest}")
print(f"Lowest amount was spent on: {lowest_item}, Amount :Rs.{lowest}")
print()

