import numpy as np
import pandas as pd
import os

FILENAME = "final_data_set.csv"

df = pd.read_csv("data31.csv")
df.head()
df.columns = ['waste']
df_done = df.waste.str.split(',', n=1, expand=True)
df_done.columns = ['polarity', 'text']
if not os.path.exists(FILENAME):
    df_done.to_csv(FILENAME)
print("done")