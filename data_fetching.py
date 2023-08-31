import json
import requests
import time

# sign_up_url = "https://aqs.epa.gov/data/api/signup?email=lorenzoschneiderman@gmail.com"
# AQI: OZONE (44201), Size fractionated particulate (81101), carbon monoxide (42101), Sulfur dioxide (42401), nitrogen dioxide (42602)

def fetch_data(url, path):
    response = requests.get(url)
    data = response.json()

    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)


email = "lorenzoschneiderman@gmail.com"
key = "amberram24"
api_base_url = "https://aqs.epa.gov/data/api/dailyData/byState?email="
# param_codes = ["44201","81101","42101","42401","42602"]
param_codes = "44201,81101,42101,4240,42602"



def build_database_locally(end_year, param_codes, state_codes):
    for s_code in state_codes:
        for s in state_codes:
            for time_span in range(1980, end_year):
                begin_date = str(time_span) + "01" + "01"
                end_date = str(time_span) + "02" + "27"
                
                sample_data_url = api_base_url + email + "&key=" + key + "&param=" + param_codes + "&bdate=" + begin_date + "&edate=" + end_date + "&state=" + s_code
                sample_data_path = "data/" + s_code + "_" + param_codes + "from" + begin_date + "to" + end_date + "_AQdata.json"
                
                fetch_data(sample_data_url, sample_data_path)
                time.sleep(10)

state_codes = ["36"]
end_year = 1983
build_database_locally(end_year, param_codes, state_codes)
