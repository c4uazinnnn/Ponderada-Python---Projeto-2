import pandas as pd

column_names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']

df = pd.read_csv('adult.data.csv', header=None, names=column_names, skipinitialspace=True)
print('dtypes:')
print(df.dtypes)
print('\nhead (first 10 rows):')
print(df.head(10).to_string())
print('\nage column unique sample values:')
print(df['age'].astype(str).head(20).to_list())
print('\nsex column unique values:')
print(df['sex'].unique().tolist())
print('\nshape:', df.shape)
