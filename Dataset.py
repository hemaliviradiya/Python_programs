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

--------------------------read data from dataset array of array--------------------------
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


