print("Adding a new column by passing as series: ")
df['three']=pd.Series([10,20,30], index=['a','b','c'])

print(df)

print("Adding a new column using the existing columns in Dataframe:")
df('four')=df['one']+df['three']