import os
import csv
#import file
print(os.getcwd())
csvpath = os.path.join("..", "PyPoll", "election_data.csv")
with open(csvpath, newline='') as csvfile:
  csvreader2 = csv.reader(csvfile, delimiter=',')
  #skip header
  csv_header = next(csvreader2)
  candidatelist = []
  total_vote = 0
  vote_cnt = {}
  vote_percent = {}
  #Calculate the total number of votes
  for xrow in csvreader2:
    total_vote += 1
  #Show complete list of candidates who received votes
    if xrow[2] not in candidatelist :
      candidatelist.append(xrow[2])
      vote_cnt[xrow[2]] = 1
    else:
      vote_cnt[xrow[2]] += 1
  print("Election Results")
  print("-------------------------")
  print('Total Votes:', total_vote)
  print("-------------------------")
  #Calculate number of votes each candidate got
  #Calculate percentage of votes each candidate got
  for key, value in vote_cnt.items():
    vote_percent[key] = str(round(((value/total_vote)*100),3)) + "% ("+str(value) + ")"
  #find the winner (candidate with the most votes)  
  winner=max(vote_cnt, key=vote_cnt.get)
  # print(key, value)
  print(vote_percent)
  print("-------------------------")
  print("The Winner: ", winner)
  print("-------------------------")