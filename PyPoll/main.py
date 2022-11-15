#PyPoll Instruction
#-------------------------------------------------------------------------------------------------------
#The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
#--------------------------------------------------------------------------------------------------------
# Import dependables
#--------------------------------------------------------------------------------------------------------
# #import os
import os
#import csv
import csv
#import collection
import collections
from collections import Counter
# Define and assign PyPoll's variables
vc = []
vpc = []
# Change directory to the directory of the current python script to enable read
os.chdir(os.path.dirname(__file__))
# Set path for files
election_data = os.path.join("Resources", "election_data.csv")
# Open and read csv, encoding ='utf-8' as csv file
with open(election_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
# Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    for row in csv_reader: 
        # print(row)
        vc.append(row[2])
        # print(v_candidates)
# Sort the list by default ascending order
    sorted_list = sorted(vc)
    
    # Arrange the sorted list by most common outcomes for the candidates
    arrange_list = sorted_list

    #number of votes/candidate for most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    vpc.append(count_candidate.most_common())

    # Compute % of votes per candidate in 3 digital places!!!
    for item in vpc:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
#-----------------------------------------------------------------------------------------------------
#Print the analysis to the terminal------------------------------------------------------------------>
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{vpc[0][1][0]}: {second}% ({vpc[0][1][1]})")
print(f"{vpc[0][0][0]}: {first}% ({vpc[0][0][1]})")
print(f"{vpc[0][2][0]}: {third}% ({vpc[0][2][1]})")
# print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {vpc[0][0][0]}")
print("-------------------------")
#------------------------------------------------------------------------------------------------------>
#  Export a text file with the results----------------------------------------------------------------->
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{vpc[0][1][0]}: {second}% ({vpc[0][1][1]})\n")
    outfile.write(f"{vpc[0][0][0]}: {first}% ({vpc[0][0][1]})\n")
    outfile.write(f"{vpc[0][2][0]}: {third}% ({vpc[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {vpc[0][0][0]}\n")
    outfile.write("-------------------------\n")    