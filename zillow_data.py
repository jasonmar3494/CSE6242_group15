import pandas as pd
import numpy as np

COUNTY_HOUSE_IDX_PATH = 'data/zillow/county_zhvi.csv'
ZIP_HOUSE_IDX_PATH = 'data/zillow/zip_zhvi.csv'
ZIP_RENTAL_IDX_PATH = 'data/zillow/zip_zori.csv'

def get_zillow_data():
	zip_zhvi_data = {}
	fips_zhvi_data = {}

	zip_zori_data = {}

	zip_zhvi_df = pd.read_csv(ZIP_HOUSE_IDX_PATH)
	# print(df)

	for row in zip_zhvi_df.dropna().itertuples(index=False):
		k = "{}_{}".format(row.StateName, str(row.RegionName).zfill(5))
		zip_zhvi_data[k] = row

	county_zhvi_df = pd.read_csv(COUNTY_HOUSE_IDX_PATH)

	for row in county_zhvi_df.dropna().itertuples(index=False):
		state_fips = str(row.StateCodeFIPS).zfill(2)
		county_fips = str(row.MunicipalCodeFIPS).zfill(3)
		k = state_fips + county_fips
		fips_zhvi_data[k] = row

	zip_zori_df = pd.read_csv(ZIP_RENTAL_IDX_PATH)

	for row in zip_zori_df.dropna().itertuples(index=False):
		zip_code = str(row.RegionName).zfill(5)
		state = row.MsaName.split(" ")[-1]
		k = "{}_{}".format(state, zip_code)
		zip_zori_data[k] = row

	return zip_zhvi_data, fips_zhvi_data, zip_zori_data


if __name__ == '__main__':
	zip_zhvi_data, fips_zhvi_data, zip_zori_data = get_zillow_data()
	
	# print(zip_zhvi_data)
	# print(fips_zhvi_data)
	# print(zip_zori_data)

	print(zip_zhvi_data['MA_01470'].ZHVI)
	print(fips_zhvi_data['16025'].ZHVI)
	print(zip_zori_data['IL_60606'].ZORI)

















