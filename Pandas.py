------------------------------1D array series number using panda-------------------------

import pandas as pd
s1=pd.Series([2,.4,6,8,10])
print(s1)

O/P :-
0     2.0
1     0.4
2     6.0
3     8.0
4    10.0
dtype: float64

2nd method:--------

import pandas as pd

s1=pd.Series([2,4,6,8,10])
print(s1)

O/P :-
0     2
1     4
2     6
3     8
4    10
dtype: int64

------------------------------1D array series number using string datatype in  panda-------------------------

import pandas as pd
s1=pd.Series(["PYTHON","Program"])
print(s1)

O/P :-
0     PYTHON
1    Program
dtype: object

------------------------------1D array series number using mix datatype in  panda-------------------------
import pandas as pd
s1=pd.Series([5,10,"PYTHON","Program"])
print(s1)

O/P :-
0          5
1         10
2     PYTHON
3    Program
dtype: object

------------------------------1D array series number using array datatype in  panda-------------------------

import pandas as pd
s1=pd.Series([[5,10],[20,25],[30,40]])
print(s1)

O/P :-
0     [5, 10]
1    [20, 25]
2    [30, 40]
dtype: object

------------------------------1D array series number using own datatype in  panda-------------------------
import pandas as pd
s1=pd.Series(data=[5,10,15,20],index=['A','B','C','D'])
print(s1)

O/P :-
A     5
B    10
C    15
D    20
dtype: int64

------------------------------1D array series number using asign your own index panda-------------------------
import pandas as pd
s1=pd.Series(data=[5,10,15,20],index=['hello','python','program','D'])
print(s1)

O/P :-
hello       5
python     10
program    15
D          20
dtype: int64

------------------------------1D array series number using asign your own index panda-------------------------


















