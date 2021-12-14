# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt

n=10000000
arr=np.zeros((n))

for i in range(n):

    x=random.randrange(0,n)
    arr[x]+=1
# y=Counter(arr)
# print(arr)

plt.hist(arr)
plt.xlabel('No of servers having loads as')
plt.ylabel('No of servers')
plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
