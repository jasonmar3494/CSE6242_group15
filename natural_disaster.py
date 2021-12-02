import pandas as pd
import math


# use nri_table as the dataframe for data in NRI_Table_Counties_Reduced.csv
df = pd.read_csv('data/natural_disaster/NRI_Table_Counties_Reduced.csv')
column_headers = df.columns.tolist()
nri_table = {}

for row in df.itertuples(index=False):
	fips = row.STCOFIPS
	nri_table[fips] = row

def get_natural_disaster_data():
	# use nri_table as the dataframe for data in NRI_Table_Counties_Reduced.csv
	df = pd.read_csv('data/natural_disaster/NRI_Table_Counties_Reduced.csv')
	column_headers = df.columns.tolist()
	nri_table = {}

	for row in df.itertuples(index=False):
		fips = row.STCOFIPS
		nri_table[fips] = row
	return nri_table

# this function will print out the static dictionary of the data keyed by fips code. Copy pasta to use
def print_data(nri_table, column_headers):
	for fips, row in nri_table.items():
		print(fips, ": {")
		for i, column in enumerate(column_headers):
			if i is not len(column_headers) - 1:
				if isinstance(row[i], str):
					no_quote = row[i].replace("'", "")
					print(f"\'{column}\':\'{no_quote}\', ", end='')
				else:
					if pd.isna(row[i]):
						print(f"\'{column}\':math.nan, ", end='')
					else:
						print(f"\'{column}\':{row[i]}, ", end='')
			else:
				if isinstance(row[i], str):
					no_quote = row[i].replace("'", "")
					print(f"\'{column}\':\'{no_quote}\' ", end='')
				else:
					if pd.isna(row[i]):
						print(f"\'{column}\':math.nan ", end='')
					else:
						print(f"\'{column}\':{row[i]} ", end='')
				
		print(" },")

#print_data(nri_table, column_headers)
print(get_natural_disaster_data())