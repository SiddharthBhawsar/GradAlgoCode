import random
skills=[]
person=[]
for i in range(500):
    skills.append(i)
for i in range(500):
    person.append((random.sample(skills, 25)))

print (person)

