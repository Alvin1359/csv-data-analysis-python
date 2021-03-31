# Import relevant modules
import os
import csv

# Locate budget_data.csv file
dirname = os.path.dirname(__file__)
budget_csv = os.path.join(dirname, "Resources", "budget_data.csv")

# Initialise variables
total_months = []
profit_loss_list = []
profit_loss = 0
profit = 0
loss = 0
net_total = 0
decrease = 0
increase = 0
inc_name = 0
dec_name = 0
max_profit = 0
max_loss = 0

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        
        # Find the total number of months
        total_months.append(row[0])
        
        # Find net total of Profit/Loss
        if int(row[1]) > 0:
            profit = profit + int(row[1])
        
        if int(row[1]) < 0:
            loss = loss - int(row[1])
        
        net_total = profit - loss

        # Average of change in Profit/Loss
        profit_loss = int(row[1]) - profit_loss
        profit_loss_list.append(profit_loss)    
        profit_loss = int(row[1])

        # Greatest increase in profits
        if int(row[1]) > increase:
            increase = int(row[1])
            inc_name = row[0]
            max_profit = max(profit_loss_list)

        # Greatest decrease in losses
        if int(row[1]) < decrease:
            decrease = int(row[1])
            dec_name = row[0]
            max_loss = min(profit_loss_list)

# Printing results to the terminal
print(" ")
print(" ")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(total_months)}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(sum(profit_loss_list[1:])/len(profit_loss_list[1:]),2)}')
print(f'Greatest Incrase in Profits: {inc_name} (${max_profit})')
print(f'Greatest Decrease in Profits: {dec_name} (${max_loss})')
print(" ")
print(" ")

# Export a text file with the results
# Saving the output file path
output_file = os.path.join(dirname, "Analysis", "Financial Analysis.txt")

# Open the output file, write in results into the txt file
with open(output_file, "w") as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {len(total_months)}\n')
    txtfile.write(f'Total: ${net_total}\n')
    txtfile.write(f'Average Change: ${round(sum(profit_loss_list[1:])/len(profit_loss_list[1:]),2)}\n')
    txtfile.write(f'Greatest Increase in Profits: {inc_name} (${max_profit})\n')
    txtfile.write(f'Greatest Decrease in Profits: {dec_name} (${max_loss})\n')