README.md

# Service Incidents : Impact Prediction

# Acceptance criteria: 
To build the best model which gives the maximum performance, and need to deploy the model with either RShiny or Flask/Heroku.

# Milestones: 
50 days to complete the Project.

Process flow for the Project include below steps:-

1] Business Objective-
To predict the impact of the incident raised by the customer.

2] DataSet Details-
The dataset is having incidents raised by customers. Which contains an event log of an incident management process extracted from a service desk platform of an IT company

3] Data Visualization-
Dataset has 25 columns in total, in which 24 are Independent Variables and 'impact' is Target Variable. 

4] Data Analysis-
I did Missing Value Treatment on some features. I eliminated duplicates among the columns. I dealt with some misclassified/misinterpreted data in some columns. I replaced the values with Mode (A measure of Central Tendency).

5] Data Preprocessing-
I did some data conversions by Performing hot encoding, label encoding and probability encoding on catagorical data. Based on the performance of the model, the specific encoding process is selected for the final model.

6] Feature Selection-
For selecting the desied features for final model, I tried various feature selection techniques, such as ExtraTreesClassifier, SelectKModel, Correlation, Mutual info classif and also Univariate Selection. I checked feature importance both graphically and analytically to come up with the list of desired columns for final model.

7] Model Building: 
I built various models with multiple algorithms such as Logistic Regression, Decision Tree Classifier, Random Forest Classifier, Naive Bayes Classifier and with multiple meta algorithms such as XGBoost Classifier, CatBoost Classifier, Gradient Boost, LGBM Classifier and with Neural Networks. Based on the Classification report, I choosed the best model as CatBoost Classifier for the project.

8] Deployment in Local System:
For Show casing the project, I used Flask Framework.

9] Cloud Platform: 
I deployed the final model on Heroku Cloud Platform. 

To see my website/web-api Go to >>> 