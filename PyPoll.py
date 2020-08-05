import os
import csv

with open('Resources/election_data.csv') as election_csv:
    csvreader = csv.reader(election_csv, delimiter = ',')

    votes_each = {}
    candidates = []
    
    # skip header row
    next(csvreader)

    for row in csvreader:
        # appends unique candidate names to list 'candidates' and starts vote count for dictionary 'votes_each'
        # for each instance of a given candidate, adds 1 to corresponding dict value
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_each[row[2]] = 1

        votes_each[row[2]] += 1

    total_votes = sum(votes_each.values())


    # calculates percentage of votes each candidate received
    percent = []

    for key in votes_each:
        temp_var = votes_each[key] / total_votes * 100
        percent.append(round(temp_var, 3))

    
    # calculates winner of election. The for loop will successively store the highest number of votes as var winner0 until resolved
    winner0 = 0
    winner1 = ""
    
    for x in votes_each:
        if votes_each[x] >= winner0:
            winner0 = votes_each[x]
            winner1 = x
        else:
            pass

    print(f"""

        Election Results
    -------------------------
    Total Votes: {total}
    -------------------------
    {candidates[0]}:  {percent[0]}%  ({votes_each[candidates[0]]})
    {candidates[1]}:  {percent[1]}%  ({votes_each[candidates[1]]})
    {candidates[2]}:  {percent[2]}%  ({votes_each[candidates[2]]})
    {candidates[3]}:  {percent[3]}%  ({votes_each[candidates[3]]})
    -------------------------
    Winner: {winner1}
    -------------------------

    """)

file = open('Output/election_file.txt', 'w')

file.write(f'    Election Results\n')
file.write(f'-------------------------\n')
file.write(f'Total Votes: {total}\n')
file.write(f'-------------------------\n')
file.write(f'{candidates[0]}:  {percent[0]}%  ({votes_each[candidates[0]]})\n')
file.write(f'{candidates[1]}:  {percent[1]}%  ({votes_each[candidates[1]]})\n')
file.write(f'{candidates[2]}:  {percent[2]}%  ({votes_each[candidates[2]]})\n')
file.write(f'{candidates[3]}:  {percent[3]}%  ({votes_each[candidates[3]]})\n')
file.write(f'-------------------------\n')
file.write(f'Winner: {winner1}\n')
file.write(f'-------------------------\n')



file.close()


