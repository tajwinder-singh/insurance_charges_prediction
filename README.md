# Insurance Charges Prediction Project

## Overview  
This project predicts medical insurance charges based on customer features such as age, BMI, smoking status, and region. It combines exploratory data analysis with predictive modeling and is deployed as a web application using Flask and AWS Elastic Beanstalk.

## Dataset Description  
The dataset contains medical insurance charges information for individuals, including BMI, smoking status, region, number of children, and sex.

## Tools and Libraries Used  
- Python 3.12  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn 1.7.1  
- Flask  
- Gunicorn  
- AWS Elastic Beanstalk  

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
- Discovered smoking has a strong impact on insurance charges  

### 4. Model Building  
- Encoded categorical variables  
- Built a linear regression model  
- Evaluated model using R², RMSE, and MSE  
- Saved preprocessing objects and model using `pickle` (ct_ohe.pickle, minmax.pickle, polyfeatures.pickle, medical_charges_prediction.pickle) with **Scikit-learn version 1.7.1** to ensure compatibility during deployment  

### 5. Web App Deployment  
- Created `app.py` (Flask application)  
- Created `requirements.txt` specifying all dependencies  
- Created `Procfile` to run Gunicorn: web:gunicorn app:application
- Configured AWS Elastic Beanstalk environment:  
- Platform: Python 3.12 running on 64bit Amazon Linux 2023  
- Region: ap-south-1  
- Deployed the app using `eb init`, `eb create`, and `eb deploy`  
- Verified deployment URL and tested endpoints  

### 6. Key Insights  
- Smokers are charged significantly more than non-smokers  
- Gender does not have a strong effect on charges  
- BMI and number of children show moderate influence  

### App link:
http://medical-charges-env.eba-2eshmaxd.ap-south-1.elasticbeanstalk.com/

### Dashboard:
<img width="1365" height="630" alt="image" src="https://github.com/user-attachments/assets/3cd17203-1340-4a79-a10f-9c976bb5ba8c" />

## Deployment Instructions for Future Users  
1. Clone the repository.  
2. Install dependencies:  
   pip install -r requirements.txt
3. Initialize Elastic Beanstalk:
   eb init

Choose Python 3.12 on 64bit Amazon Linux 2023
Choose your region (ap-south-1)

4. Create the environment and deploy:
   eb create <environment-name>
   eb deploy

5. Access the app using the provided EB URL.

## Author
Tajwinder Singh

## LinkedIn
https://www.linkedin.com/in/tajwinder-singh-?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDuXVqgdxTaycCeffmt54iw%3D%3D
