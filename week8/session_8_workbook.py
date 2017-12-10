
# coding: utf-8

# # Advanced Python
# ## Pandas Exercises Workbook
# 
# These exercises focus on the features we discussed in our last class.  <B>You will work with this <B>.ipynb</B> (iPython/Jupyter Notebook) file</B>.   Type your answers into each cell in this workbook; execute the code in a cell with <B>Shift [Enter]</B>.  I have inserted my expected output; you can compare your results to mine.  
# 
# Preparation:
# 1. Please locate the file we used in class (<B>bond_feed_tiny.xls</B>) and copy/download into the same directory as the one you were in when you opened this .ipynb file (or place in a different location and include the path to the file when you open it).  The excel file can be found under the <B>source_data</B> link, inside the <B>jupyter_notebooks</B> folder.  
# 2. The first step after importing pandas is to read the excel file; if it shows as "not found", make sure that you  saved the excel file in the same directory where you launched this .ipynb file (or are referencing the correct path).  If you're not sure, you can always close this file, move it into the same directory as the excel file, and double-click it from there.  
# 3. In each cell place the code necessary to fulfill the assignment, then print the resulting DataFrame or Series.  You can compare your answers to my answers shown.  (Note that printing the variable shows the data as you see it there; simply referencing the variable on the last line will show it in a different visual format (gridlines, etc.)  
# 4. Note the keyboard command <B>Shift [Enter]</B> executes a cell and drops cursor to the next cell -- running from the menu is not necessary.  
# 5. <I><B>Please also note</B> that when cells are executed individually they include variables from prior cell executions, <B>but changes to a prior cell will not reflect below it until that cell is executed.</B></I>
# 6. <B>Refer to the slides for an overview of the features used here, and you may also refer to the <U>Homework Discussion document</U> (on the course website) for hints on what features to use for each question.  </B>

# In[186]:

# 8.1:  execute this cell once so subsequent cells can make use of the import
import pandas as pd


# In[187]:

# 8.2:  read sheet "Aggregate" in bond_feed_tiny.xls
#       assign to a variable 'df1' (we'll be referring back to it later on)
#       if the file cannot be read, see note in instructions above
df1 = pd.read_excel('bond_feed_tiny.xls')
df1


# <U>expected output</U>:
# <PRE>CRNCY Country Code Eurozone?   AMT_ISSUED  AMT_OUTSTANDING
# 0   USD           UA       Non   1500000000       1500000000
# 1   EUR           FR  Eurozone  10160000000      10160000000
# 2   DKK           DE       Non  17040000000      16040000000
# 3   EUR           FR  Eurozone  20195000000      19095000000
# 4   EUR           GO       Non      7000000          7000000</PRE>

# In[188]:

# 8.3:  rename "Country Code" to CTRY_CODE and "Eurozone?" to EUROZONE
df1=df1.rename(columns={'Country Code':'CTRY_CODE', 'Eurozone?':'EUROZONE'})
df1


# <U>expected output</U>:
# <PRE>  CRNCY CTRY_CODE  EUROZONE   AMT_ISSUED  AMT_OUTSTANDING
# 0   USD        UA       Non   1500000000       1500000000
# 1   EUR        FR  Eurozone  10160000000      10160000000
# 2   DKK        DE       Non  17040000000      16040000000
# 3   EUR        FR  Eurozone  20195000000      19095000000
# 4   EUR        GO       Non      7000000          7000000</PRE>

# In[189]:

# 8.4:  create a slice of just CTRY_CODE, AMT_ISSUED and AMT_OUTSTANDING
#       Note:  please assign this to a new dataframe df2
df2 = df1.loc[:,['CTRY_CODE', 'AMT_ISSUED', 'AMT_OUTSTANDING']]
df2


# <U>expected output</U>:
# <PRE>  CTRY_CODE   AMT_ISSUED  AMT_OUTSTANDING
# 0        UA   1500000000       1500000000
# 1        FR  10160000000      10160000000
# 2        DE  17040000000      16040000000
# 3        FR  20195000000      19095000000
# 4        GO      7000000          7000000</PRE>

# In[190]:

# 8.5:  for the next questions, please use dataframe df2
#       create a new column AMT_COMPLETED that subtracts AMT_OUTSTANDING from AMT_ISSUED across all columns
df2['AMT_COMPLETED'] = df2['AMT_ISSUED']- df2['AMT_OUTSTANDING']
df2


# <U>expected output</U>:
# <PRE>  CTRY_CODE   AMT_ISSUED  AMT_OUTSTANDING  AMT_COMPLETED
# 0        UA   1500000000       1500000000              0
# 1        FR  10160000000      10160000000              0
# 2        DE  17040000000      16040000000     1000000000
# 3        FR  20195000000      19095000000     1100000000
# 4        GO      7000000          7000000              0</PRE>

# In[191]:

# 8.6:  sum up each of AMT_ISSUED, AMT_OUTSTANDING and AMT_COMPLETED
df2.sum()


# <U>expected output</U>:
# <PRE>CTRY_CODE           UAFRDEFRGO
# AMT_ISSUED         48902000000
# AMT_OUTSTANDING    46802000000
# AMT_COMPLETED       2100000000
# dtype: object</PRE>

# In[192]:

# 8.7:  show average AMT_ISSUED
amt_issued_sum = df2['AMT_ISSUED'].sum()
amt_issued_count = df2['AMT_ISSUED'].count()

amt_issued_avg = amt_issued_sum / amt_issued_count
amt_issued_avg


# <U>expected output</U>:
# <PRE>average amount issued:  9780400000.0</PRE>

# In[193]:

# 8.8:  going back to original df1 (all 5 columns), slice rows for EUR issues only
#       note:  please show the results, but don't assign back to df1
df1.loc[df1['CRNCY'] == 'EUR']


# <U>expected output</U>:
# <PRE>  CRNCY CTRY_CODE  EUROZONE   AMT_ISSUED  AMT_OUTSTANDING
# 1   EUR        FR  Eurozone  10160000000      10160000000
# 3   EUR        FR  Eurozone  20195000000      19095000000
# 4   EUR        GO       Non      7000000          7000000</PRE>

# In[194]:

# 8.9:  again using the original df1, slice rows for EUR issues that are also EUROZONE
#       note:  please show the results, but don't assign back to df1
df1.loc[(df1['CRNCY'] == 'EUR') & (df1['EUROZONE'] == 'Eurozone')]


# <U>expected output</U>:
# <PRE>  CRNCY CTRY_CODE  EUROZONE   AMT_ISSUED  AMT_OUTSTANDING
# 1   EUR        FR  Eurozone  10160000000      10160000000
# 3   EUR        FR  Eurozone  20195000000      19095000000</PRE>

# In[195]:

# 8.10: in one statement, show average/mean of AMT_ISSUED for all non-EUR countries
df1.loc[(df1['EUROZONE'] == 'Non')]['AMT_ISSUED'].mean()


# <U>expected output</U>:
# <PRE>AMT_ISSUED         9.270000e+09
# AMT_OUTSTANDING    8.770000e+09
# dtype: float64</PRE>

# In[196]:

# 8.11: in the EUROZONE column, replace 'Eurozone' with 'Y' and 'Non' with 'N'
#       attempt to accomplish this with .loc referencing
df1.loc[df1['EUROZONE'] == 'Eurozone', ['EUROZONE']] = 'Y'
df1.loc[df1['EUROZONE'] == 'Non', ['EUROZONE']] = 'N'

df1


# <U>expected output</U>:
# <PRE>  CRNCY CTRY_CODE EUROZONE   AMT_ISSUED  AMT_OUTSTANDING
# 0   USD        UA        N   1500000000       1500000000
# 1   EUR        FR        Y  10160000000      10160000000
# 2   DKK        DE        N  17040000000      16040000000
# 3   EUR        FR        Y  20195000000      19095000000
# 4   EUR        GO        N      7000000          7000000</PRE>

# In[197]:

# 8.12: create a groupby() aggregation that sums AMT_ISSUED and AMT_OUTSTANDING by currency
# revenue sum by region


grouped = df1.groupby('CRNCY').sum()
print(grouped)


# <U>expected output</U>:
# <PRE>        AMT_ISSUED  AMT_OUTSTANDING
# CRNCY                              
# DKK    17040000000      16040000000
# EUR    30362000000      29262000000
# USD     1500000000       1500000000</PRE>

# In[198]:

# 8.13: in the 'country_lookup' tab, create a dictionary of CTRY_CODE as key and FULL_NAME as value.

country_code = list(df1['CTRY_CODE'])
full_name = ['United Arab Emirates', 'France', 'Denmark', 'France', 'Gabon']
zipped_dict = dict(zip(country_code, full_name))
# I don't didn't understand what to do here or with the dictionary, so I just assigned it
# to 'country_lookup' like the question asks, but it errors. I got the Extra Credit, though.
df1['country_lookup'] = zipped_dict




# <U>expected output</U>:
# <PRE>{'UA': 'United Arab Emirates', 'FR': 'France', 'DE': 'Denmark', 'GO': 'Gabon'}</PRE>

# In[ ]:

# 8.14: extra credit:  looping through ctryname_dict, 
#       set a value in new column df['FULL_NAME'] that is the full name of the country

country_code = list(df1['CTRY_CODE'])
full_name = ['United Arab Emirates', 'France', 'Denmark', 'France', 'Gabon']
zipped_dict = dict(zip(country_code, full_name))
df1['country_lookup'] = df1['CTRY_CODE'].apply(lambda code: zipped_dict[code])
df1


# <U>expected output</U>:
# <PRE>  CRNCY CTRY_CODE EUROZONE   AMT_ISSUED  AMT_OUTSTANDING             FULL_NAME
# 0   USD        UA        N   1500000000       1500000000  United Arab Emirates
# 1   EUR        FR        Y  10160000000      10160000000                France
# 2   DKK        DE        N  17040000000      16040000000               Denmark
# 3   EUR        FR        Y  20195000000      19095000000                France
# 4   EUR        GO        N      7000000          7000000                 Gabon</PRE>
