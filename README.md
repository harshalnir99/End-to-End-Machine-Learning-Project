# Sensor-Fault-Detection

### Problem Statement:- 
Predict whether income exceeds $50K/yr based on census data. Also known as "Census Income" dataset.

### Solution:- 
We are working on Income Prediction problem associated with the Adult Income Census dataset. The goal is to accurately predict whether or not person is making more or less than $50,000 a year by using different machine Learning Algorithms & choose Best ML Model & deploy on web server. 

#### About the Dataset
- **Age:** Describes the age of individuals. Continuous.
- **Workclass:** Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- **fnlwgt:** Continuous.
- **education:** Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
- **education-num:** Number of years spent in education. Continuous.
- **marital-status:** Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- **occupation:** Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- **relationship:** Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- **race:** White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
- **sex:** Female, Male.
- **capital-gain:** Continuous.
- **capital-loss:** Continuous.
- **hours-per-week:** Continuous.
- **native-country:** United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
- **salary:** >50K,<=50K

### Step We Followed:-
1. Data Ingestion
2. Data Transformation
3. Model Trainer
4. Predication Pipeline
5. Training Pipeline

## Tech Stack Used
1. Python 
2. EDA
3. Machine learning algorithms
4. Deployment


### Step 1: Clone the repository
```
git clone https://github.com/harshalnir99/End-to-End-Machine-Learning-Project.git
```

## Step 2- Create a conda environment after opening the repository

```
conda create -n income python=3.7.6 -y
```

```
conda activate income
```

### Step 3 - Install the requirements
```
pip install -r requirements.txt
```


