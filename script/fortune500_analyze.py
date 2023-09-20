import sys
sys.path.append('../lib')
from lib import *

df = pd.read_csv('../data/fortune500.csv')
# Rename the columns for better readability
df.columns = ['year', 'rank', 'company', 'revenue', 'profit']

# Look into the profit column. We only want numbers - use regex as a filter.
non_numberic_profits = df.profit.str.contains('[^0-9.-]')

# Check the invalid value set
set(df.profit[non_numberic_profits])

# Show the distribution of invalid value
bin_sizes, _, _ = plt.hist(df.year[non_numberic_profits], bins=range(1955, 2006))

# Remove the invalid values, then convert all the profit values into numeric for plotting
df = df.loc[~non_numberic_profits]
df.profit = df.profit.apply(pd.to_numeric)

# Check if the length and value types of the dataframe match our expectations
len(df)
df.dtypes

group_by_year = df.loc[:, ['year', 'revenue', 'profit']].groupby('year')
avgs = group_by_year.mean()
x = avgs.index
y1 = avgs.profit
fig, ax = plt.subplots()
plot(x, y1, ax, 'Increase in mean Fortune 500 company profits from 1955 to 2005', 'Profit (millions)')

y2 = avgs.revenue
fig, ax = plt.subplots()
plot(x, y2, ax, 'Increase in mean Fortune 500 company revenues from 1955 to 2005', 'Revenue (millions)')

fig, (ax1, ax2) = plt.subplots(ncols=2)
title = 'Increase in mean and std Fortune 500 company %s from 1955 to 2005'
stds1 = group_by_year.std().profit.values
stds2 = group_by_year.std().revenue.values
plot_with_std(x, y1.values, stds1, ax1, title % 'profits', 'Profit (millions)')
plot_with_std(x, y2.values, stds2, ax2, title % 'revenues', 'Revenue (millions)')
fig.set_size_inches(14, 4)
fig.tight_layout()

# Save the final fig as png
fig.savefig("fig.png")