import pandas as pd
import json
import InsuranceDataService
import data.PropertyTax as PropertyTax

class FormulaEngine:

    def getFloodInsuranceData(self):
        return InsuranceDataService.FloodInsuranceMap

    def getEarthquakeInsuranceData(self):
        return InsuranceDataService.EarthquakeInsuranceMap

    def getHomeOwnersInsuranceData(self):
        return InsuranceDataService.HomeOwnersInsuranceMap

    def estimateInsuranceCost(self):
        relevant_cols = ['STATE',
                        'COUNTY',
                        'STCOFIPS',
                        'RISK_SCORE', # National Risk Index - Score - Composite
                        'EAL_SCORE', # Expected Annual Loss - Score - Composite
                        'FLD_EALS', # Flooding - Expected annual loss score
                        'ERQK_EALS', # Earthquake - Expected annual loss score
                        'HRCN_EALS', # Hurricane - Expected annual loss score
                        'TRND_EALS' # Tornado - Expected annual loss score
                        ]
        scores = ['RISK_SCORE', 'EAL_SCORE', 'FLD_EALS',  'ERQK_EALS','HRCN_EALS','TRND_EALS']
        df = pd.read_csv('data/natural_disaster/NRI_Table_Counties.csv')
        df['FLD_EALS'] = df.CFLD_EALS.fillna(0) + df.RFLD_EALS # combine river and coastal flooding

        df = df[relevant_cols]

        # transform scores to weights for cap rate calc, right now just % of mean I guess
        mean = df.groupby(['STATE'])[scores].transform('median')
        #std = df.groupby(['STATE'])[scores].transform('std')
        df[scores] = df[scores]/mean

        flood_cost = df['STATE'].map(self.getHomeOwnersInsuranceData())
        HOI_cost =  df['STATE'].map(self.getHomeOwnersInsuranceData())
        EQ_cost = df['STATE'].map(self.getEarthquakeInsuranceData())

        df['insurance_cost'] = flood_cost * df['FLD_EALS'] + HOI_cost * (1 + (df['TRND_EALS'] + df['HRCN_EALS'])/2) + EQ_cost * df['ERQK_EALS']
        # lots of nas when combined with housing data....
        return df
        #return df.set_index('STCOFIPS').to_dict(orient='index')

    def getHomeValueIndexData(self):
        hpi_df = pd.read_csv('data/zillow/fips_house_price_index.csv')
        new_hpi_df = hpi_df[hpi_df.Year == 2020]
        new_hpi_df = new_hpi_df.drop(['Year'], axis=1)
        return new_hpi_df

    def getIncomeValueIndexData(self):
        return

    # return dataframe with STCOFIPS, RENT_AVG
    def getRentalIndexData(self):
        rent_df = pd.read_csv('data/zillow/fips_to_rent.csv')
        return rent_df

    # return dataframe with STCOFIPS, CRIME_DATA
    def getCrimeRateIndexData(self):
        f = open("data/crime/crime.json",)
        crime = json.load(f)
        df = pd.DataFrame(crime.items(), columns=['STCOFIPS', 'CRIME_DATA'])
        dtypes = {'STCOFIPS': 'int64', 'CRIME_DATA' : 'object'}
        df = df.astype(dtypes)
        return df

    def getFipToCountyAndStateMapping(self):
        return;

    def getHOAData(self):
        return 0;
    def getProperyTaxData(self):
        return PropertyTax.PropertyTaxMap;
