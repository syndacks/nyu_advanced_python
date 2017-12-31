
# coding: utf-8

# # Pandas 2 Homework Assignment

# <U>Note on viewing large datasets</U>:  as you know, there are two ways to view a DataFrame in Jupyter Notebook:  by <B>print()</B>ing the DataFrame variable (i.e., <B>print(df)</B> (where <B>df</B> is the DataFrame), and by simply referring to the DataFrame variable as the last statement in a cell (i.e., <B>df</B> by itself on the last line), which displays a formatted view of the data with scrolling.  Note that either method may show an abbreviation of the data -- the text formatted view provided by Jupyter may include ellipses on large datasets -- so not all rows or columns may be displayed.  

# <B>3.1.</B> Open <B>govt_bond_feed_sample.xls</B>.  Look at the <B>len()</B> of the resulting dataframe -- make sure it is <B>102 rows</B> and that the data shows sovereign bond issues.  If it is not, make sure you are specifying the correct sheet name.  If you are unsure of the argument to use for sheet name, use <B>help(pd.read_excel)</B> to see the docstring.  

# In[201]:

import pandas as pd

df1 = pd.read_excel('govt_bond_feed_sample.xls')
print (len(df1))
df1.columns


# <PRE><U>Expected Output</U>:  
# 
# 102</PRE>

# <B>3.2.</B> Change all column headings so that they are UPPERCASE_WITH_UNDERSCORES.  Print <B>df.columns</B> to verify.

# In[202]:

cols = df1.columns
cols = cols.map(lambda x: x.replace(' ', '_'))
cols = cols.map(lambda x: x.upper())
df1.columns = cols
df1.columns


# <PRE><U>Expected Output</U>:  
# 
# Index(['COUNTRY_HAS_ABOVE_$50_BIL_OUTSTANDING_ON_7/15?', 'LONG_COMP_NAME',
#        'CRNCY', 'CURRENCY_TYPE', 'ID_CUSIP', 
#        'MARKET_SECTOR_DES', 'INDUSTRY_SECTOR', 'INDUSTRY_GROUP',
#        'INDUSTRY_SUBGROUP', 'COUNTRY', 'EUROZONE?', 'COUNTRY_GUARANTOR',
#        'CNTRY_OF_DOMICILE', 'AMT_ISSUED', 'AMT_OUTSTANDING',
#        'AMOUNT_OUTSTANDING_(STATED_CURRENCY)_FROM_MARKET_VALUE',
#        'AMOUNT_OUTSTANDING_(USD)_FROM_MARKET_VALUE',
#        'AMOUNT_OUTSTANDING_(USD)_FROM_MARKET_VALUE_FIX',
#        'YIELD_AT_ISSUE_RAW', 'YIELD_AT_ISSUE_FIX', 'PRICE_AT_ISSUE', 
#        'ISSUE_DT', 'MATURITY', 'FINAL_MATURITY',
#        'INTEREST_PAYMENTS_FROM_CURRENT_COUPONS', 'LOCAL_CURRENCY_RATING'],
#       dtype='object')</PRE>

# <B>3.3.</B>  <U>Limit columns to the following</U>:<BR>
# LONG_COMP_NAME <BR>
# CRNCY <BR>
# CURRENCY_TYPE <BR>
# ID_CUSIP <BR>
# COUNTRY <BR>
# EUROZONE? <BR>
# CNTRY_OF_DOMICILE <BR>
# AMT_ISSUED <BR>
# AMT_OUTSTANDING <BR>
# ISSUE_DT <BR>
# MATURITY <BR>
# LOCAL_CURRENCY\_RATING
# 
# <U>Special note</U>:  Don't forget that <B>.loc[]</B> is the preferred way to select data that may later be changed.  

# In[203]:

columns_to_keep = [
    'LONG_COMP_NAME',
    'CRNCY',
    'CURRENCY_TYPE',
    'ID_CUSIP',
    'COUNTRY',
    'EUROZONE?',
    'CNTRY_OF_DOMICILE',
    'AMT_ISSUED',
    'AMT_OUTSTANDING',
    'ISSUE_DT',
    'MATURITY',
    'LOCAL_CURRENCY_RATING'
                  ]

for column in df1.columns:
    if column not in columns_to_keep:
        df1 = df1.drop(column, 1)

df1


# <PRE><U>To verify expected output</U>:  display the dataframe in Jupyter by simply referring to it in the last line of a cell.  Scroll to the right to verify you have selected the correct columns.</PRE>

# <B>3.4.</B>  Use <B>.isnull()</B> along with <B>.any()</B> on the DataFrame to see which columns contain any null values (<B>np.nan</B> or <B>NaN</B>).  You should see a list of columns along with <B>True/False</B> for each.  

# In[204]:

df1.isnull().any()


# <PRE><U>Expected Output</U>: 
# 
# LONG_COMP_NAME                False
# CRNCY                         False
# CURRENCY_TYPE                 False
# ID_CUSIP                      False
# COUNTRY                        True
# EUROZONE?                     False
# CNTRY_OF_DOMICILE              True
# <B>AMT_ISSUED                     True</B>
# AMT_OUTSTANDING               False
# ISSUE_DT                      False
# <B>MATURITY                       True</B>
# LOCAL_CURRENCY\_RATING     True
# dtype: bool</PRE>

# <B>3.5.</B>  Fill in any missing values in <B>AMT_ISSUED</B> with 0.  <BR>
# Eliminate rows that do not have a value for <B>MATURITY</B>.
# 
# Again <B>.isnull() with .any()</B> to confirm that <B>AMT_ISSUED</B> and <B>MATURITY</B> do not show any null values.  

# In[211]:

df1['AMT_ISSUED'] = df1['AMT_ISSUED'].fillna(0)
df1['MATURITY'] = df1['MATURITY'].fillna(0)

df1.isnull().any()


# 
# <PRE><U>Expected Output</U>:  
# 
# LONG_COMP_NAME                False
# CRNCY                         False
# CURRENCY_TYPE                 False
# ID_CUSIP                      False
# COUNTRY                        True
# EUROZONE?                     False
# CNTRY_OF_DOMICILE              True
# <B>AMT_ISSUED                    False</B>
# AMT_OUTSTANDING               False
# ISSUE_DT                      False
# <B>MATURITY                      False</B>
# LOCAL_CURRENCY\_RATING         True
# dtype: bool</PRE>

# <B>3.6.</B>  Display rows where <B>LOCAL_CURRENCY\_RATING</B> is <B>null</B> (you should see 2 rows); display rows where <B>COUNTRY</B> is <B>null</B> or <B>CNTRY_OF_DOMICILE</B> is <B>null</B> (you should see 1 row).
# 

# In[206]:

loc_cur_rat_null = df1['LOCAL_CURRENCY_RATING'].isnull()
df1[loc_cur_rat_null]


cntry_null_or_cntry_domic_null = df1['COUNTRY'].isnull() | df1['CNTRY_OF_DOMICILE'].isnull()
df1[cntry_null_or_cntry_domic_null]


# <PRE><U>To verify expected output</U>:  querying for "LOCAL_CURRENCY" rows should return <B>Niger Government Bond</B> and <B>Union of Myanmar Treasury Bond</B>.  
# 
# "COUNTRY" and "COUNTRY OF DOMICILE" should return one line, <B>Namibia Treasury Bills</B>.</PRE>  

# <B>3.7.</B>  Set column <B>ID_CUSIP</B> as the index for this DataFrame.    Print <B>df.index</B> to confirm.  

# In[207]:

df1.set_index('ID_CUSIP')


# <PRE><U>Expected Output</U>: 
# 
# Index(['29134UAB7', 'EK1898270', 'JK1313812', 'QZ6293943', 'EC3464624',
#        '040114GV6', 'EH6697161', 'EI7901354', 'EJ9077292', 'EK1869404',
#        ... continued ...
#        'EJ3796640', 'EC1377414', 'EJ3042904', '912833L32', '912820TQ0',
#        '912820YT8', '9128337B0', '912810RC4', 'EJ7621927', 'EK2699859'],
#       dtype='object', name='ID_CUSIP', length=101)</PRE>

# <B>3.8.</B>  Reading the Currencies sheet from the DataFrame, create a dict or DataFrame lookup that matches the 'Currency' column to the 'USD Conversion' column.  Print the dict to confirm.  

# In[208]:

currencies = pd.read_excel('govt_bond_feed_sample.xls', sheetname='Currencies')
currency = currencies['Currency']
exchange_rate = currencies['USD Conversion']

lookup_dict = dict(zip(currency, exchange_rate))
lookup_dict


# <PRE><U>Expected Output</U>:  
# 
# {'AED': 0.27229999999999999,
#  'AFN': 0.0150105,
#  'ALL': 0.0077999999999999996,
#  'AMD': 0.0020860000000000002,
#  'ANG': 0.56259999999999999,
#  'AOA': 0.0060000000000000001,
# ... continued ...      
# 
#  'XAF': 0.0016130000000000001,
#  'XCD': 0.37040000000000001,
#  'XOF': 0.001614,
#  'YER': 0.0040000000000000001,
#  'ZAR': 0.072914000000000007,
#  'ZMK': 1.0,
#  'ZMW': 0.10100000000000001}</PRE>

# <B>3.9.</B>  Create a new column, <B>AMT_ISSUED_USD</B> to calculate <B>AMT_ISSUED</B> in dollars.  Use the currencies lookup you created in the prior step.  Print the first few rows of the below two columns to see the calculation.  

# In[209]:

df1['AMT_ISSUED_USD'] = (df1['AMT_ISSUED'] * df1['CRNCY'].apply(lambda x: lookup_dict[x]))
df1['AMT_ISSUED_USD']
df1[:4]


# <PRE><U>Expected Output</U>:
#                                               LONG_COMP_NAME  AMT_ISSUED_USD
# ID_CUSIP                                                                    
# 29134UAB7            Abu Dhabi Government International Bond    1.500000e+09
# EK1898270                             Angola Government Bond    3.082817e+07
# JK1313812                             Angola Government Bond    8.716035e+07
# QZ6293943                             Angola Government Bond    4.646983e+07
# EC3464624                          Argentina Government Bond    2.608060e+09</PRE>

# <B>3.10.</B>  Calculate average AMT_ISSUED by CRNCY. 

# In[216]:

df1['AMT_ISSUED'].groupby(df1['CRNCY']).mean()


# <PRE><U>Expected Output</U>:
# 
# CRNCY
# AOA    9.136575e+09
# BBD    1.000000e+08
# BDT    1.250000e+09
# BOB    7.500000e+07
# BSD    1.500000e+07
# CAD    1.150000e+10
# CLP    1.800000e+07
# CNY    2.800000e+10
# CRC    1.397278e+11
# ...continued...
# 
# TZS    6.480530e+10
# UAH    1.644780e+09
# USD    3.564844e+09
# VND    4.212000e+12
# XOF    3.850000e+10
# ZMW    1.045850e+08
# Name: AMT_ISSUED, dtype: float64</PRE>

# <B>3.11.</B>  Reading the "Country Codes" spreadsheet, build a new "Country Codes" dataframe with two columns named <B>COUNTRY</B> and <B>CTRY_NAME</B> from the 'Country Code' and 'Full Name' columns on the spreadsheet.

# In[231]:

df_country_codes = pd.read_excel('govt_bond_feed_sample.xls', sheetname='Country Codes')

df_country_codes2 = df_country_codes.rename(columns={'Country Code':'COUNTRY', 'Full Name':'CTRY_NAME'})
df_country_codes2 = df_country_codes2.loc[:,['COUNTRY', 'CTRY_NAME']]
df_country_codes2


# <PRE><U>Expected Output</U>:
# 
#     COUNTRY        CTRY_NAME
# 0        US    United States
# 1        JN            Japan
# 2        CH            China
# 3        IT            Italy
# 4        FR           France
# 5        EN          Britain
# ... continued ...
# 211      VA          Vanuatu
# 212      VC          Vatican
# 213      VG   Virgin Islands
# 214      YE            Yemen
# 215      ZI         Zimbabwe
# 216      ZM           Zambia
# 
# [217 rows x 2 columns]</PRE>

# <B>3.12.</B>  Use a DataFrame <B>merge()</B> to do a LEFT merge/join of the Bond Feed DataFrame with the Country Codes DataFrame.  The CTRY_NAME field from Country Codes should appear as the rightmost column.  

# In[234]:

pd.merge(df1, df_country_codes2, on='COUNTRY', how='left')


# <PRE><U>To verify expected output</U>:  viewing the merge, you should see the rightmost column <B>CTRY_NAME</B> with the correct full name for each country listed in <B>COUNTRY</B> ]</PRE>
