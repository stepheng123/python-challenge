# Import Mods
import os
import csv

#set path for file
csvpath = os.path.join("Resources" , "PyPoll_election_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # ignore first row - header
    csvheader = next(csvfile)
    # print(f"header:{header}")

    # set counters to 0
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

# store values in empty list for the variables
    votes = [khan_votes, correy_votes, li_votes, otooley_votes]
    candidates = ["Khan", "Correy", "Li","O'Tooley"]
  
    for row in csvreader:

        # total amount of votes and per canidate
        total_votes = int(total_votes+1)
        if row[2] == "Khan":
            khan_votes = int(khan_votes+1)
        elif row[2] == "Correy":
            correy_votes = int(correy_votes+1)
        elif row[2] == "Li": 
            li_votes = int(li_votes+1)
        elif row[2] == "O'Tooley":
            otooley_votes = int(otooley_votes+1)
 
 
 # find the winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

#put together the list of candidates and the total votes with a zip
candidates_and_votes = dict(zip(candidates,votes))
winner = max(candidates_and_votes, key=candidates_and_votes.get)

# calculate the percentage
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#output the results
print("Election Results")
print("...........................")
print(f"total votes: {total_votes}")
print("...........................")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

# Output to a file
output_file = os.path.join("analysis", "analysis_results.txt")

with open (output_file, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("...........................")
    file.write("\n")
    file.write(f"total votes: {total_votes}")
    file.write("\n")
    file.write("...........................")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")