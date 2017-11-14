# ## Option 2: PyPoll
# ![Vote-Counting](Images/Vote_counting.jpg)
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:

# ```
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

import os
import csv
import pandas as pd
import glob

cols = ["Voter ID", "County", "Candidate"]

names = pd.DataFrame()
for i in glob.glob('PyPoll/*.csv', recursive=True):
    #print(i)
    df = pd.read_csv(i, header = None, skiprows=[0],names = cols)
print(df)

total_votes = len(df)
df_candidates = df.loc[:,'Candidate']

#df_candidates.shape

candidate_votes = df.groupby('Candidate').count()
winner = candidate_votes['County'].argmax() 

cand0_percent = str(round((candidate_votes['County'][0] / total_votes * 100) ,1))
cand1_percent = str(round((candidate_votes['County'][1] / total_votes * 100) ,1))
cand2_percent = str(round((candidate_votes['County'][2] / total_votes * 100) ,1))
cand3_percent = str(round((candidate_votes['County'][3] / total_votes * 100) ,1))

print(
      "Election Results \n" +
      "---------------------- \n" +
      "Total Votes: " + str(total_votes) +
      "---------------------- \n" +
      str(candidate_votes.index[0]) + ': ' + cand0_percent + '% ' + ' (' + str(candidate_votes['County'][0]) + ')' +"\n" + 
      str(candidate_votes.index[1]) + ': ' + cand1_percent + '% ' + ' (' + str(candidate_votes['County'][1]) + ')' +"\n" +
      str(candidate_votes.index[2]) + ': ' + cand2_percent + '% ' + ' (' + str(candidate_votes['County'][2]) + ')' +"\n" +
      str(candidate_votes.index[3]) + ': ' + cand3_percent + '% ' + ' (' + str(candidate_votes['County'][3]) + ')' +"\n" +
      "---------------------- \n" +
      "Winner: " + winner +  "\n" +
      "---------------------- \n" 

      )