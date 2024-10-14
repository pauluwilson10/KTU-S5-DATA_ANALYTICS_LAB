import numpy as np
import pandas as pd
import statistics as st
df=pd.read_csv("exp6.csv")
print(df)
a=list(df["a"])
b=list(df["b"])
print(a)
print(b)
l=len(a)
coef=0
coef_num=0
coef_den=0
covar=0
covar_n=0
mean_a=np.mean(a)
mean_b=np.mean(b)
sd_a=np.sqrt(np.var(a))
sd_b=np.sqrt(np.var(b))
for i in range(l):
	coef_num+=((a[i]-mean_a)*(b[i]-mean_b))
	coef_den+=np.sqrt(((a[i]-mean_a)**2)*((b[i]-mean_b)**2))
coef=coef_num/coef_den
for i in range(l):
	covar_n+=(a[i]-mean_a)*(b[i]-mean_b)
covar=covar_n/l
print(f"Co-realation coefficient between A and B is : {coef}")
if(coef>0):
	print("positive Relation")
elif(coef==0):
	print("No relation")
else:
	print("negative relation")

#print(f"Mean of A : {mean_a}")
#print(f"mean of B : {mean_b}")	
print(f"Co-variance between A and B is : {covar}")
print("Values using Funcions")
print("The covariance is : ")
print(df.cov())
print("The correlation is : ")
print(df.corr())
