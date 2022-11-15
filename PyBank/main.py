#PyBank Instruction
#------------------------------------------------------------------------------------------------------>
#Calculating the total number of months
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#-------------------------------------------------------------------------------------------------------->
# Import dependencies
# --------------------------------------------------------------------------------------------------------
# import os
#import csv
import csv
import os

# Define PyBank's variables for the Analysis
total_months = []
profitloss_changes = []
months_counter = 0
netprofit_loss = 0
previous_month_profit_loss = 0
current_profit_loss = 0
change = 0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# path to collect data from the Resources folder

# pwd = os.getcwd()
# print(pwd)

# print('+++++++++++++++++++++++++++')
# print(f'Directory changed to {pwd}')
# print('+++++++++++++++++++++++++++')

budget_data = os.path.join("Resources","budget_data.csv")
# Open and read csv, encoding ='utf-8' as csv file

with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
# Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
# Iterate through the rows in the stored file contents
    for row in csv_reader: 
        # print(row)
       
    #Counts of months
        months_counter+=1
        # print(months_counter)

#Net total amount of "Profit/Losses" over the period
        current_profit_loss=int(row[1])
        
        netprofit_loss+= current_profit_loss

   #looping through the rows
        if (months_counter==1):
            previous_profit_loss=current_profit_loss
        else:
            change=current_profit_loss-previous_profit_loss
            
            total_months.append(row[0])
            profitloss_changes.append(change)
       
# Make the current_loss to be previous_profit_loss for the next loop
            previous_profit_loss = current_profit_loss

#Sum and average of the change in "profit/loss" over the period
sum_profit_loss = sum(profitloss_changes)
# print(sum_profit_loss)
average_profit_loss = (round((sum_profit_loss/(months_counter-1)),2))
# print(average_profit_loss)
#Calculating the highest/lowest changes in "profit/loss" months on months
max_profit_loss=max(profitloss_changes)
# print(max_profit_loss)
min_profit_loss=min(profitloss_changes)
# print(min_profit_loss)
# highest and lowest changes in "Profit/Losses" months on months
highest_change = max(profitloss_changes)
lowest_change = min(profitloss_changes)
# print(lowest_change)
# Locate the index value of highest and lowest changes in "Profit/Losses" over the period
highest_month_index = profitloss_changes.index(highest_change)
# print(highest_month_index)
lowest_month_index = profitloss_changes.index(lowest_change)
# print(lowest_month_index)
# Assign best and worst month
best_month = total_months[highest_month_index]
# print(best_month)
worst_month = total_months[lowest_month_index]
# print(worst_month)
# -------------------------------------------------------------------------------------------------->
# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months_counter}")
print(f"Total:  ${netprofit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# pwd = os.getcwd()  
# print(pwd)
# # Export to a text file with the results printed above--------------------------------------------->
budget_file = os.path.join("Output", "budget_output.txt")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {months_counter}\n")
    outfile.write(f"Total:  ${netprofit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")









