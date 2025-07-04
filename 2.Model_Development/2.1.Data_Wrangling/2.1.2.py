# Remove Null values
data_frame = data_frame.dropna(subset=['SEX'])
data_frame.isnull().sum()

# Replace Null values with the mean value for the column
data_frame['Target'] = data_frame['Target'].fillna(data_frame['Target'].mean())
data_frame.isnull().sum()

data_frame.duplicated().sum()

data_frame = data_frame.drop_duplicates()
data_frame.duplicated().sum()

data_frame['SEX'] = data_frame['SEX'].apply(lambda x: x.lower())
data_frame['SEX'].head()

data_frame['SEX'].unique()

data_frame['SEX'] = data_frame['SEX'].apply(lambda gender: 'male' if gender.lower() == 'male' else 'female')
data_frame['SEX'].unique()

#get the inter-quartile range on the salary column
print(data_frame['BP'].describe())
Q1 = data_frame['BP'].quantile(0.25)
Q3 = data_frame['BP'].quantile(0.75)
IQR = Q3 - Q1
print(f'Outliers are a BP above {Q3 + IQR * 1.5} or below {Q1 - IQR * 1.5}')

# Filter salaries within the acceptable range
data_frame = data_frame[(data_frame['BP'] >= Q1 - 1.5 * IQR) & (data_frame['BP'] <= Q3 + 1.5 * IQR)]
print(data_frame['BP'].describe())

scale_feature = 'BP'

#the minimum value with space for outliers
MIN_BP = 55

#the maximum value with space for outliers
MAX_BP = 140

#scale features
data_frame[scale_feature] = [(X - MIN_BP) / (MAX_BP - MIN_BP) for X in data_frame[scale_feature]]

data_frame.describe()

#save wrangled data to csv
data_frame.to_csv('../2.2.Feature_Engineering/2.2.1.wrangled_data.csv', index=False)