# Import os and csv modules
import os
import csv

# Establish file path for file 'budget_data.csv'
csvpath = os.path.join("Resources", "budget_data.csv")

# Declare and assign starting values for output variables
monthCount = 0
totalNetPL = 0
greatestInc = 0
greatestDec = 0

# Declare a variable to store the previous Profit/Loss value to be used for calculating the month-to-month Profit/Loss change
previousPL = 0
    
# Declare a variable to store a calculated month-to-month Profit/Loss change
PLChange = 0

# Declare a list to contain all of the calculated month-to-month Proft/Loss changes
monthlyChange = []


# Read file 'budget_data.csv' and store it in the object rawData
with open(csvpath) as sourceFile:
    rawData = csv.reader(sourceFile, delimiter=",")

    # Skip over the header row so that the rest of the code looks at the data values
    next(rawData)

    # Loop through each row in the read csv file stored in rawData
    for row in rawData:
        # Since each month is unique to each row, the number of months can be counted by increasing the monthCount by 1 with each iteration
        monthCount += 1
        # Add the value of the Profit/Loss column in the csv file to totalNetPL variable to sum up the net Total Profit/Loss within the data set
        totalNetPL += int(row[1])
        # Calculate the month-to-month Profit/Loss change and store it in variable PLChange
        PLChange = int(row[1]) - previousPL
        # Check to see if the calculated month-to-month Profit/Loss change for the current row is has the Greatest Increase or Decrease in Profits
        # If PLchange (current row's month-month Profit/Loss) is higher than what is currently stored in variable greatestInc, then greatestInc is reassigned the value of PLChange and greatestIncMonth is reassigned the value of the current row's month
        if PLChange > greatestInc:
            greatestInc = PLChange
            greatestIncMonth = row[0]
        # If PLchange (current row's month-month Profit/Loss) is lower than what is currently stored in variable greatestDec, then greatestDec is reassigned the value of PLChange and greatestDecMonth is reassigned the value of the current row's month
        elif PLChange < greatestDec:
            greatestDec = PLChange
            greatestDecMonth = row[0]

        # Add the value of PLchange to the list monthlyChange
        monthlyChange.append(PLChange)

        # Store the value of the current row's Profit/Loss in variable previousPL for use in the next iteration  
        previousPL = int(row[1])

# Remove the first value in the monthlyChange list since it does not reflect a change in Profit/Losses (the first row of rawData had no previous Profit/Losses value to compare it to)
    monthlyChange.pop(0)

# Define a function that receives a list and returns an average, rounded to two decimal places
def calculateAverage(numberList):
    length = len(numberList)
    sumTotal = 0.00
    for number in numberList:
        sumTotal+=number
    return round((sumTotal/(length)),2)


# Print output to terminal
# Print the output title
print("Financial Analysis")
print("----------------------------")

# Print Total Months
print(f"Total Months: {monthCount}")

# Print net total amount of 'Profit/Losses' over the entire period
print(f"Total: ${totalNetPL}")

# Print the average changes in 'Profit/Losses by calling the calculateAverage function using monthlyChange list
print(f"Average Change: ${calculateAverage(monthlyChange)}")    

# Print greatest increase in profits (date & amount)
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")

# Print greatest decrease in profits (date & amount)
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")

# Write output to a text file
# Determine the output path for file 'analysis_results.txt'
outputPath = os.path.join("analysis","analysis_results.txt")

# Create/open file 'analysis_results.txt'
with open(outputPath, 'w') as outputFile:

# Write the output title to .txt file
    outputFile.write("Financial Analysis\n")
    outputFile.write("----------------------------\n")

# Write Total Months to .txt file
    outputFile.write(f"Total Months: {monthCount}\n")

# Write net total amount of 'Profit/Losses' over the entire period to .txt file
    outputFile.write(f"Total: ${totalNetPL}\n")

# Write the average changes in 'Profit/Losses by calling the calculateAverage function using monthlyChange list
    outputFile.write(f"Average Change: ${calculateAverage(monthlyChange)}\n")    

# Write greatest increase in profits (date & amount) to .txt file
    outputFile.write(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})\n")

# Write greatest decrease in profits (date & amount) to .txt file
    outputFile.write(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})\n")  