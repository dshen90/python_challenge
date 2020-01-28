#import dependencies
import os
import csv
#read Election Data
csv_path = os.path.join("..","python_challenge", "election_data.csv")

with open(csv_path, newline="") as csvfile:
	csv_reader=csv.reader(csvfile, delimiter=",")
#Count total votes
#count candidates
	total_votes=0
	vote_list={}

	header=next(csv_reader)
	for row in csv_reader:
		total_votes+=1
		if row[2]not in vote_list:
			vote_list[row[2]] = 1
		else:
			vote_list[row[2]]+=1
	line1=('Election Results:\n------------------------')
	print('Election Results:\n------------------------')
	line2=('Total Votes:     '+str(total_votes))
	print('Total Votes:     '+str(total_votes))
	
	for k,v in vote_list.items():
		line3=(f"{k}     {str(round((v/total_votes)*100,2))}%       {v}   votes")  
		print(f"{k}     {str(round((v/total_votes)*100,2))}%       {v}   votes")

	

	#Winner based on popular vote
	max_val=0
	for k,v in vote_list.items():
		if max_val<v:
			max_val=v
	for k,v in vote_list.items():
		if v ==max_val:
			line4=('The winner is '+k)
			print('The winner is '+k)


	#Write out a report
output_path= os.path.join('..','outputs','poll_notes.txt')

with open(output_path,'w') as out:
	print(line1,file=out)
	print(line2,file=out)
	print(line3,file=out)
	print(line4,file=out)