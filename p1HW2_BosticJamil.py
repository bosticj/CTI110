# Create a program that will calculate and display travel expenses
#9/28/2023
#CTI-110 P1HW2 - Travel Expense
#Jamil Bostic
print("This program calculates and displays travel expenses")
budget=float(input("Enter budget: "))
destin=input("Enter your travel destination: ")
gas=float(input("How much do you think you will spend on gas? "))
hotel=float(input("Approximately, how much will you need for accomodations/hotel? "))
food=float(input("Last, how much do you need for food? "))
print("------------Travel Expenses------------")
print("Location: ",destin)
print(f'Initial Budget: {budget:.0f} ')
print('')
print(f'fuel: {gas:.0f} ')
print(f'Accomodation: {hotel:.0f} ')
print(f'Food: {food:.0f} ')
print('')
bal=( budget-( hotel + gas + food))

print(f'Remaining Balance: {bal:.0f}')
