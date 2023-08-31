import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open("data/36_44201from19810101to19810227_AQdata.json", 'r') as json_file:
    data = json.load(json_file)
    # data = data["Data"][0:5]

    average_pm_concentration = []

    sorted_data = sorted(data['Data'], key=lambda x: x['date_local'])
    # for sample in sorted_data:
    #     print(sample["pollutant_standard"])
    #     print(sample["units_of_measure"])
    #     print(sample["arithmetic_mean"])
    #     print(sample["date_local"])
    #     try:
    #         average_pm_concentration.append(float(sample["arithmetic_mean"]))
    #     except:
    #         continue


method_dataframes = []

for entry in data['Data']:
    method = entry['method']
    date = pd.to_datetime(entry['date_local'])
    value = entry['arithmetic_mean']

    # Check if a DataFrame for this method already exists
    existing_df = next((df for df in method_dataframes if df['method'].iloc[0] == method), None)
    # print(existing_df)
    # If a DataFrame exists, append the data to it; otherwise, create a new DataFrame
    if existing_df is not None:
        existing_df = pd.concat([existing_df, pd.DataFrame({'date_local': [date], 'method': [method], 'arithmetic_mean': [value]})], ignore_index=True)
        method_dataframes = [df if df['method'].iloc[0] != method else existing_df for df in method_dataframes]
    else:
        new_df = pd.DataFrame({'date_local': [date], 'method': [method], 'arithmetic_mean': [value]})
        method_dataframes.append(new_df)

desired_method = "INSTRUMENTAL - CHEMILUMINESCENCE"
for df in method_dataframes:
    df.plot(x='date_local', y='arithmetic_mean', kind='scatter')
    mean_df = df.groupby(['date_local', 'method'])['arithmetic_mean'].mean().reset_index()
    mean_df.plot(x='date_local', y='arithmetic_mean', kind='line')
    plt.show()
