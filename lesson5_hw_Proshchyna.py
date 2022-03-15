#Task 1
#The greatest number

import random

count=0
list_1=[]
while count<10:
    list_1.append(random.randint(1,1000))
    count+=1
print(list_1)
max_value=max(list_1)
print(f'The max number in the list {list_1} is {max_value}')

#Task 2
#Exclusive common numbers

count_1=0
list_1=[]
while count_1<10:
    list_1.append(random.randint(1,10))
    count_1+=1

count_2=0
list_2=[]
while count_2<10:
    list_2.append(random.randint(1,10))
    count_2+=1

print(list_1)
print(list_2)

set_1=set(list_1)
set_2=set(list_2)
list_3=list(set_1&set_2)

print(f'The common list of element between list_1 and list_2 is {list_3}')

#Task 3
#Extracting numbers

list_integers=list(range(1,101))
count=0
new_list_integers=[]

while count<len(list_integers):
    for i in list_integers:
        count+=1
        if i % 7 == 0 and i % 5 !=0:
            new_list_integers.append(i)
        else:
            continue
print(new_list_integers)





