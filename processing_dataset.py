import pandas as pd
import model_traectory
import main

def read_data(file_name: str):
    data = pd.read_csv(file_name)
    start_points = []
    end_points = []
    angele = []
    print (data)
    for index, row in data.iterrows():
        #print (row)
        start_points.append([row['start position x'], row['start position y']])
        end_points.append([row['end position x'], row['end position y']])
        angele.append(row["angele"])    
    return {"start": start_points, "end": end_points, "angele":angele}
