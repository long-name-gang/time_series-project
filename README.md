TIME SERIES

Time Series Project - Superstore -
By: Mathias Boissevain & Rachel Robbins-Mayhill
Codeup - Innis Cohort - April 2022
 
===
 
Table of Contents
---
 
* I. [Project Overview](#i-project-overview)<br>
[1. Goals](#1-goal)<br>
[2. Description](#2-description)<br>
[3. Initial Questions](#3initial-questions)<br>
[4. Formulating Hypotheses](#4-formulating-hypotheses)<br>
[5. Deliverables](#5-deliverables)<br>
* II. [Project Data Context](#ii-project-data-context)<br>
[1. Data Dictionary](#1-data-dictionary)<br>
* III. [Project Plan - Data Science Pipeline](#iii-project-plan---using-the-data-science-pipeline)<br>
[1. Project Planning](#1-plan)<br>
[2. Data Acquisition](#2-acquire)<br>
[3. Data Preparation](#3-prepare)<br>
[4. Data Exploration](#4explore)<br>
[5. Modeling & Evaluation](#5-model--evaluate)<br>
[6. Product Delivery](#6-delivery)<br>
* IV. [Project Modules](#iv-project-modules)<br>
* V. [Project Reproduction](#v-project-reproduction)<br>
 
 
 
## I. PROJECT OVERVIEW
 
 
#### 1.  GOAL:
The goal of this project is to identify key drivers of lost revenue for SuperStore, a retail store, and make recommendations to reduce loss in order to increase profit. 
 
 
#### 2. DESCRIPTION:
With an ever-competitive retail market, it is vital to understand your market base in order to prevent profit loss and maximize revenue.  Ultimately, knowing what components are contributing to profit loss, is important for maintaining and increasing profit.  This project will identify key drivers of loss for the Superstore dataset and use modeling and statistics to identify ways to prevent loss in the future. Ultimately it will provide a recommendation that could be used by Superstore or other customer-based service companies to maximize profit.
 
 
#### 3.INITIAL QUESTIONS:
The focus of the project is on decreasing profit loss and increasing profit. Below are some of the initial questions this project looks to answer throughout the Data Science Pipeline.
 
##### Data-Focused Questions
- What customer base contributes the most to profit loss?
- What geographic area experiences the most profit loss?
- Which product category contributes most to profit loss?
- Does shipping contribute to profit loss?
- What is our total revenue?
- What amount of revenue is impacted by the profit loss?
- What amount of revenue is impacted by the customer base that has the most loss?
- What amount of revenue is impacted by the product category that has the most loss?
 
##### Overall Project-Focused Questions
- What will the end product look like?
5-minute presentation to key stakeholder.
- What format will it be in?
Slide format, with agenda, executive summary, data overview, and recommendations.
- Who will it be delivered to?
Key stakeholder (TBD)
- How will it be used?
To recommend steps to take in order to reduce loss.
- How will I know I'm done?
When driver and recommendation have been identified, along with deliverables complete.
- What is my MVP?
Identify one driver of profit loss. 
- How will I know it's good enough?
If the exploratory process produces one data-backed driver of loss and one recommendation for that driver. 
 

#### 4. FORMULATING HYPOTHESES
- Is geographic region related to profit loss?
   + H0: The profit loss rate of a single geographic region <= the profit loss rate of all geographic regions.
   + H1: The profit loss rate of a single geographic region > the profit loss rate of all geographic regions.
 
 
#### 5. DELIVERABLES:
- [x] README file - provides an overview of the project and steps for project reproduction
- [x] Draft Jupyter Notebook - provides all steps taken to produce the project
- [x] wrangle.py - provides reproducible code to automate acquiring, preparing, and splitting the data
- [x] Report Jupyter Notebook - provides final presentation-ready wrangle and exploration
- [x] Slide Deck - includes 2 visualizations and an executive summary with recommendations and rationale
- [x] 5-minute presentation to stakeholders
 
 
## II. PROJECT DATA CONTEXT
 
#### 1. DATA DICTIONARY:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
 
|  Variables             |    Data Type                                |    Definition             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
customer_id           |               object             | unique identifier for each customer | 
is_senior                |                 integer (whole #)    |  senior citizen (65+), 0= no, 1=yes|
tenure_months       |                      integer (whole #)    | length of customer service in months|
monthly_charges     |                    float (decimal)    | current monthly charges in USD |
total_charges            |               float (decimal)    | sum of all charges for tenure in USD |
contract_type             |               object    | type of contract customer signed: month-to-month, One year, Two year|
internet_service_type |               object    | type of internet service customer has or had: Fiber optic, DSL, None|
payment_type |   object | type of payment method customer uses or used: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) |
is_male_Male         |   boolean int. (0, 1)    | binary gender identity 0= male, 1=female|    
has_partner_Yes    |                       boolean int. (0, 1)  | has spouse, partner, or significant other, 0= no, 1=yes||
has_dependents_Yes     |  boolean int. (0, 1)   | has dependent(s), children or otherwise, 0= no, 1=yes|
has_phone_service_Yes |                    boolean int. (0, 1)  | is or was a phone customer, 0= no, 1=yes|
has_multiple_lines_No phone service |      boolean int. (0, 1)  | didn’t or doesn’t have phone service, 0= no, 1=yes|
has_multiple_lines_Yes   |                 boolean int. (0, 1)  | has or had multiple phone lines, 0= no, 1=yes|
has_online_security_Yes   |  boolean int. (0, 1)| internet option: has or had service add-on, 0= no, 1=yes|
has_online_backup_Yes  | boolean int. (0, 1) | internet option: has or had service add-on, 0= no, 1=yes|
has_device_protection_Yes  |  boolean int. (0, 1)|  internet option: has or had service add-on, 0= no, 1=yes|
has_tech_support_Yes  |               boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_tv_Yes   |          boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_streaming_movies_Yes  |       boolean int. (0, 1)   | internet option: has or had service add-on, 0= no, 1=yes|
has_paperless_billing_Yes |    boolean int. (0, 1)|  customer bill is or was paperless, 0= no, 1=yes |
did_churn_Yes (target) |            boolean int. (0, 1) | customer services have been canceled, 0= no, 1=yes|  
contract_type_One year  |                  integer ( boolean 0,1|  customer has or did have 1 year contract, 0= no, 1=yes|
contract_type_Two year  |                  boolean int. (0, 1) | customer has or did have 2 year contract, 0= no, 1=yes|   
internet_service_type_Fiber optic  | boolean int. (0, 1)|  is or was a fiber optic internet customer,  0= no, 1=yes |
internet_service_type_None     | boolean int. (0, 1)| is or was an internet customer,  0= no, 1=yes |
payment_type_Credit card (automatic)   |   boolean int. (0, 1)  | payment type is or was credit card, 0= no, 1=yes |   
payment_type_Electronic check     |        boolean int. (0, 1)  | payment type is or was electronic check, 0= no, 1=yes |  
payment_type_Mailed check       |          boolean int. (0, 1)  | payment type is or was check via post, 0= no, 1=yes |
 
 
## III. PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver
 
#### 1. PLAN
- [x]  Review project expectations
- [x]  Draft project goal to include measures of success
- [x]  Create questions related to the project
- [x]  Create questions related to the data
- [x]  Create a plan for completing the project using the data science pipeline
- [x]  Create a data dictionary to define variables and data context
- [x]  Draft starting hypothesis
 
#### 2. ACQUIRE
- [x]  Create .gitignore
- [x]  Create env file with log-in credentials
- [x]  Store env file in .gitignore to ensure the security of sensitive data
- [x]  Create wrangle.py module
- [x]  Store functions needed to acquire the Superstore dataset from mySQL
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
- [x]  Using Jupyter Notebook
     - [x]  Run all required imports
     - [x] Import functions from wrangle.py module
     - [x]  Summarize dataset using methods and document observations
 
#### 3. PREPARE
Using Jupyter Notebook
- [x]  Import functions from wrangle.py module
- [x]  Summarize dataset using methods and document observations
- [x]  Clean data
- [x]  Features need to be turned into numbers
- [x]  Categorical features or discrete features need to be numbers that represent those categories
- [x]  Continuous features may need to be standardized to compare like datatypes
- [x]  Address missing values, data errors, unnecessary data, renaming
- [x]  Split data into train, validate, and test samples
Using Python Scripting Program (Jupyter Notebook)
- [x]  Create prepare function within wrangle.py
- [x]  Store functions needed to prepare the Superstore data such as:
   - [x]  Cleaning Function: to clean data for exploration
   - [x]  Encoding Function: to create numeric columns for object column
   - [x]  Feature Engineering Function: to create new features
   - [x]  Split Function: to split data into train, validate, and test
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
 
#### 4.EXPLORE
Using Jupyter Notebook:
- [x]  Answer key questions about hypotheses and find drivers of profit loss
     - [x]  Run at least two statistical tests
     - [x]  Document findings
- [x]  Create visualizations with the intent to discover variable relationships
     - [x]  Identify variables related to loss
     - [x]  Identify any potential data integrity issues
- [x]  Summarize conclusions, provide clear answers, and summarize takeaways
     - [x] Explain plan of action as deduced from work to this point
 
#### 5. MODEL & EVALUATE
Using Jupyter Notebook:
- [x]  Establish baseline accuracy
- [x]  Train and fit multiple (3+) models with varying algorithms and/or hyperparameters
- [x]  Compare evaluation metrics across models
- [x]  Remove unnecessary features
- [x]  Evaluate best performing models using validate set
- [x]  Choose best performing validation model for use on test set
- [x]  Test final model on out-of-sample testing dataset
- [x]  Summarize performance
- [x]  Interpret and document findings
 
#### 6. DELIVERY
- [x]  Prepare a five-minute presentation using Google Sheets
     - [x]  Include an introduction of the project and goals
     - [x]  Provide an executive summary of findings, key takeaways, recommendations, and rationale
     - [x]  Create a walkthrough of the analysis 
     - [x]  Include 2 presentation-worthy visualizations that support the problem and recommendation
     - [x] Provide final takeaways, recommend a course of action, and next steps
     - [x] Be prepared to answer questions following the presentation
- [x]  Prepare final notebook in Jupyter Notebook
     - [x]  Create clear walk-though of the Data Science Pipeline using headings and dividers
     - [x]  Explicitly define questions asked during the initial analysis
     - [x]  Visualize relationships
     - [x]  Document takeaways
     - [x]  Comment code thoroughly



 
 
## IV. PROJECT MODULES:
- [x] wrangle.py - provides reproducible python code to automate acquiring, preparing, and splitting the data
 
  
## V. PROJECT REPRODUCTION:
### Steps to Reproduce
 - [x] You will need an env.py file that contains the hostname, username, and password of the mySQL database that contains the superstore_db database
- [x] Store that env file locally in the repository
- [x] Make .gitignore and confirm .gitignore is hiding your env.py file
- [x] Clone our repo (including the wrangle.py)
- [x] Import python libraries:  pandas, matplotlib, seaborn, numpy, and sklearn
- [x] Follow steps as outlined in the README.md. and mathias_work.ipynb
- [x] Run Final_Report.ipynb to view the final product

