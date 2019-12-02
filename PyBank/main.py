import os, csv

with open(os.path.join("budget_data.csv"), "r") as file:

	csv_reader = csv.reader(file)
	data = list(csv_reader)
	header = data.pop(0)


#var definitions
months = 0
total = 0
changes = []


# The total number of months included in the dataset
months = len(data)


# The net total amount of "Profit/Losses" over the entire period
total = sum(int(row[1]) for row in data)


# The average of the changes in "Profit/Losses" over the entire period
profit_losses = [x[1] for x in data]
profit_losses = [int(i) for i in profit_losses] # Transforming everything to ints


for i in range(0, len(profit_losses)-1):
	diff = profit_losses[i+1] - profit_losses[i]
	changes.append(diff)

# Actual average
average_diff = sum(changes) / len(changes)
average_diff = round(average_diff, 2)


# The greatest increase in profits (date and amount) over the entire period
profit = max(changes)
profit_place = data[profit_losses.index(max(profit_losses))]


# The greatest decrease in losses (date and amount) over the entire period
loss = min(changes)
loss_place = data[profit_losses.index(min(profit_losses))]


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

analysis = "\n"+"\n"\
+ "Financial Analysis"\
+"\n"+"----------------------------"\
+"\n"+"Total Months: " + str(months)\
+"\n"+"Total: $" + str(total)\
+"\n"+"Average  Change: $" + str(average_diff)\
+"\n"+"Greatest Increase in Profits: " + str(profit) + " ($" + str(profit_place[0]) +")"\
+"\n"+"Greatest Decrease in Profits: " + str(loss) + " ($" + str(profit_place[0]) +")"

print(analysis)

f = open('out_file.txt','w')
f.write(analysis)
f.close()

