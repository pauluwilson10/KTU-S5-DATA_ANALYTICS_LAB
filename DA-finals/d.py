import csv 
from itertools import combinations
with open('apriori.csv','r') as f:
	data=[]
	reader=csv.reader(f)
	for row in reader:
		data.append(row)

    
print(data)
min_support=0.2
min_confidence=0.7
freq={}
for i in range(1,len(data)):
	for j in range(len(data[i])):
		item=(data[i][j],)
		if item in freq:
			freq[item]+=1
		else:
			freq[item]=1


for i in range(1,len(data)):
	for j in range(len(data[i])):
		for k in range(j+1,len(data[i])):
			item=tuple(sorted((data[i][j],data[i][k])))
			if item in freq:	
				freq[item]+=1
			else:
				freq[item]=1

for i in range(1,len(data)):
	for j in range(len(data[i])):
		for k in range(j+1,len(data[i])):
			for l in range(k+1,len(data[i])):
				item=tuple(sorted((data[i][j],data[i][k],data[i][l])))
				if item in freq:	
					freq[item]+=1
				else:
					freq[item]=1
for row in list(freq):
	if freq[row]<min_support:
		del freq[row]
print("frequent set is")
for row in freq:
	print(f"{row}:{freq[row]}")

rules=[]
for itemset in freq:
	if isinstance(itemset,tuple) and len(itemset)>1:
		for i in range(1,len(itemset)):
			for antecedent in combinations(itemset,i):
				consequent=tuple(sorted(set(itemset)-set(antecedent)))
				if len(antecedent)==1:
					antecedent_support=freq[antecedent]
				else:
					antecedent_support=freq[tuple(sorted(antecedent))]
				rule_support=freq[itemset]
				

				confidence=rule_support/antecedent_support
				
				if confidence>=min_support:
					rules.append((antecedent,consequent,confidence))
for i in data:
	print(f"{i[0]}->{i[1]}")
