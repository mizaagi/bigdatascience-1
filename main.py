import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import data_cleaner as dc

df = dc.clean_data('./data/country_wise_latest.csv')
print(df)
sorted_df_confirmed = df.sort_values('Confirmed')
sorted_df_confirmed.plot(x='Confirmed', y='Deaths', marker='o')
plt.savefig('./plots/plot1')