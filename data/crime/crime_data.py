import pandas as pd
import json

def load_crime_df(fpath):
    crime_df = pd.read_excel(fpath, header=4)
    crime_df.State = crime_df.State.fillna(method='ffill')
    crime_df.State = crime_df.State.str.split(' - ').str[0]
    crime_df.Arson1 = crime_df.Arson1.fillna(0)
    crime_df = crime_df.iloc[:-7] # remove notes
    crime_df = crime_df.rename(columns={i : i.lower().replace(' ', '_').replace('\n', '') for i in crime_df.columns})
    crime_df.state = crime_df.state.str.lower()

    crime_df.county = crime_df.county.str.lower().str.replace('[\.\'\d+]', '')
    crime_df.county = crime_df.county.str.replace(' county', '').str.replace(' police department', '')
    crime_df.county = crime_df.county.str.replace(' bureau of police', '').str.replace(' public safety', '')
    crime_df.county = crime_df.county.replace({'augusta-richmond' : 'richmond', 'hartsville/trousdale' : 'trousdale'})

    crime_df = crime_df.groupby(['state', 'county']).sum()
    return crime_df

def load_fips_df(fpath):
    fips_df = pd.read_excel(fpath, header=1)
    fips_df.State = fips_df.State.str.lower()
    fips_df['County Name'] = fips_df['County Name'].str.lower()
    fips_df = fips_df.rename(columns={i : i.lower().replace(' ', '_').replace('\n', '') for i in fips_df.columns})
    fips_df['fips'] = fips_df.fips_state.astype(str).apply('{:0>2}'.format) + fips_df.fips_county.astype(str).apply('{:0>3}'.format)
    return fips_df

def get_crime_data(crime_fpath, fips_fpath, return_df=False):
    crime = load_crime_df(crime_fpath)
    fips_df = load_fips_df(fips_fpath)
    crime_merge = pd.merge(crime, fips_df, how='left', left_on=['state', 'county'], 
                        right_on=['state', 'county_name'])
    crime_merge = crime_merge.rename(columns={'county_name': 'county'})
    crime_merge = crime_merge[['fips', 'state', 'county', 'fips_state', 'fips_county',
        'violent_crime', 'murder_and_nonnegligent_manslaughter',
       'forcible_rape', 'robbery', 'aggravated_assault', 'property_crime',
       'burglary', 'larceny-theft', 'motor_vehicle_theft', 'arson1']]
    if return_df:
        return crime_merge
    return crime_merge.set_index('fips').to_dict('index')

if __name__ == "__main__":
    data = get_crime_data('crime_tbl10.xls', 'US_FIPS_Codes.xls')
    with open('crime.json', 'w') as file:
        file.write(json.dumps(data))