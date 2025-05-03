import csv
from itertools import combinations

def read_csv(filename):
    data=[]
    with open(filename,'r') as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row)
    return data

data=read_csv('apriori.csv')

min_support=2
min_confidence=0.7

freq={}


for i in range(1,len(data)):
    for j in range(len(data[i])):
        item=(data[i][j],)
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
print(freq)

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
print(list(freq))
for i in list(freq):
    if freq[i]<min_support:
        del freq[i]
for i in freq:
    print(f"{i}:{freq[i]}")


# rules=[]
# for itemset in freq:
#     if isinstance(itemset,tuple) and len(itemset)>1:
#         for i in range(1,len(itemset)):
#             for antecedent in combinations(itemset,i):
#                 consequent=tuple(sorted(set(itemset)-set(antecedent)))
        
#                 if len(antecedent)==1:
#                     antecedent_support=freq[antecedent]
#                 else:
#                     antecedent_support=freq[tuple(sorted(antecedent))]
#                 rule_support=freq[itemset]
#                 confidence=rule_support/antecedent_support
#                 if confidence<=min_confidence:
#                     rules.append((antecedent,consequent,confidence))


# print("Association Rules:")
# print(rules)
# for rule in rules:
#     print(f"{rule[0]}->{rule[1]}")


rules=[]
for itemset in freq:
	if isinstance(itemset,tuple) and len(itemset)>1:
		for i in range(1,len(itemset)):
			for antecedent in combinations(itemset,i):
				consequent=tuple(sorted(set(itemset)-set(antecedent)))
				if len(antecedent)==1:
					min_support=freq[antecedent]
				else:
					min_support=freq[tuple(sorted(antecedent))]
				rule_support=freq[itemset]
				confidence=rule_support/min_support
				
				if confidence>=min_confidence:	
					rules.append((antecedent,consequent,confidence))
print("\n")
print("associatioon rules")
for i in rules:
	print(f"{i[0]}->{i[1]}")
			
