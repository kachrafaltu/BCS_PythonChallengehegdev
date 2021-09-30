# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# initialize candidate_votes and county_votes as empty dictionories
candidate_votes = dict()
county_votes = dict()
current_county = ""
current_candidate = ""
count_candidates=0
count_counties=0
candidates = list()
candidate_vote_counts = list()
counties = list()
county_vote_counts=list()
counties = list()
winner = ""
winner_votes=0
total_votes = 0

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
#        print(row)
        
        current_candidate = row[2]
        current_county = row[1]
        if current_candidate in candidate_votes:
            candidate_votes[current_candidate]= candidate_votes[current_candidate]+1
        else:
            candidate_votes[current_candidate] = 1

        if current_county in county_votes:
            county_votes[current_county]= county_votes[current_county]+1
        else:
            county_votes[current_county] = 1
    
#    print(candidate_votes)
#    print(county_votes)

# we are assuming that the data model is as shown below
# Candidates can receive votes from voters located in many counties
# we need to get votes received by 
# We therefore will try to get the following structures
# Candidates {"Candidate1":VoteCount, "Candidate2":votecount}
# and County {"County1":VoteCount, "County2":VoteCount}

for contestant in candidate_votes:
    candidates.append(contestant)
    candidate_vote_counts.append(candidate_votes[contestant])
    count_candidates=count_candidates+1

for county in county_votes:
    counties.append(county)
    county_vote_counts.append(county_votes[county])
    count_counties=count_counties+1

#print(candidates)


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# Specify the file to write to
output_path =  "output.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(".\Analysis\output.txt", 'w') as outfile:
    total_votes = sum(candidate_vote_counts)
    print("-------------------------")
    outfile.write("-------------------------\n")
    print("Total Votes : ", total_votes)
    outfile.write(f"Total Votes : {total_votes}\n")
    print("-------------------------")
    outfile.write("-------------------------\n")

    for i in range(len(candidates)):
        if candidate_vote_counts[i] > winner_votes:
            winner = candidates[i]
            winner_votes = candidate_vote_counts[i]
        print(f" {candidates[i]} : {candidate_vote_counts[i]*100/total_votes:3.3f} % ({candidate_vote_counts[i]})")
        outfile.write(f" {candidates[i]} : {candidate_vote_counts[i]*100/total_votes:3.3f}  % ({candidate_vote_counts[i]})\n")
    print("-------------------------")
    outfile.write("-------------------------\n")
    print(f"Winner :  {winner} with {winner_votes} votes")
    outfile.write(f"Winner :  {winner} with {winner_votes} votes\n")
    print("-------------------------")
    outfile.write("-------------------------\n")
