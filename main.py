# This is a sample Python script.
import random
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
lst=[]
population=10000000
a=['A']*(population*52)
b=['B']*(population*48)
countA=0
countB=0
lst=a+b
finalst=[]
samplesize=800
for i in range(100):
    result=random.sample(lst,samplesize)
    temp=[]
    # concate=list()+list(result.count(1))
    temp.append(result.count('A'))
    temp.append(result.count('B'))
    finalst.append(temp)
for i in finalst:
    if(i[0]>i[1]):
        countA+=1
    elif(i[0]<=i[1]):
        countB+=1
prob=countA/(countB+countA)
print(prob)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
