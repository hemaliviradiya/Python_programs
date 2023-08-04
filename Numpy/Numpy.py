  
  -------------------------Numpy 1D array print------------------------
  
  import numpy as np
  
  n1=np.array([10,20,30,40,50])
  print(n1)
  
  O/P :-
  [10 20 30 40 50]
  
  -------------------------Numpy 2D array print------------------------
  
  import numpy as np
  
  n1=np.array([[10,20,30,40,50],[5,10,15,20,25]])
  print(n1)
  
  O/P :-
  [[10 20 30 40 50]
   [ 5 10 15 20 25]]
  
  -------------------------Numpy shape of 2D array print------------------------
  
  import numpy as np
  
  n1=np.array([[10,20,30,40,50],[5,10,15,20,25]])
  print(n1.shape)
  
  O/P :-
  (2, 5)
  
  -------------------------Numpy zeros matrix------------------------
  import numpy as np
  
  n1=np.zeros((2,3))
  print(n1)
  
  O/P :-
  [[0. 0. 0.]
   [0. 0. 0.]]
  
  -------------------------Numpy ones matrix------------------------
  
  import numpy as np
  
  n1=np.ones((3,4))
  print(n1)
  
  O/P :-
  [[1. 1. 1. 1.]
   [1. 1. 1. 1.]
   [1. 1. 1. 1.]]
  
  -------------------------Numpy print range of number------------------------
  import numpy as np
  
  n1=np.arange(11,20)
  print(n1)
  
  O/P :-
  [11 12 13 14 15 16 17 18 19]
  
  -------------------------Numpy print even value range of number------------------------
  
  import numpy as np
  
  n1=np.arange(11,20,2)
  print(n1)
  
  O/P :-
  [11 13 15 17 19]
  
  -------------------------Numpy print gape of 10 value range of number------------------------
  import numpy as np
  
  n1=np.arange(10,100,10)
  print(n1)
  
  O/P :-
  [10 20 30 40 50 60 70 80 90]
  
  -------------------------Numpy print 3*3 matrix------------------------
  import numpy as np
  
  n1=np.arange(10,100,10)
  n1.shape=(3,3)
  print(n1)
  
  O/P :-
  [[10 20 30]
   [40 50 60]
   [70 80 90]]
  
  -------------------------Numpy print 4*2 matrix------------------------
  import numpy as np
  
  n1=np.arange(10,90,10)
  n1.shape=(4,2)
  print(n1)
  
  O/P :-
  [[10 20]
   [30 40]
   [50 60]
   [70 80]]
  
  -------------------------Numpy print any random number------------------------
   import numpy as np
  
  n1 = np.random.randint(1,100,10)
  print(n1)
  
  O/P :-
  [51 82  2 35 71 95 79 89 99 82]
  and time run :- [ 6 71 90 31 46 16 92 34 67 37](every time run wil get diffrent output)
  
  -------------------------Numpy numpy array------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(10,15)
  print(n1)
  print(n2)
  
  O/P :-
  [1 2 3 4]
  [10 11 12 13 14]
  
  -------------------------Numpy combine numpy array horizontaly------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(10,15)
  print(n1)
  print(n2)
  print(np.hstack((n1,n2)))
  
  O/P :-
  [1 2 3 4]
  [10 11 12 13 14]
  [ 1  2  3  4 10 11 12 13 14]
  
  -------------------------Numpy combine numpy array vertically------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(11,15)
  print(n1)
  print(n2)
  print(np.vstack((n1,n2)))
  
  O/P :-
  [1 2 3 4]
  [11 12 13 14]
  [[ 1  2  3  4]
   [11 12 13 14]]
  
  -------------------------Numpy combine numpy array in column_stack------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(11,15)
  print(np.column_stack((n1,n2)))
  
  O/P :-
  [[ 1 11]
   [ 2 12]
   [ 3 13]
   [ 4 14]]
  
  -------------------------Numpy sum of 2 matrix------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(11,15)
  print(n1)
  print(n2)
  print(n1+n2)
  
  O/P :-
    [1 2 3 4]
  [11 12 13 14]
  [12 14 16 18]

 -------------------------Numpy sub of 2 matrix------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(11,15)
  print(n1)
  print(n2)
  print(n1-n2)
  
  O/P :-
      [1 2 3 4]
  [11 12 13 14]
  [-10 -10 -10 -10]

 -------------------------Numpy mul of 2 matrix------------------------
  import numpy as np
  
  n1 = np.arange(1,5)
  n2 = np.arange(11,15)
  print(n1)
  print(n2)
  print(n1*n2)
  
  O/P :-
       [1 2 3 4]
  [11 12 13 14]
  [11 24 39 56]

-------------------------Numpy div of 2 matrix------------------------
import numpy as np

n1 = np.arange(1,5)
n2 = np.arange(11,15)
print(n1)
print(n2)
print(n1/n2)

 O/P :-
 [1 2 3 4]
[11 12 13 14]
[0.09090909 0.16666667 0.23076923 0.28571429]

-------------------------Numpy mean(average) of 2 matrix------------------------
import numpy as np

n1 = np.arange(1,5)
n2 = np.arange(10,15)
print(np.sum(n2))
print(np.mean(n2))

O/P :-
 60
12.0

-------------------------Numpy mean(average),median.standard deviation  of 2 matrix------------------------
import numpy as np

n1 = np.arange(1,5)
n2 = np.arange(10,15)
print(np.sum(n2))
print(np.mean(n2))
print(np.median(n2))
print(np.std(n2))

O/P :-
60
12.0
12.0
1.4142135623730951

-------------------------Numpy scaller of matrix------------------------
import numpy as np

n1 = np.arange(1,5)
print(n1)
print(n1+2)

O/P :-
[1 2 3 4]
[3 4 5 6]

-------------------------Numpy mul scaller of matrix------------------------
import numpy as np

n1 = np.arange(1,5)
print(n1)
print(n1*2)

O/P :-
[1 2 3 4]
[2 4 6 8]

-------------------------Numpy print array------------------------
import numpy as np

n1 = np.array([1,2,4,5,8,9])
n2=np.array([5,6,7,8,9])
print(n1)
print(n2)

O/P :-
[1 2 4 5 8 9]
[5 6 7 8 9]

-------------------------Numpy print same arrray in 2d  array------------------------
import numpy as np

n1 = np.array([1,2,4,5,8,9])
n2=np.array([5,6,7,8,9])
print(n1)
print(n2)
print(np.intersect1d(n1,n2))

O/P :-
[1 2 4 5 8 9]
[5 6 7 8 9]
[5 8 9]

-------------------------Numpy print 1 time(remaining) arrray in 2d  array------------------------
import numpy as np

n1 = np.array([1,2,4,5,8,9])
n2=np.array([5,6,7,8,9])
print(n1)
print(n2)
print(np.setdiff1d(n1,n2))

O/P :-
[1 2 4 5 8 9]
[5 6 7 8 9]
[1 2 4]

-------------------------create numpy file in folder------------------------
import numpy as np

n1 = np.array([1,2,4,5,8,9])
n2=np.array([5,6,7,8,9])

np.save('mynparray',n1)

O/P :-
mynnparray.npy(file created in folder
               
-------------------------print nupmy file value that created in our folder------------------------
import numpy as np

n1 = np.array([1,2,4,5,8,9])
n2=np.array([5,6,7,8,9])

np.save('mynparray',n1)
n3=np.load('mynparray.npy')
print(n3)

O/P :-
[1 2 4 5 8 9]

               
