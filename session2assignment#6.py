# This program is to find how much paint is needed to paint a room and the total cost
length = float(input("Enter the length: "))
height = float(input("Enter the height: "))
width = float(input("Enter the width: "))
totalarea = 2 * length * height + 2 * width * height
print("Total area:", totalarea)
sqftpergal = 400
ngal = round(float(totalarea / sqftpergal + .9999))
print("Total number of gallons:", ngal)
prgal = float(input("Enter the price of the gallon: "))
cost = ngal * prgal
print("Total cost of the paint:$", cost)
