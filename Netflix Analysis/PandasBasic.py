import pandas as pd 
import numpy as np

#################
# PANDAS SERIES #
#################

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
s3 = pd.Series([12,3,23,3,5])
print(s3[1])
print(s3[0:3])
print(s3[:2])
print(s3[4:])
print(s3[:-1])
s4 = pd.Series([32,43,456,67,89], index=["first", "second", "third", "fourth", "fifth"])
print(s4.index)
print(s4.keys)
print(list(s4.items()))

#Queries in Pandas Series
s5 = pd.Series([23,83,45,67,8])
print(3 in s5)
print(23 in s5)

# Selecting multiple elements in Pandas Series
s6 = pd.Series([23,344,56,89,5])
print(s6[[2,4]])
s7 = pd.Series([23,344,56,89,5], index=["first", "second", "third", "fourth", "fifth"])
print(s7[["first", "third"]])

# Update value in Series
s8 = pd.Series([2,343,54,45,7])
s8[0] = 6
print(s8)

####################
# PANDAS DATAFRAME #
####################

# Attributes in DataFrame
dic = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45]}
df1 = pd.DataFrame(dic)
print(df1)
print(df1["No_devices"])
print(df1.No_devices)

l1 = [52,6,37,3,2,12,2,42,35]
df2 = pd.DataFrame(l1,columns=["variable_name"]) 
print(df2)

arr = np.array(l1).reshape(3,3)
print(arr)
df3 = pd.DataFrame(arr, columns=["Var1","Var2","Var3"])
print(df3)
print(df3.axes)
print(df3.shape)
print(df3.ndim)
print(df3.size)
print(df3.columns)
print(df3.index)
print(df3.values)

# Change column in DataFrame
print(df3)
print(df3.columns)
df3.columns = ["col1", "col2", "col3"]
print(df3)

# Access rows in dataframe
dic = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45], 'Age': [2,3,4]}
df1 = pd.DataFrame(dic)
print(df1)
print(df1.iloc[0])
print(df1.iloc[[0,2]]) # Select multiple rows
print(df1.iloc[[0,2],2]) # Rows for specific column
print(df1.iloc[[0,2],[1,2]]) # Rows for multiple columns
print(df1.iloc[1:3])
print(df1.iloc[1:3,2])

# Using loc to access rows
# Difference between loc and iloc - loc is label based and iloc is integer based
print(df1)
df1.loc[0]
df1.loc[[0,2],"Age"]
df1 = pd.DataFrame(dic, index=["a", "b", "c"])
print(df1)
print(df1.loc["a"])
print(df1.loc[["a","c"]])
print(df1.loc["b":])
print(df1.loc["c":,"No_devices"])

# Accessing columns in dataframe
print(df1)
print(df1.Age)
print(df1["Age"])
print(df1["Age"][0])

# Assigning value to row
print(df1)
df1.iloc[2] = ["Huawei", "30", "3"]
print(df1)

# Assigning custom index using columns
dic = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45], 'Age': [2,3,4], 'Serial_no': ["JSD1231231","DSH231234","HSD123455"]}
df1 = pd.DataFrame(dic)
print(df1)
df1 = df1.set_index("Serial_no")
print(df1)
print(df1.loc["JSD1231231"])

# Reset index 
print(df1)
df1.reset_index(inplace=True)
print(df1)

# Sorting index
dic = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45], 'Age': [2,3,4], 'Serial_no': ["JSD1231231","DSH231234","HSD123455"]}
df1 = pd.DataFrame(dic, index=[4,3,6])
print(df1)
df1.sort_index(inplace=True)
print(df1)

# Filtering 
dic = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45], 'Age': [2,3,4], 'Serial_no': ["JSD1231231","DSH231234","HSD123455"]}
df1 = pd.DataFrame(dic)
print(df1["Name"] == "Juniper")
print(df1[df1["Name"] == 'Cisco'])
print(df1.loc[df1["Name"] == "Arista", "Serial_no"])

# Filtering with arithmetic operations
print(df1[df1["No_devices"] > 30])
print(df1[(df1["No_devices"] > 30) & (df1["Age"] < 4)])
print(df1[(df1["No_devices"] > 30) | (df1["Age"] < 4)])
print(df1[~(df1["No_devices"] > 30)])

# Filtering with filter() function
fil = df1.filter(items=["Name","Serial_no"])
print(fil)

# Filter with regex for column that ends with e
fil = df1.filter(regex='e$', axis=1)
print(fil)

# Adding rows using append
print(df1)
app1 = df1.append({"Name": "Dell"},ignore_index=True)
print(app1)
print(df1)
app2 = df1.append({"Name":"Dell","No_devices":32,"Age":56,"Serial_no":"DHSDA03123"},ignore_index=True)
print(app2)

# Remove rows using index
dp1 = df1.drop(index=2)
print(dp1)
cond1 = df1[df1["No_devices"]>30]
print(cond1)
dp2 = df1.drop(index=cond1.index)
print(dp2)

# Adding columns
df1["Version"] = [14,32,42]
print(df1)

# Remove columns
dp3 = df1.drop(columns=["Age", "No_devices"])
print(dp3)
dp4 = df1.drop(["Name","Version"],axis=1)
print(dp4)

# Combining 2 dataframes
dic1 = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [17,34,45], 'Age': [2,3,4], 'Serial_no': ["JSD1231231","DSH231234","ASD173455"]}
dic2 = {'Name': ["Dell","Nokia", "Huawei"], 'No_devices': [34,44,22], 'Age': [3,7,4], 'Serial_no': ["DHSD02313","NSDSD1234","HSD123455"]}
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
df3 = pd.concat([df1,df2])
print(df3)
df3 = pd.concat([df1,df2], ignore_index=True)
print(df3)

# Inner Join: Join matching values only. Different columns are removed
dic1 = {'Name': ["Juniper","Cisco", "Arista"], 'Serial_no': ["JSD1231231","DSH231234","ASD173455"]}
dic2 = {'Name': ["Dell","Nokia", "Huawei"], 'No_devices': [34,44,22], 'Age': [3,7,4], 'Serial_no': ["DHSD02313","NSDSD1234","HSD123455"]}
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
df3 = pd.concat([df1,df2])
print(df3)
df3 = pd.concat([df1,df2], ignore_index=True, join="inner")
print(df3)

# dic3 = {'Department': ["IT","Account", "Management"]}
# df3 = pd.DataFrame(dic3)
# df4 = pd.concat([df1,df3])
# print(df4)


# Full join 
df4 = pd.concat([df1,df2],join="outer")
print(df4)

# Left join
df5 = pd.merge(df1,df2,how="left")
print(df5)

# Right join
df6 = pd.merge(df1,df2,how="right")
print(df6)

# Merge many to many structure
dic1 = {'Name': ["Juniper","Cisco", "Arista"], 'No_devices': [50,34,45], 'Age': [2,3,4], 'Serial_no': ["JSD1231231","DSH231234","ASD173455"]}
dic2 = {'Serial_no': ["JSD1231231","DSH231234","ASD173455"],'Department': ["IT","Account", "Management"], 'Team': ["abc","def", "ghi"] }
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
df3 = pd.merge(df1,df2)
print(df3)

# Sort by values
print(df1)
df4 = df1.sort_values(by="No_devices")
print(df4)
df4 = df1.sort_values(by="No_devices", ascending=False)
print(df4)
# Sort by no of devices first and then sort by age
df4 = df1.sort_values(by=["No_devices", "Age"])
print(df4)
df4 = df1.sort_values(by=["No_devices", "Age"], ascending=[True,False])
print(df4)

# Largest elements in column. N denotes the number of elements
largest = df1["No_devices"].nlargest(2)
smallest = df1["No_devices"].nsmallest(1)
print(largest)
print(smallest)