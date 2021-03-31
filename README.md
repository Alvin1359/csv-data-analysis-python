# Python Challenge
A repository containing Python Challenge homework  
  
Each analysis contains three items:
- A file called main.py. This is the main script to run for each analysis.
- A "Resources" folder that contains the CSV files used
- An "Analysis" folder that contains a text file that has the results from the analysis.

**Modules used:**
- import os
- import csv

**IDE created with:**
- Visual Studio Code (VSC)

**The following code included in each _main.py_ should ensure the python file runs on VSC:**
```
dirname = os.path.dirname(\__file__\)
(csv file name)_csv = os.path.join(dirname, "Resources", "(csv file name.csv")
```

## PyBank
- This challenge involves analysing the financial records of a company
- The csv file "_Budget_data.csv_" is a dataset composed of two columns: _Date_ and _Profit/Losses_
- The _main.py_ script calculates:
  - Total number of months in the dataset
  - Net Profit/Loss over the period
  - Average change in Profit/Loss
  - Greatest increase in profit
  - Greatest decrease in loss
- The following outout is achieved in the terminal as well as a .txt file:
  ![image](https://user-images.githubusercontent.com/79504423/113161126-aceae600-9270-11eb-8830-15d8f7b05075.png)



## PyPoll
- This challenge involves analysing a vote counting process
- The csv file "_election_data.csv_" is a dataset composed of three columns: _Voter ID_, _County_ and _Candidate_
- The _main.py_ script calculates:
  - Total number of votes cast
  - List of candidates who have received votes
  - Percentage votes of each candidate
  - Number of votes of each candidate
  - Winner based on who has the maximum amount of votes
- The following output is achieved in the terminal as well as a .txt file:
   ![image](https://user-images.githubusercontent.com/79504423/113161393-ec193700-9270-11eb-85e5-2c1ea3af35cf.png)
