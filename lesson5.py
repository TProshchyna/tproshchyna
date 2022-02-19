list_1=[(),(1,2,4),(5,6,7),('hi','hello')]

tup=()
print(len(tup))

for i in list_1:
    if len(i) == 0:
        list_1.remove(i)
print(list_1)

##3. Create a list from elements of a range from 700 to 4000 with steps of 130, using list comprehension

list_1=[x for x in range(700,4000,130)]
print(list_1)

##Check if all item in the tuple are the same


list_1=[(),(1,2,4),(5,6,7),('hi','hello')]

##Get only
set1={1,2,3,4,5,5}
set2={6,6,7}
set3=set1|set2
print(set3)





