# Insurance Charges Prediction Project

## Overview  
This project uses linear regression to predict medical insurance charges based on customer features such as age, BMI, smoking status, and region. It combines exploratory data analysis with predictive modeling to extract actionable insights.

## Dataset Description  
The dataset contains medical insurance charges information for a particular person based on his/her BMI, smoking status, region, children and sex.

## Tools and Libraries Used  
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

## Steps Performed  

### 1. Data Inspection  
- Checked data types and shape using `.info()`  
- Explored dataset statistics using `.describe()`  
- Identified missing values and column distributions  

### 2. Data Cleaning & Preparation  
- Verified no null values  
- Identified categorical vs numerical columns  
- Analyzed distributions and outliers (especially in `bmi` and `charges`)  

### 3. Exploratory Data Analysis  
- Plotted distributions for categorical and numerical features  
- Compared insurance charges based on smoking status, gender, and number of children  
- Discovered that smoking has a strong impact on insurance charges  

### 4. Model Building  
- Encoded categorical variables  
- Built a linear regression model  
- Evaluated model using R², RMSE and MSE 

### 5. Key Insights  
- Smokers are charged significantly more than non-smokers  
- Gender does not have a strong effect on charges  
- BMI and number of children show moderate influence  

## Conclusion  
This project highlights key factors affecting insurance costs and provides a regression model for predicting charges. The insights can help insurance companies in pricing strategies and customer risk assessment.

## Author  
Tajwinder (Taj) Singh
