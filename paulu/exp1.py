n=int(input("Enter the number of limit"))
a=[]
sum_=0
median=0
mode=0
max_=0
freq={}
for i in range(n):
	num=int(input("Enter the number: "))
	a.append(num)
a.sort()
for i in range(n):
	sum_+=a[i]
	if a[i] in freq:
		freq[a[i]]+=1
	else:
		freq[a[i]]=1
print("Mean of the list is: ",(sum_/n))	
if (n%2)!=0:
	print("The median is ",a[n//2])
else:
	print("The median is",(a[n//2]+a[(n//2)-1])/2)
#print(freq)
print("Range of the list is:",a[n-1]-a[0])
b=[]
modes=[]
max_freq = max(freq.values())
for k,v in freq.items():
	if v==max_freq:
		modes.append(k)

print("Mode of the list is:",modes)
	




