import pandas as pd 

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
s1 = pd.Series(li, index=["one", "two", "three", "four", "five", "six"])
print(s1)