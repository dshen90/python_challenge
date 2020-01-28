# importing dependencies
import os
import csv
#reading file
csv_path = os.path.join("..","python_challenge", "budget_data.csv")

#open file
with open(csv_path, newline="") as csvfile:
	csv_reader=csv.reader(csvfile, delimiter=",")

#Find total months recorded
	x=0
	profit_loss=[]
	header=next(csv_reader)
	for row in csv_reader:
		x+=1
		profit_loss.append(int(row[1]))
	print(x)
#Find net total profit/loss
	total = 0
	for n in profit_loss:
		total+=n
	print(total)
#find changes between months
	changes=[]
	index = 0
	while(index != len(profit_loss)):
		changes.append(profit_loss[index] - profit_loss[index - 1])
		index+=1

	list_sum = 0;
	change_index = 0
	while(change_index != len(changes)):
		list_sum += change_index
		change_index+=1

	print(list_sum)
	# avg_change=(sum(changes))/len(changes)
	# print(avg_change)

	greatest_increase=max(changes)
	greates_loss=min(changes)
	# print(changes)
	print(greatest_increase)
	print(greates_loss)

#Write out a report
output_path= os.path.join('..','outputs','bank_notes.txt')

with open(output_path,'w') as out:
	print(line1,file=out)
	print(line2,file=out)
	print(line3,file=out)
	print(line4,file=out)
	
