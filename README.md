# Customer_Segmentation     
# Customer Personality Analysis Dataset

Customer Personality Analysis is a detailed examination of a company’s ideal customers. This analysis assists businesses in gaining a better understanding of their customers, enabling them to tailor products and services to meet the specific needs, behaviors, and concerns of different customer segments.

## Dataset Features
 
### People

- **ID**: Customer's unique identifier
- **Year_Birth**: Customer's birth year  
- **Education**: Customer's education level 
- **Marital_Status**: Customer's marital status
- **Income**: Customer's yearly household income 
- **Kidhome**: Number of children in customer's household
- **Teenhome**: Number of teenagers in customer's household
- **Dt_Customer**: Date of customer's enrollment with the company
- **Recency**: Number of days since customer's last purchase
- **Complain**: 1 if the customer complained in the last 2 years, 0 otherwise

### Products

- **MntWines**: Amount spent on wine in the last 2 years
- **MntFruits**: Amount spent on fruits in the last 2 years
- **MntMeatProducts**: Amount spent on meat in the last 2 years
- **MntFishProducts**: Amount spent on fish in the last 2 years
- **MntSweetProducts**: Amount spent on sweets in the last 2 years
- **MntGoldProds**: Amount spent on gold in the last 2 years

### Promotion

- **NumDealsPurchases**: Number of purchases made with a discount
- **AcceptedCmp1**: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
- **AcceptedCmp2**: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
- **AcceptedCmp3**: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
- **AcceptedCmp4**: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
- **AcceptedCmp5**: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
- **Response**: 1 if customer accepted the offer in the last campaign, 0 otherwise

### Place

- **NumWebPurchases**: Number of purchases made through the company’s website
- **NumCatalogPurchases**: Number of purchases made using a catalog
- **NumStorePurchases**: Number of purchases made directly in stores
- **NumWebVisitsMonth**: Number of visits to the company’s website in the last month

    ## Data Preprocessing Notes

- **Missing Values**: There are missing values in the `Income` feature.
- **DateTime Parsing**: `Dt_Customer` feature indicating the date a customer joined the database is not parsed as DateTime.
- **Categorical Encoding**: Some features are categorical (dtype: object) and will need to be encoded into numeric forms later.

## Overview
This repository contains a dataset analysis focusing on customer segmentation and insights derived from a marketing campaign. The dataset consists of customer information including demographic details, purchase history, and campaign response data.

## Dataset Information
- Total number of data-points after removing the rows with missing values: 2216
- Total number of duplicated rows: 0

### Features
- **ID**: Unique identifier for each customer
- **Year_Birth**: Year of birth of the customer
- **Education**: Level of education of the customer
- **Marital_Status**: Marital status of the customer
- **Income**: Income of the customer
- **Kidhome**: Number of small children in the customer's household
- **Teenhome**: Number of teenagers in the customer's household
- **Dt_Customer**: Date when the customer was enrolled
- **Recency**: Number of days since the last purchase
- **MntWines**: Amount spent on wines
- **MntFruits**: Amount spent on fruits
- **MntMeatProducts**: Amount spent on meat products
- **MntFishProducts**: Amount spent on fish products
- **MntSweetProducts**: Amount spent on sweet products
- **MntGoldProds**: Amount spent on gold products
- **NumDealsPurchases**: Number of purchases made with discount
- **NumWebPurchases**: Number of purchases made through the website
- **NumCatalogPurchases**: Number of purchases made through catalog
- **NumStorePurchases**: Number of purchases made directly in stores
- **NumWebVisitsMonth**: Number of visits to the website per month
- **AcceptedCmp3-5**: Whether the customer accepted marketing campaign 3-5
- **AcceptedCmp1-2**: Whether the customer accepted marketing campaign 1-2
- **Complain**: Whether the customer has complained
- **Z_CostContact**: Cost of contacting the customer
- **Z_Revenue**: Revenue generated from the customer
- **Response**: Response to the marketing campaign

## Data Preprocessing

### Engineering Features
1. Extracting "Age" of customers from "Year_Birth"
2. Creating "Spent" feature indicating total amount spent
3. Deriving "Living_With" feature from "Marital_Status"
4. Creating "Children" feature to indicate total children
5. Feature for "Family_Size" indicating total household members
6. Introducing "Is_Parent" feature to indicate parenthood status
7. Segmenting "Education" levels into three groups

### Data Cleaning
- Dropping redundant features: Marital_Status, Dt_Customer, Z_CostContact, Z_Revenue, Year_Birth, ID

## Data Exploration and Visualization
- Analyzing distribution and relationships among features
- Identifying patterns and trends in customer behavior

## Future Engineering
- Continuously updating and refining features for better analysis and modeling


