import pandas as pd
from scipy.stats import chi2_contingency #import scipy.stats from chi2_contingency

df=pd.read_csv("exp6A.csv")
Table_contingency=pd.crosstab(df['val'],df['val2'])
stat,pval