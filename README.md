README.md

# Service Incidents : Impact Prediction

# Acceptance criteria: 
To build the best model which gives the maximum performance, and need to deploy the model with either RShiny or Flask/Heroku.

# Milestones: 
70 days to complete the Project.

# Process flow for the Project include below steps:-

## [1. Business Objective]
The Business Objective for this Project is to predict the impact of the incident raised by the customer.

## [2. DataSet Details]
-The dataset is having incidents raised by customers. Which contains an event log of an incident management process extracted from a service desk platform of an IT company.

-Dataset has 25 columns in total, in which 24 are Independent Variables and 'impact' is Target Variable. 

[Incidents_service.xlsx](https://github.com/Shruti3893/Impact_Prediction/blob/main/Incident_services.xlsx) is the provided Dataset for the Project.

## [3. Exploratory Data Analysis]

### 1) Data Visualization:
- For getting Initial Overview of Dataset I choose to get Pandas Profiling Report. Below is the link for the same.

https://github.com/Shruti3893/Impact_Prediction/blob/main/Pandas%20Profiling%20Report_Impact%20Prediction.html

- I performed complete Visualization in Tableau to get more deep hidden Insights. Below is the link for my Tableau workbook.

https://public.tableau.com/profile/shruti.bichkunde#!/vizhome/Incident_Services/Story1

### 2) Data Analysis:
- I did Missing Value Treatment on some features. 
- I eliminated duplicates among the columns. 
- I dealt with some misclassified/misinterpreted data in some columns. 
- I replaced the values with Mode (A measure of Central Tendency).

### 3) Data Preprocessing:
- I did some data transformations by hot encoding, label encoding and probability encoding on catagorical data. 
- Based on the performance of the model, the specific encoding process is selected for the final model.

### 4) Feature Selection:
1. For selecting the desired features for final model, I tried various feature selection techniques, such as 
- ExtraTreesClassifier
- SelectKModel
- Correlation
- Mutual info classif 
- Univariate Selection. 

2. I checked feature importance both graphically and analytically to come up with the list of desired columns for final model.

## [4. Model Building]
- I tried building various models with multiple algorithms such as 
1) Logistic Regression
2) Decision Tree Classifier
3) Random Forest Classifier
4) Naive Bayes Classifier 

- I also tried building models with multiple meta algorithms such as 
1) XGBoost Classifier
2) CatBoost Classifier
3) Gradient Boost
4) LGBM Classifier 
5) Neural Networks

- Based on the Classification report, I chose the best model as CatBoost Classifier for the project. It gave highest Accuracy, Precision, Recall and F1-score.

## [5. Deployment in Local System]
For Show casing the project, I used Flask Framework.

## [6. Cloud Platform]
I deployed the final model on Heroku Cloud Platform. 

To see my website/web-api Go to >>> https://impactprediction-api.herokuapp.com/

Please check the below link for Complete PPT for Project-
https://github.com/Shruti3893/Impact_Prediction/blob/main/Incident%20Services%20PPT.pptx



![template1](https://github.com/Shruti3893/Impact_Prediction/blob/main/templates/input.png)

![template1](https://github.com/Shruti3893/Impact_Prediction/blob/main/templates/output.png)

