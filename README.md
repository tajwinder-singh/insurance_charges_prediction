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

## Repository Structure  
medical_charges_prediction/
│
├── app.py # Flask app for deployment
├── requirements.txt # Python dependencies
├── Procfile # Gunicorn startup file
├── .gitignore
├── README.md
├── dataset.csv # Original dataset
├── ct_ohe.pickle # Preprocessing object
├── minmax.pickle # Preprocessing object
├── polyfeatures.pickle # Preprocessing object
├── medical_charges_prediction.pickle # Trained model
├── notebooks/
│ └── model_training.ipynb # EDA & model building
└── static/ # (Optional) static files for Flask
└── templates/ # includes frontend html


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