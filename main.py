import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import data_cleaner as dc

df = dc.clean_data('./data/country_wise_latest.csv')
pd.options.display.float_format = "{:.10f}".format
print(df.describe())
sorted_df_confirmed = df.sort_values('Confirmed')
# plt.figure(figsize=(12,4), dpi=600)
# sorted_df_confirmed.plot(x='Confirmed', y='Deaths', marker='.')
# plt.xlabel('Confirmed Cases')
# plt.ylabel('Deaths')
# ax = sns.barplot(x=sorted_df_confirmed['Confirmed'], y=sorted_df_confirmed['Deaths/100 Cases'], color='slateblue')
# ax.bar_label(ax.containers[0], fontsize=10)

df_whovals = df.groupby('WHO Region')['Deaths/100 Cases'].mean()
ax = sns.barplot(x=df_whovals.index, y=df_whovals.values, color='slateblue')
ax.bar_label(ax.containers[0], fontsize=10)
plt.title("Correlation of WHO Region and Deaths/100 Cases")
plt.ylabel("Deaths/100 Cases")
plt.savefig('./plots/plot1')
