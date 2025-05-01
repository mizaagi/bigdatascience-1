# Analysis of country_wise_latest.csv
## Five Number Summary
Confirmed | Deaths | Recovered | ... | Confirmed last week | 1 week change | 1 week % increase
|---|---|---|---|---|---|---|
count | 187.0000000000 | 187.0000000000 | 187.0000000000 | ... | 187.0000000000 | 187.0000000000 | 187.0000000000
mean | 88130.9358288770 | 3497.5187165775 | 50631.4812834225 | ... | 78682.4759358289 | 9448.4598930481 | 13.6062032086
std | 383318.6638306154 | 14100.0024820185  190188.1896431397  ... | 338273.6765665371 | 47491.1276840353 | 24.5098377445
min | 10.0000000000 | 0.0000000000 | 0.0000000000  ... | 10.0000000000 | -47.0000000000 | -3.8400000000
25% | 1114.0000000000 | 18.5000000000 | 626.5000000000  ... | 1051.5000000000 | 49.0000000000 | 2.7750000000
50% | 5059.0000000000 | 108.0000000000 | 2815.0000000000  ... | 5020.0000000000 | 432.0000000000 | 6.8900000000
75% | 40460.5000000000 | 734.0000000000 | 22606.0000000000  ... | 37080.5000000000 | 3172.0000000000 | 16.8550000000
max | 4290259.0000000000 | 148011.0000000000 | 1846641.0000000000 | ... | 3834677.0000000000 | 455582.0000000000 | 226.3200000000

## Correlation of WHO Region and Deaths/100 Cases
One interesting statistic to look at is the correlation of the WHO Region and the average amount of deaths per 100 cases in a certain area. This graph displays the mean of each area's countries' deaths per 100 cases.
![Correlation of WHO Region and Deaths/100 Cases](./plots/plot1.png)
Europe has the highest average deaths per 100 cases, followed by the Eastern Mediterranean region. The two areas that had extremely similar (and low) deaths per 100 cases were Southeast Asia and the Western Pacific. This is most likely because of their geographic closeness.

## 