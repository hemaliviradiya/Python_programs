--------------------------read data from dataset--------------------------

import pandas as pd
df = pd.read_csv("iris.csv")
print(df.head)

O/P :-
<bound method NDFrame.head of       Id  SepalLengthCm  ...  PetalWidthCm         Species
0      1            5.1  ...           0.2     Iris-setosa
1      2            4.9  ...           0.2     Iris-setosa
2      3            4.7  ...           0.2     Iris-setosa
3      4            4.6  ...           0.2     Iris-setosa
4      5            5.0  ...           0.2     Iris-setosa
..   ...            ...  ...           ...             ...
145  146            6.7  ...           2.3  Iris-virginica
146  147            6.3  ...           1.9  Iris-virginica
147  148            6.5  ...           2.0  Iris-virginica
148  149            6.2  ...           2.3  Iris-virginica
149  150            5.9  ...           1.8  Iris-virginica

[150 rows x 6 columns]>

--------------------------read data from dataset array of array fetch top five value of given column--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df[['PetalWidthCm','Species']].head())

O/P :-
   PetalWidthCm      Species
0           0.2  Iris-setosa
1           0.2  Iris-setosa
2           0.2  Iris-setosa
3           0.2  Iris-setosa
4           0.2  Iris-setosa

--------------------------read data from dataset array of array whether null or not--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df[['PetalWidthCm','Species']].head().isnull())

O/P :-
 PetalWidthCm  Species
0         False    False
1         False    False
2         False    False
3         False    False
4         False    False

--------------------------read data from dataset array of array whether null or not--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.head().isna())

O/P :-
 Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm  Species
0  False          False         False          False         False    False
1  False          False         False          False         False    False
2  False          False         False          False         False    False
3  False          False         False          False         False    False
4  False          False         False          False         False    False

--------------------------read data from dataset fetch specific item--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.at[2,'Species'])

O/P :-
Iris-setosa

--------------------------read data from dataset locatipon of data--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.loc[2,])

O/P :-
Id                         3
SepalLengthCm            4.7
SepalWidthCm             3.2
PetalLengthCm            1.3
PetalWidthCm             0.2
Species          Iris-setosa
Name: 2, dtype: object

--------------------------read data from dataset locatipon of data--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.loc[2,'Species'])

O/P :-
Iris-setosa

--------------------------read data from dataset locatipon of data int value--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.iloc[2,2])

O/P :-  3.2

--------------------------read data from dataset locatipon of data--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.iloc[0:2,2:2])

O/P :-
Empty DataFrame
Columns: []
Index: [0, 1]

--------------------------read data from dataset locatipon of data--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df.iloc[0:2,4:6])

O/P :-
 PetalWidthCm      Species
0           0.2  Iris-setosa
1           0.2  Iris-setosa

--------------------------read data from dataset locatipon of data--------------------------
import pandas as pd

df = pd.read_csv("iris.csv")
print(df['PetalWidthCm'].value_counts())

O/P :-
0.2    28
1.3    13
1.5    12
1.8    12
1.4     8
2.3     8
1.0     7
0.3     7
0.4     7
0.1     6
2.0     6
2.1     6
1.2     5
1.9     5
1.6     4
2.5     3
2.2     3
2.4     3
1.1     3
1.7     2
0.6     1
0.5     1
Name: PetalWidthCm, dtype: int64



