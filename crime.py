import json

CRIME_DATA_PATH = 'data/crime/crime.json'
FIPS_DATA_PATH = 'data/crime/fips2state.json'

crime = json.load(open(CRIME_DATA_PATH))
fips2state = json.load(open(FIPS_DATA_PATH))
state2fips = {v: k for k, v in fips2state.items()}

if __name__ == '__main__':
    print(crime["01001"])
    print(fips2state["01"])
    print(state2fips['alabama'])