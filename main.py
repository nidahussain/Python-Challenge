import os
import csv
from operator import itemgetter

#opening the file
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #define variables
    total_votes = 0
    total_candidates = 0
    winner_votes = 0
    greatest_votes = ["", 0]
    candidate_options = []
    candidate_votes = {}

    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row[2]        

        if row[2] not in candidate_options:
            
            candidate_options.append(row[2])

            candidate_votes[row[2]] = 1
            
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    print("Election Results")
    print("-----------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("-----------------------------------------")

#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100.00))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("---------------------------------------")
print("Winner: " + str(winner[0]))
print("----------------------------------------")