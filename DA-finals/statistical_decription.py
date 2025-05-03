import csv
def read_csv(filename):
    with open(filename,"r") as f:
        reader=csv.reader(f)
        data=[]
        for row in reader:
            data.append(row)
        return data
data=read_csv('stati.csv')
data=data[0]
a_data=[]
for i in data:
    a_data.append(int(i))
print(a_data)

    

# sum_=0
# median=0
# mode=0
# max_=0
# freq={}
# a.sort()