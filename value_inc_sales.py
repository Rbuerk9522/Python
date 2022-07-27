# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:32:49 2022

@author: Rodney Buerkley
"""

import pandas as pd

transactions = pd.read_csv('transaction.csv', sep = ';')

transactions.info()

cost_per_item = transactions['CostPerItem']
sellingprice_per_item = transactions['SellingPricePerItem']
Num_Items_Purchased = transactions['NumberOfItemsPurchased']

Profit_per_Item = Num_Items_Purchased - cost_per_item

Profit_Per_Transaction = Num_Items_Purchased * Profit_per_Item
Cost_Per_Transaction = Num_Items_Purchased * cost_per_item
SellingPrice_Per_Transaction = Num_Items_Purchased * sellingprice_per_item

# Cost per transaction
transactions['CostPerTransaction'] = transactions['CostPerItem'] * transactions['NumberOfItemsPurchased']

# Sales per transaction
transactions['SalesPerTransaction'] = transactions['SellingPricePerItem'] * transactions['NumberOfItemsPurchased']

# Profit per transaction
transactions['ProfitPerTransaction'] = transactions['SalesPerTransaction'] - transactions['CostPerTransaction']

# Markup
transactions['Markup'] = round(transactions['ProfitPerTransaction'] / transactions['CostPerTransaction'], 3)

# Date joining
transactions['Date'] = transactions['Day'].astype(str) + '-' +transactions['Month'] + '-' + transactions['Year'].astype(str)

# Split client keywords
split_client_keywords = transactions['ClientKeywords'].str.split(',', expand = True)

# Cleaning split client keywords
split_client_keywords[0] = split_client_keywords[0].str.replace('[', '')
split_client_keywords[2] = split_client_keywords[2].str.replace(']', '')

# Adding Client Keywords Columns to DataFrame
transactions['ClientAge'] = split_client_keywords[0]
transactions['ClientType'] = split_client_keywords[1]
transactions['ContractLength'] = split_client_keywords[2]

# Making Item Description Lowercase
transactions['ItemDescription'] = transactions['ItemDescription'].str.lower()

# Merging Seasons data into transaction data
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')
transactions = pd.merge(transactions, seasons, on='Month')

# Dropping Unnecessary Columns
transactions = transactions.drop(['ClientKeywords', 'Year', 'Month', 'Day'], axis=1)

# Export Data into a .csv
transactions.to_csv('Value_Inc_Cleaned.csv', index=False)





























