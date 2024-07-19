# Import os and csv modules 
import os
import csv

# Establish file path for file 'election_data.csv'
csvpath = os.path.join("Resources","election_data.csv")

# Declare variable to store overall number of votes
voteCount = 0
# Declare dictionary to store candidate names (key) and their respective vote counts
voteTally = {}
# Declare variable to store the highest number of votes by a candidate aka the winner
mostVotes = 0
# Declare a list to store the names of candidates who have the same number of votes
tiedCandidates = []

# Open file 'budget_data.csv'
with open(csvpath) as electionData:
    # Skip row containing the header titles
    next(electionData)
    # Read the contents of 'budget_data.csv' and store it in object dataReader
    dataReader = csv.reader(electionData,delimiter=",")
    # Loop through each row of data
    for row in dataReader:
        # Since each row is a unique vote, the overall number of votes can be calculated by increasing the value of variable voteCount by 1 with each iteration
        voteCount+=1
        
        # Identify who the voter voted for using the 'Candidate' column of the current row.
        # Update the dictionary voteTally by using the identified Candidate as the key and increasing its value by one to represent the added vote.
        # If the Candidate is not yet in the dictionary, add them using the Candidate name as the key and a starting value of 0 which is then increased by 1.        
        voteTally[row[2]] = voteTally.get(row[2],0) + 1


# Declare a function that receives two numbers and returns a calculated percentage, expressed as a number rounded to 3 decimal places
def calculatePercentShare (share, total):
    return round((share/total)*100,3)


# Print output to terminal
# Print the output header titles
print("Election Results")
print("-------------------------")

# Print the Total Votes
print(f"Total Votes: {voteCount}")
print("-------------------------")

# Loop through the dictionary voteTally
for candidate in voteTally:
    # Print candidate data (name, percentage of votes, number of votes) where percentage of votes determined by calling the calculatePercentShare function using the candidate's stored number of votes and variable voteCount
    print(f'{candidate}: {calculatePercentShare(voteTally[candidate],voteCount)}% ({voteTally[candidate]})')

    # Determine the winner or possible tie
    # Identifies first iteration of the loop if mostVotes is still the initial value of 0. If the vote count of the current candidate is greater than the variable mostVotes, assign variable 'tie' as False and set that candidate as the winner.  
    if voteTally[candidate] > mostVotes and mostVotes == 0:
        tie = False
        result = "Winner: " + candidate
        # Update the variable mostVotes to equal the vote count of the current candidate to use in the next iteration
        mostVotes = voteTally[candidate]
        # Add candidate to list tiedCandidates in case a tie occurs with future iterations
        tiedCandidates.append(candidate)
    # If the vote count of the current candidate is greater than the variable mostVotes, assign variable 'tie' as False and set that candidate as the winner.
    elif voteTally[candidate] > mostVotes:
        # Since there is a potential winner identified, delete contents of tiedCandidates since a tie based on the previous data so far isn't possible
        tiedCandidates.pop()
        tie = False
        result = "Winner: " + candidate
        mostVotes = voteTally[candidate]
        # Add candidate to list tiedCandidates in case a tie occurs with future iterations
        tiedCandidates.append(candidate)
    # If the vote count of the current candidate is equal to the variable mostVotes, a tie has potentially occurred.  Set variable tie to True and add the candidate to the list 'tiedCandidates'.  Update the string variable winner to state that a tie has occurred between candidates.
    elif voteTally[candidate] == mostVotes:
        tie = True
        tiedCandidates.append(candidate)
        result = "There is a tie between the following candidates: "
print("-------------------------")

# Print the winner(s) of the election based upon the final value of variable 'tie' coming out of the previous loop
# If 'tie' ends up being False, print the winner of the election
if tie == False:
    print(result)

# If 'tie' ends up being True, print the list of the candidates that tied
elif tie == True:
    print(result + ', '.join(tiedCandidates))
print("-------------------------")

# Write output to a text file
# Determine the output path for file 'election_results.txt'
outputPath = os.path.join("analysis","election_results.txt")

# Open/create file 'election_results.txt'
with open(outputPath,'w') as election_results:

    # Write the output header titles
    election_results.write("Election Results\n")
    election_results.write("-------------------------\n")

    # Write the Total Votes
    election_results.write(f"Total Votes: {voteCount}\n")
    election_results.write("-------------------------\n")

    # Write candidate data (name, percentage of votes, number of votes) where percentage of votes determined by calling the calculatePercentShare function using the candidate's stored number of votes and variable voteCount
    for candidate in voteTally:
        election_results.write(f'{candidate}: {calculatePercentShare(voteTally[candidate],voteCount)}% ({voteTally[candidate]})\n')
    election_results.write("-------------------------\n")

    # Write the winner(s) of the election based upon the final value of variable 'tie' coming out of the earlier loop
    # If 'tie' ends up being False, print the winner of the election
    if tie == False:
        election_results.write(f'{result}\n')
    # If 'tie' ends up being True, print the list of the candidates that tied
    elif tie == True:
        election_results.write(result + ', '.join(tiedCandidates)+"\n")
    election_results.write("-------------------------\n")