import pandas as pd
import numpy as np
import csv
import os

raw_data_dir = './data/raw'
cleaned_data_dir = './data/cleaned'

raw_data_path = os.path.join(raw_data_dir, '2018 Local Elections.xlsx')

redistricting_processes = pd.read_excel(raw_data_path, 'Redistricting Process')
rep_term_lengths = pd.read_excel(raw_data_path, 'State Representative Term Lengt')
senate_term_lengths = pd.read_excel(raw_data_path, 'State Senate Term Lengths')
governor_term_lengths = pd.read_excel(raw_data_path, 'Governor Term Lengths')
rep_elections = pd.read_excel(raw_data_path, 'State Representative Elections')
senate_elections = pd.read_excel(raw_data_path, 'State Senate Elections')
gubernatiorial_elections = pd.read_excel(raw_data_path, 'Gubernatorial Elections')

"""
Aim is to finish with the follwing relevant columns:
1) has_relevant_elections: bool -- true if this state has relevant elections for 
redistricting in 2018, false otherwise
2) relevant_rep_elections: int -- number of relative elections in the state's rep body
3) total_rep_seats: int -- number of seats in the state's rep body
4) relevant_senate_elections: int -- number of relative elections in the state's senate
5) total_senate_seats: int -- number of seats in the state's senate
6) relevant_gubernatorial_election: bool -- true if this state has a relevant election for
the governorship
"""

state_dict = {}

# Handle redistricting procedures per state
for row in redistricting_processes.iterrows():
	state_dict[row[1]['State']] = {
		'political_redistricting' = row[1]['State'] in row[1]['Redistricting Body']
		if political_redistricting and row[1]['Governor Veto'] == 'Yes':
			'governor_veto' = True
		else if political_redistricting and row[1]['Governor Veto'] == 'No':
			'governor_veto' = False
		else:
			'governor_veto' = None
	}

# Handle rep term lengths per state
for row in rep_term_lengths.iterrows():
	state_dict[row[1]['State']].extend(
		{
			'count' = state_dict[row[1]['Count']]
			'count' = state_dict[row[1]['Term']]
		}
	)

