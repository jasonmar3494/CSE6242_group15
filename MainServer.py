from flask import Flask, render_template
import pandas as pd
import json
from zillow_rent import *
from FormulaEngine import *

app = Flask(__name__);

@app.route('/')
def main():

	# this is to load the topology file
	f = open("data/us.json",)
	counties = json.load(f)

	property_tax_data = {}
	property_tax_data = FormulaEngine().getProperyTaxData()

	insurance_data = {}
	# load insurance data in one dict
	insurance_data['earthquake'] = FormulaEngine().getEarthquakeInsuranceData()
	insurance_data['flood'] = FormulaEngine().getFloodInsuranceData()
	insurance_data['homeowner'] = FormulaEngine().getHomeOwnersInsuranceData()

	# loading natural disaster data
	natural_disaster_df = pd.read_csv('data/natural_disaster/NRI_Table_Counties_Reduced.csv')

	# loading housing price index
	house_price_df = FormulaEngine().getHomeValueIndexData()

	# loading average rent for each fips
	fips_rent_avg = FormulaEngine().getRentalIndexData()

	# loading crime data for each fips
	fips_crime = FormulaEngine().getCrimeRateIndexData()

	# merging dataframes
	new_df_1 = pd.merge(natural_disaster_df, house_price_df, on="STCOFIPS", how="left")
	new_df_2 = pd.merge(new_df_1, fips_rent_avg, on="STCOFIPS", how="left")
	new_df_3 = pd.merge(new_df_2, fips_crime, on="STCOFIPS", how="left")

	new_df_3 = new_df_3.to_dict(orient='records')
	new_df_3 = json.dumps(new_df_3, indent=2)
	#print(newer_df)

	# pass data via render_template to html file
	return render_template("index.html", fips_keyed_data=new_df_3, insurance_data=insurance_data, property_tax_data=property_tax_data, topo=counties)


if __name__ == '__main__':
	app.run(debug=True);
