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

To see my website/web-api Go to >>> https://impactprediction-api.herokuapp.com/








### Background:

[Incidents_service.xlsx](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/Incidents_service.xlsx) as given data file.

- The dataset is having incidents raised by customers. Which contains an event log of an incident management process extracted from a service desk platform of an IT company.

- Dataset contains total 26 features, and 1.4Lac+ records. Out of which 25 features are independent and 'Impact' Feature is output variable.

- The Prediction needs to be Classified into 3 Classes:
1. High Impact
2. Medium Impact
3. Low Impact

# Project Phases:

## [1. Exploratory Data Analysis](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/tree/master/1.%20Exploratory%20Data%20Analysis)

- This Phase Includes EDA part for Project Conducted in Tableau.

- Each Categorical and Numerical variable is Visualised in Tableau session. Please find Tableau workbook [Here](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Impact_prediction%20Project%20Stories%20And%20Insights.twbx)

- Each Feature is interacting with each other, making whole workbook fully interactive. Please find the detailed workbook here: [https://public.tableau.com/profile/ashish.gore#!/vizhome/Impact_predictionProjectStories/Story2](https://public.tableau.com/profile/ashish.gore#!/vizhome/Impact_predictionProjectStories/Story2)

- Fully Interactive Dashboards were created for both Numerical as well as Categorical Features.

- After Analysis of EDA part, the data had some hidden Insights, which are mentioned using stories:

1. Story 1

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Story%201%20EDA.jpg)

2. Story 2

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Story%202%20EDA.jpg)

**For More Details on Dataset Visualisation Please visit: https://public.tableau.com/profile/ashish.gore#!/vizhome

## [2. Model Building Phase](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/tree/master/2.%20Model%20Building%20Phase)

### [1. Feature_Selection](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/1.%20Feature_Selection.ipynb)
- Out of 25 Features only top few features were contributing for the output prediction. So only those Features were kept.

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/Imp_Features.JPG)

### [2. PCA_Technique](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/2.%20PCA_Technique.ipynb)

- After Conversion of categorical variables into dummies many new columns were generated. so to reduce dimensionality PCA technique is used.
**Unsupervised Learning Technique**

### [3. LDA_Technique](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/3.%20LDA_Technique.ipynb)

- After Conversion of categorical variables into dummies many new columns were generated. so to reduce dimensionality LDA technique is used.
**Supervised Learning Technique**

#### In Both PCA and LDA Dimensionality Reduction Techniques, Algorithms Used are:

1. Algorithms:

- Decision Tree
- Random Forest
- Support Vector Classifier
- Gausian NB
- KNN

2. Meta Algorithms:

- Voting Classifier
- Bagging Classifier 
- AdaBoost Classifier
- XGBoost Classifier


### [4. Neural_Networks_Impact_prediction](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/4.%20Neural_Networks_Impact_prediction.ipynb)

Please Find More Details Here: [Model Building Phase.pptx](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/Model%20Building%20Phase.pptx)


## [3. Model Deployment Phase](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/Impact_Prediction_final_Model_py.ipynb)

- Finally Model is Deployed on AWS Cloud Platform with Flask Framework.

- Link: http://ec2-18-219-185-230.us-east-2.compute.amazonaws.com:8080/

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS1.jpg)

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS2.JPG)

