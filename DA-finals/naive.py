import csv

def read_file(filename):
    data=[]
    with open(filename,'r') as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row)
    return data
data=read_file('n.csv')

req=[['age','youth'],['income','medium'],['student','yes'],['credit_rating','fair']]
yesno=[[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]

pyes=0.0
pno=0.0
yescount=0
nocount=0

for i in range(1,len(data)):
    if data[i][5]=='yes':
        yescount+=1
    else:
        nocount+=1
pyes=yescount/(len(data)-1)
pno= nocount/(len(data)-1)
print(pyes)
print(pno)

for i in range(4):
    r_index=0
    for j in range(6):
        if(req[i][0]==data[0][j]):
                r_index=j
                break
    val=req[i][1]
    # t_count=0
    # for k in range(1,len(data)):
    #     if(data[k][r_index]==val):
    #         t_count+=1
    p_req_yes=0
    p_req_no=0
    for k in range(1,len(data)):
        if(data[k][r_index]==val and data[k][5]=="yes"):
            p_req_yes+=1
        elif(data[k][r_index]==val and data[k][5]=="no"):
            p_req_no+=1
        
    p_req_yes/=yescount
    p_req_no/=nocount

    yesno[i][0]=p_req_yes
    yesno[i][1]=p_req_no

theyes=yesno[0][0]*yesno[1][0]*yesno[2][0]*yesno[3][0]*pyes
theno=yesno[0][1]*yesno[1][1]*yesno[2][1]*yesno[3][1]*pno

finalyes='no'

if theyes>theno:
    finalyes='yes'

print("Probability Table:") 
print(yesno)
print("Probability for yes: ",theyes)
print("Probability for no: ",theno)
print("Predicted class_buys_book for [youth,medium,yes,fair]: ",finalyes)




