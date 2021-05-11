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


#open the election results and read the file
# election_data =open(file_to_load,'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the headers
    headers = next(file_reader)
    print(headers)
    

    # to do: perform analysis
    # print(election_data)
    # file_reader = csv.reader(election_data)
    #Print each row in the csv file
    # for row in file_reader:
    #     print(row)

    # #close the file:
    # election_data.close()

# #create a file name variable to direct or indirect path to the file
file_to_save = os.path.join("..","analysis", "election_analysis.txt")
# #Using the open() function with the "W" mode we will write data to the file
# with open(file_to_save,"w") as txt_file:
#     #write some data in the file
#     txt_file.write("Counties in the Election\n------------------------\nArapaho\nDenver\nJefferson")
# #Close the file
# txt_file.close()

#Open the election results and read the file






   
