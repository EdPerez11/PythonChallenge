import csv

# Initialized variables, create a counetr, a list, and a dictionary
total_votes = 0
candidates_list = []
candidate_votes = {}

# Open the CSSV file as a read file, create a object for the following loop and skip the header
with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #skip the header
# iterate though the rows to calculate your results
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
      
# As the for loop iterates through the rows, store names in the list we created. When it finds a name that is not in the list, then it will added creating a complete list of candidates.
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
# Increments the number of votes for each candidate in the dictionary
        candidate_votes[candidate_name] += 1

print(f"Total Votes: {total_votes}")
print("List of Candidates who received votes:")
# this line will intialzie the loop that iterates over each key-value pair in candiadte_votes, during each iteration the loop will seperate the key-value pairs into the variables of candidates and votes
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")
for candidate in candidates_list:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Determines the winner by finding the candidate with the maximum votes using the max function
winner = max(candidate_votes, key=candidate_votes.get)
winning_votes = candidate_votes[winner] 

print(f"Winner: {winner} with {winning_votes} votes")

