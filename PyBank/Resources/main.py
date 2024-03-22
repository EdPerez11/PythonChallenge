import csv

# Initialize variables for counting rows and calculating the changes and averages
total_months = 0
net_amount = 0
changes_amount = 0
previous_profit_loss = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# with open in order to read the csv file
with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row so it is not counted later on without values
 
    # Iterate through the rows to count the number of months and calculate net amount
    for row in csv_reader:
        total_months += 1
        net_amount += int(row[1])

        # Calculate the changes with if conditionals in profit/losses
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            changes_amount += change

            # Check for greatest increase in profits
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            # Now check for the greatest decrease in profits
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = changes_amount / (total_months - 1) if total_months > 1 else 0

# Print
print(f"Total Months: {total_months}")
print(f"Net Amount: ${net_amount}")
print(f"Total Changes: ${changes_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")