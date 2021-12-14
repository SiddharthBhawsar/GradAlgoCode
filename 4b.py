# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt

n=100000
arr=np.zeros((n))

for i in range(n):

    r1=random.randrange(0,n)
    r2 = random.randrange(0,n)
    if(arr[r1]<arr[r2]):


        arr[r1]+=1
    else:
        arr[r2] += 1
# y=Counter(arr)
# print(arr)

plt.hist(arr)
plt.xlabel('No of servers having loads as')
plt.ylabel('No of servers')
plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
