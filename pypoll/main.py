import os
import csv

# path to data file
election_data = 'election_data.csv'

#variables
#set this equal to 0
total_votes = 0
#create list for unique candidates
candidates_unique = []
#create list for unique candidate votecount
candidate_vote_count = []

#read file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
 #if candidate already in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
 #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #calculation to get the percentage
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

#print to git bash
print('-------------')
print('Election Results')
print('-------------')
print(f'Total Votes: {total_votes}')
print('-------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('-------------')
print(f'Election winner: {election_winner}')
print('-------------')


#output to .txt
output_file = "pypoll_election_results.txt"
with open(output_file, "w", newline="") as datafile:
    datafile.write('-------------\n')
    datafile.write('Election Results\n')
    datafile.write('-------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('-------------\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('-------------\n')
    datafile.write(f'Election winner: {election_winner}\n')
    datafile.write('-------------\n')
    datafile.write("---END OF REPORT---")
