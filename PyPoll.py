#Open csv file
#Total numbers of votes cast
#a complete list of candidates who received votes
#The percentage of votes each candidate won
#The winner of the election based on popular votes

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("..","Resources","election_results.csv")
#create a file name variable to direct or indirect path to the file
file_to_save = os.path.join("..","analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0 

#Candidate option & candidate votes
candidate_options = []
#Declare a new dictionary
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election data and read the results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the headers
    headers = next(file_reader)
    # print(headers)

    #Print each row in the csv file
    for row in file_reader:
        total_votes = total_votes + 1

        #Print the candidate name from each row
        candidate_name = row[2]
        
        #IF the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add name to list of candidates
            candidate_options.append(candidate_name)
        
            #set count to 0
            candidate_votes[candidate_name]= 0
        #Begin tracking that candidates vote count
        candidate_votes[candidate_name] += 1

           
           
 #Save the results through our text file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes {total_votes:,}\n"
        f"--------------------\n\n"
        f"County Votes:\n")
    print(election_results,end="")

    txt_file.write(election_results)

        #     #1 Iterate through the candidate list
    for candidate_name in candidate_votes:
        #     #Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #Calculate the percentage of votes
            vote_percentage = float(votes)/float(total_votes)*100

        #     #To do: print out each candidate's name, vote count, and percentage of
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print candidate results
            print(candidate_results)

            #save candidate results to our text file
            txt_file.write(candidate_results)
            
        #     #Determine winning vote count and candidate

        #     #Determine if the votes is greater than the winning count.
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                # If true then set winning_count = votes & winning_percent = 
                winning_count = votes
                winning_percentage = vote_percentage
                #And , set the winning candidate equal to the candidate's name
                winning_candidate = candidate_name

            #Print out the winning candidate, vote count and percentage to 
            #terminal

            #Print the candidate name & percentage of votes
            # print(f"{candidate_name}: received {vote_percentage}% of the vote.")

            #print the winning candidate
            winning_candidate_summary = (
                f"-------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning_Percentage: {winning_percentage:.1f}%\n"
                f"-------------------\n")
            print(winning_candidate_summary)
            #save the winning candidate's name to our text file
            txt_file.write(winning_candidate_summary)




   
