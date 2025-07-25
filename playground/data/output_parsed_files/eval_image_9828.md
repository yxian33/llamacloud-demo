

| RegmID | SigBank | RegmName        | RegionType | SigName    | Date            | Value           |
| ------ | ------- | --------------- | ---------- | ---------- | --------------- | --------------- |
| 5454   | 49      | Dest of columns | Static     | NaN        | 2003-1-1-10     | 37.2594.0058553 |
| 1898   | 61      | Wyoming         | NaN        | 2003-1-1-1 | 14459.8050245   |                 |
| 1426   | 27      | Oklahoma        | NaN        | 2023-4-1-0 | 19544.7386510   |                 |
| 1392   | 19      | Ohio            | NaN        | 2018-4-1   | 18338.3822713   |                 |
| 1382.5 | 4       | PennsylVania    | NaN        | 2022-03-1  | 24950.3457474   |                 |
| 1392   | 32      | Nevada          | NaN        | 2013-03-1  | 16793.3782614   |                 |
| 6642   | 35      | Kansas          | NaN        | 2014-10-10 | 11044.1656779   |                 |
| 8144   | 32      | Oregon          | NaN        | 2010-03-1  | 14378.8959406   |                 |
| 1312   | 23      | Alabama         | NaN        | 2011-03-1  | 11540.7.8931177 |                 |
| 8030   | 14      | Massachusetts   | NaN        | 2014-03-30 | 23801.6-14452.1 |                 |
| 7554   | 26      |                 | NaN        | 2017-03-30 |                 |                 |


```python
# MELT Line
df_melt_pd = pd.melt(pd.DataFrame({
    'Query': ['Convert', 'the', 'Date', 'column', 'to', 'datetime', 'format'],
    'df_melt_pd': ['Date'] * 7,
    'var_name': ['Date'] * 7,
    'value_name': ['Value'] * 7
}))

# Convert the Date column to datetime format
df_melt_pd['Date'] = pd.to_datetime(df_melt_pd['Date'])

# Long format
df_melt_pd.sort_values(['Date'], ascending=True)

# RegionType, SigBank, RegionID, SigName, Date
```
