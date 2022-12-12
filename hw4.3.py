a =[1, 2 ,3 , 4 ,5 ,6]
b = [9,10,12,3,5]
c = []
d = []
e = []
for i in range (len(a)):
    count =0
    for j in range(len(b)):
        if(a[i]==b[j]):
            count+=1
            print(a[i],b[j])
    if(c.count(a[i])==0 and count>0):
        c.append(a[i])
for i in range (len(a)):
    if(c.count(a[i])==0):
        d.append(a[i])
for i in range (len(b)):
    if(c.count(b[i])==0):
        e.append(b[i])
print("в обоих списках:",c)
print("в первом списке:",d)   
print("в во втором списке:",e)   
print("в только в первом или во втором списках:",d+e)           

