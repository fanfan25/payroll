"""

program: payroll2.py
Author: Jude 11/2/2021

program that reads from a text file and outputs the info in tabular format.
"""

# Input phase
fileName =input("Please enter the name of the employee data file that you wish to use: ")

# Calculation phase
# Open the input file which is the source of the employee payroll data

data = open(fileName, "r")

# output phase
# print the report's header in tabular format
print()
print("%-18s%7s%7s" % ("Last Name", "Wage", "Hours"))
#print("{}  {}  {}".format("Last Name", "Wage", "Hours"))

print("-" * 32)

# Read the text from the file line by line. Split up the dat from each line. Place each component into tabular format for output.

for line in data:
	# Seperate the line into individual string values
	dataArray = line.split()
	# Extract the name and store it in a variable
	name = dataArray[0]
	# Extract the wage, convert it to float and store it
	wage = float(dataArray[1])
	# extract the hours and convert it to float 
	hours = float(dataArray[2])

	# output this emplyee's info in tabular format
	print("%-18s%7.2f%7.2f" % (name, wage, hours))
	#print("{0:%-18} {1:%7.2f} {2:%7.2f}".format(name, wage, hours))

# Final output message
print()
print("Thank you for using payroll2. Have a great day!")

