# Import relevant modules
import os
import csv

# Locate budget_data.csv file
dirname = os.path.dirname(__file__)
election_data_csv = os.path.join(dirname, "Resources", "election_data.csv")

# Initialise variables
total_votes_list = []
total_votes = 0
khan_votes = 0
khan_percent = 0
li_votes = 0
li_percent = 0
correy_votes = 0
correy_percent = 0
otooley_votes = 0
otooley_percent = 0
winner = 0

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        #Total number of votes cast
        total_votes_list.append(row[0])
        total_votes = len(total_votes_list)
        
        # List of candidate names and their total number of votes
        if row[2] == "Khan":
            khan_votes = khan_votes + 1

        if row[2] == "Correy":
            correy_votes = correy_votes + 1

        if row[2] == "Li":
            li_votes = li_votes + 1

        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

        # Percentage votes of each candidate
        khan_percent = "{:.3%}".format(khan_votes / len(total_votes_list))

        correy_percent = "{:.3%}".format(correy_votes / len(total_votes_list))

        li_percent = "{:.3%}".format(li_votes / len(total_votes_list))

        otooley_percent = "{:.3%}".format(otooley_votes / len(total_votes_list))

    # Winner of election
    candidates_list = ["Khan", "Correy", "Li", "O'Tooley"]
    votes_list = [khan_votes, correy_votes, li_votes, otooley_votes]
    winner = max(zip(votes_list, candidates_list))
    
# Print out results to terminal
print(" ")
print(" ")
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'Khan: {khan_percent} ({khan_votes})')
print(f'Correy: {correy_percent} ({correy_votes})')
print(f'Li: {li_percent} ({li_votes})')
print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
print("-------------------------")
print(f'Winner: {winner[1]}')
print("-------------------------")
print(" ")
print(" ")

# Export a text file with the results
# Saving the output file path
output_file = os.path.join(dirname, "Analysis", "Election Results.txt")

# Open the output file, write in results into the txt file
with open(output_file, "w") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Khan: {khan_percent} ({khan_votes})\n')
    txtfile.write(f'Correy: {correy_percent} ({correy_votes})\n')
    txtfile.write(f'Li: {li_percent} ({li_votes})\n')
    txtfile.write(f"O'Tooley: {otooley_percent} ({otooley_votes})\n")
    txtfile.write('----------------------------\n')
    txtfile.write(f'Winner: {winner[1]}\n')
    txtfile.write('----------------------------\n')