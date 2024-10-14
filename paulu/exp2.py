import pandas as pd
import numpy as np
a=[]
df=pd.read_csv("exp2.csv")
a=list(df.Data)
x=df.a.mode()
print(x)
print("The dataset",a)
sum_=0
median=0
mode=0
max_=0
freq={}
a.sort()

print("Quartile details: ")
q1=a[int(len(a)*0.25)]
q2=a[int(len(a)*0.5)]
q3=a[int(len(a)*0.75)]

iqr=q3-q1
print("Inter quartile range",iqr)
print("Q0 is :",a[0])
print("Q1 is :",q1)
print("Q2 is :",q2)
print("Q3 is :",q3)
print("Q4 is :",a[-1])
lo=q1-(1.5*iqr)
ho=q3+(1.5*iqr)
print("The Lower outlier is:",lo)
print("The higher outlier is:",ho)
d=[]

for i in a:
	if ( i>ho or i<lo):
		continue
	else:
		d.append(i)
n=len(d)
print("The dataset after eliminating outlier",d)
for i in range(n):
	sum_+=d[i]
	if d[i] in freq:
		freq[d[i]]+=1
	else:
		freq[d[i]]=1



print("Mean of the list is: ",(sum_/n))	
if (n%2)!=0:
	print("The median is ",d[n//2])
else:
	print("The median is",(d[n//2]+d[(n//2)-1])/2)
print("Range of the list is:",d[n-1]-d[0])

modes=[]
max_freq = max(freq.values())
for k,v in freq.items():
	if v==max_freq:
		modes.append(k)
if len(modes)==1:
	print("Mode is UNIMODE:",modes)
elif len(modes)==2:
	print("Mode is BIMODE:",modes)
elif len(modes)==3:
	print("mode is TRIMODE:",modes)
else:
	print("Neither UNIMODE,BIMODE and TRIMODE")

print("variance is",np.var(d))
print("standard deviation is",np.sqrt(np.var(d)))
print("maximum of the dataset after eliminting outlier:",max(d))
print("Minimum of the dataset after eliminating outlier:",min(d))
