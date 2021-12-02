import pandas as pd
import json
import math

def get_fips_to_rent_avg():
	rent_df = pd.read_csv('data/zillow/zip_zori.csv')
	rent_df = rent_df.drop(['RegionID','SizeRank','MsaName'], axis=1)


	zipToFips_df = pd.read_csv('data/ziptofips.csv')
	zipToFips_df = zipToFips_df.drop(['COUNTYNAME','STATE','CLASSFP'], axis=1)


	zip_to_rent = {}
	zip_to_rent = rent_df.set_index('RegionName').to_dict()

	fips_to_rent = {}
	for row in rent_df.itertuples():
		fips_list = zipToFips_df.loc[zipToFips_df["ZIP"] == row.RegionName, 'STCOUNTYFP'].values
		for fips in fips_list:
			if fips in fips_to_rent:
				fips_to_rent[fips].append(row.ZORI)
			else:
				fips_to_rent[fips] = [row.ZORI]

	fips_to_rent_avg = {}
	for fips, rent_prices in fips_to_rent.items():
		fips_to_rent_avg[fips] = round(sum(rent_prices) / len(rent_prices), 2)

	out_df = pd.DataFrame(fips_to_rent_avg.items(), columns=["STCOFIPS", "RENT_AVG"])

	return out_df