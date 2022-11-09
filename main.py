from discretify_data import discretizise
data_df, bins_df = discretizise()

print(data_df.head(5))
print(bins_df)