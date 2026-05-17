
n=[1,2,1,3,4,5,5,6,2]
result=[]
for i in n:
    if n.count(i) ==1:
        result.append(i)
print(result)
