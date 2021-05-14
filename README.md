# Election_Analysis


##Project Overview

In this challenge, we were tasked with tallying up the votes in three different counties in order to see who the winner was. The 3 counties were Arapahoe, Denver, and Jefferson. In order to do this, we needed to use python to read the csv file and do the counting for us to calculate the amount of votes, and the percentage of votes each candidate received. 
The below are the steps taken
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total # of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
-Data Source: Election_results.csv
-Software: Python 3.7.6, visual studio code, 1.41.1

## Election Audit Summary
The below is a snapshot of the analysis and what story the votes told. There were a total of 369,711 votes, with the highest voter turnout coming from Denver. The percentages per county are also illustrated below. Diana DeGette won the vote by having a majority vote of 73.8%

Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout: Denver
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

This script can be modified in order to do the same analysis on other counties with different candidates. The script already accounts for everything that you need in order to replicate this across different counties & candidates, one of the things that each person running this analysis would have to do is ensure that the results are coming in the same format. If the file that has the information of the votes & candidate names & counties, the user will have to ensure that they are in the same order so the right information can be processed. If there are more columns, and the rows referenced have shifted then this code will have to be amended. " candidate_name = row[2]" For example, currently the candidate names are referencing "row[2]" because in the election_results file, they are located in column 3. Python counts this information starting from 0. So any shift in the data will have to be reflected in the "row[n]" code. Similarly with the vairable to load the file from a path. The new analysis done by said user will have to be modified for the correct file names & folders. Currently, it is referencing my file path as the following: "file_to_load = os.path.join("..", "Resources", "election_results.csv")". This is the same for the "file_to_save" code. The resouces folder could be called "backup" in someone else's computer. Ensuring you have the right folders referenced in the code is going to enable this script to load and save properly. 

