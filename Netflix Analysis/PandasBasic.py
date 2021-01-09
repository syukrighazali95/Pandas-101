import pandas as pd 
import numpy as np

# Creating pandas series
li = [10, 20, 30, 40, 50, 60]
s = pd.Series(li)
print(s)
print(type(s))
print(s.size)
print(s.ndim)
print(s.values)
print(s.head(2))
print(s.tail(3))
print(s[1])

# Changing series labels
s1 = pd.Series(li, index=[4,4,5,6,5,7])
print(s1)
print(s1[4])
s1 = pd.Series(li, index=["one", "two", "three", "four", "five", "six"])
print(s1)
print(s1["three"])

# Create series from dictionary 
students_in_state = {"Kuala_Lumpur": 24, "Johor_Bahru": 32, "Penang": 45}
print(students_in_state)
students = pd.Series(students_in_state)
print(students)
select_state = pd.Series(students_in_state, index=["Kuala_Lumpur", "Johor_Bahru"])
print(select_state)

# Create pandas series from numpy arrays
a = np.array(li)
print(a)
a = pd.Series(a)
print(a)

# Merging or concatenate between 2 series
s1 = pd.Series([1,2,3,34,5])
s2 = pd.Series([44,4,5.6,77,3])
# Change the axis to change the concatenate direction 
c1 = pd.concat([s1, s2], axis=0)
print(c1)

# Selections of series   
