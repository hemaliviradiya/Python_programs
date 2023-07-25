tuple1 = (1,2,5.0,"Hello")
#tuple[0]=11
#******for run append write type(mylist)in commnad line***********#
tuple.append(100)
print(tuple1[-1])

O/P :-
type(mylist)
list

----------------------------------------------------------
mylist = [10,20,30,40,50,60,70,80,90]
l1=sorted(mylist)
print(l1)

O/P :-
[10, 20, 30, 40, 50, 60, 70, 80, 90]

-----------------------------------------------------

mylist = [10,20,30,40,50,60,70,80,90]
#l1=sorted(mylist)
for i in mylist:
  print(i*2)

O/P :-
20
40
60
80
100
120
140
160
180


--------------------------Dictionary---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program"}
print(mydict)

O/P :-
{'A': 'Hello', 'B': 'Python', 'c': 'Program'}

--------------------------First letter print---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program",3:2.5}
print(mydict['A'])

O/P :-
Hello

--------------------------Dictionary keys---------------------------
mydict = {'A':"Hello",'B':"Python",'c':"Program",3:2.5}
print(mydict.keys())
  
O/P :-
dict_keys(['A', 'B', 'c', 3])

--------------------------Dictionary values---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program",3:2.5}
print(mydict.values())

O/P :-dict_values(['Hello', 'Python', 'Program', 2.5])

--------------------------Nested Dictionary---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program",3:{1:10,2:50,4:10}}
print(mydict.values())
  
O/P :-
dict_values(['Hello', 'Python', 'Program', {1: 10, 2: 50, 4: 10}])

--------------------------get any index of dictionary---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program",3:{1:10,2:50,4:10}}
print(mydict[3])

O/P :-
{1: 10, 2: 50, 4: 10}


--------------------------Remove Item---------------------------

mydict = {'A':"Hello",'B':"Python",'c':"Program",3:{1:10,2:50,4:10}}
del(mydict[3])
print(mydict)

O/P :-
{'A': 'Hello', 'B': 'Python', 'c': 'Program'}

--------------------------get value---------------------------

mydict=dict()
mydict={'A':"Hello"}
print(mydict)

O/P :-
{'A': 'Hello'}
--------------------------empty function---------------------------
mydict=dict()
print(mydict)

O/P :-
{}

--------------------------get value using get method---------------------------

mydict=dict()
mydict={'A':"Hello"}
print(mydict.get('A'))

O/P :-
Hello

--------------------------set method---------------------------
S1 = {1,2,3,4,5,6,7,8}
print(S1)

O/P :-
{1, 2, 3, 4, 5, 6, 7, 8}

--------------------------union of set method---------------------------

S1 = {1,2,3,4,5,6,7,8}
S2 = {2,6,7,8,10,12,15}
print(S1.union(S2))

O/P :-
{1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15}

--------------------------intersection of set method---------------------------

S1 = {1,3,4,5,6,7,8}
S2 = {2,6,7,8,10,12,15}
print(S1.intersection(S2))

O/P :-
{8, 6, 7}

--------------------------Difference of set method---------------------------

S1 = {1,3,4,5,6,7,8}
S2 = {2,6,7,8,10,12,15}
print(S1.difference(S2))
print(S2.difference(S1))
O/P :-
{1, 3, 4, 5}

--------------------------symmetric Difference of set method---------------------------
S1 = {1,3,4,5,6,7,8}
S2 = {2,6,7,8,10,12,15}
print(S1.symmetric_difference(S2))

O/P :-
{1, 2, 3, 4, 5, 10, 12, 15}

--------------------------symmetric Difference of set method---------------------------


