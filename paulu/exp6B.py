"""import pandas as pd
import numpy as np
n=1500
df=pd.read_csv("exp7.csv")
male=list(df["male"])
male_t=male[-1]
female=list(df["female"])
female_t=female[-1]
print(df)
fic_tot=df.at[0, 'total']
non_fic_tot=df.at[1,'total']
male_tot=df.at[2,'male']
female_tot=df.at[2,'female']
print(fic_tot,non_fic_tot,male_tot,female_tot)
import pandas as pd
from scipy.stats import chi2_contingency
data=pd.read_csv("exp7.csv")
print(data)
contingency_table=pd.crosstab(data["row1"],data["row2"])
chi2,p,x,y=chi2_contingency(contingency_table)
print("Chi-value is : ",chi2)
print("P value is : " ,p)
"""

import pandas as pd
import numpy as np
df=pd.read_csv("exp7.csv")
observed=df.values
print(observed)
row_sum=np.sum(observed,axis=1)
col_sum=np.sum(observed,axis=0)
grand_total=np.sum(observed)
expected=np.zeros(observed.shape)
for i in range(observed.shape[0]):
        for j in range(observed.shape[1]):
            expected[i,j]=((row_sum[i]*col_sum[j])/grand_total)
print("Expected values:")
print(expected)
chi=np.sum((observed-expected)**2/expected)
print("chi square values: ",chi)
print("degree of freedom",(observed.shape[0]-1)*(observed.shape[1]-1))

if chi>10.8:
    print("There is a corelation")
else:
    print("There is no correlation")
    
