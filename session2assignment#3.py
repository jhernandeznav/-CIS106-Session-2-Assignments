# program to help banks count pennies,nickles,dimes, quarters
pnum = float(input("Enter the amount of pennies: "))
pennies = pnum * .01
nnum = float(input("Enter the amount of nickles: "))
nickels = nnum * .05
dnum = float(input("Enter the amount of dimes: "))
dimes = dnum * .10
qnum = float(input("Enter the amount of quarters: "))
quarters = qnum * .25
print("Pennies:", "$", pennies)
print("Nickles:", "$", nickels)
print("Dimes", "$", dimes)
print("Quarter", "$", quarters)
