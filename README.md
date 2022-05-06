SuperCONSUMERS: AN EVALUATION OF SUPERSTORE CUSTOMER SEGMENTS

===

A Time Series Project        
By: Mathias Boissevain & Rachel Robbins-Mayhill     |     Codeup     |     Innis Cohort     |     April 2022
 
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
The goal of this project is to identify which of Superstore's customer segments is the best, then make recommendations on where to shift company focus in regards to customer segments. 
 
 
#### 2. DESCRIPTION:
Superstore's mission is to be the preferred supplier of workspace solutions; from home-office to the corporate office, we aspire to be the leading expert in workplace solutions for everyone! For this reason, it is important to know whether we are reaching everyone with our products and services. 
This project will use the Data Science Pipeline through the exploration portion, to identify the best customer segment for Superstore, an office supply retail store, and will provide recommendations on where to shift the company focus in order to maintain happy loyal customers while continuing to grow the customer base.
 
#### 3.INITIAL QUESTIONS:
The focus of the project is identifying the best customer segment. Below are some of the initial questions this project looks to answer throughout the Data Science Pipeline.
 
##### Data-Focused Questions
- Who are our customers?
- What does profit look like over time?
- What do sales look like over time?
- What customer base contributes the most to profit over time?
- How does profit by customer segment trend over time?
- What customer base contributes the most to sales over time
- What is the sales per customer segment over time?
- How many orders are placed annually per segment?

 
##### Overall Project-Focused Questions
- What will the end product look like?
   + 5-minute presentation to key stakeholder, with best customer segment identified and recommendation given on where to shift company focus.
- What format will it be in?
   + Slide format, with agenda, executive summary, data overview, and recommendations along with Github Repo.
- Who will it be delivered to?
   + Company CEO
- How will it be used?
   + To recommend steps to take in order to grow customer segments.
- How will I know I'm done?
   + When customer segment impact and recommendation have been identified, along with deliverables complete.
- What is my MVP?
   + Identify best customer segment in regards to ONE of the following areas (sales volume, total profit, % profit, or sales growth). 
- How will I know it's good enough?
   + If the exploratory process produces data-backed results outlining the 'best' customer segment along with an avenue for improving company profits. 
 

#### 4. FORMULATING HYPOTHESES
- Which customer segment is the best?
   + H0: The consumer customer segment's profit is <= the profit of all other customer segments.
   + H1: The consumer customer segment's profit is > the profit of all other customer segments.
 
 
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
 
 
|  Variables             |    Definition                              |    DataType             |
| :--------------------:   | :----------------------------------------: | :--------------------: |
order_date (index)    |  Date order was placed                          |  datetime64[ns]    |
order_id              |  Order identifier assigned to each product name for each order | object |
ship_date             |  Date order was shipped                         | datetime64[ns]       |
ship_mode             |  Mode of shipping for delivery:  'Standard Class', 'First Class', 'Second Class', 'Same Day'  | object      |
segment               |  Customer type: Consumer, Cooperate, Home Office  |  object     |
country               |  Country to which shipment was delivered: 'United States'  |    object   |
city                  |  City to which shipment was delivered  |  object    |
state                 |  State to which shipment was delivered  |  object    |
postal_code           |  Postal code to which shipment was delivered   |  float64   |
sales                 |  Sale total for product id * quantity in given order ($USD)  | float64     |
quantity              |  Total number of specified product ordered  | float64     |
discount              |  Percentage of discount applied to order in decimal form  | float64     |
profit                |  Sales - Product Cost  | float64     |
category              |  Category the product belongs to  | object    |
sub-category          |  Subcategory the product belongs to  |  object    |
customer_name         |  Name of customer   | object     |
product_name          |  Name of product  |  object    |
region_name           |  General area of US where order was placed: 'Central', 'South', 'East', 'West'  |  object    |
days_to_ship *        |  Number of days from order_date to ship_date  |  int64    |
* feature engineered
 
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
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
 
#### 4.EXPLORE
Using Jupyter Notebook:
- [x]  Answer key questions about hypotheses and find the best customer segment
     - [x]  Run at least two statistical tests
     - [x]  Document findings
- [x]  Create visualizations with the intent to discover variable relationships
     - [x]  Identify variables related to best customer segments
     - [x]  Identify any potential data integrity issues
- [x]  Summarize conclusions, provide clear answers, and summarize takeaways
     - [x] Explain plan of action as deduced from work to this point
 
#### 5. MODEL & EVALUATE
- [x] No modeling was necessary for this project, however, modeling could be added to next steps if desired.

#### 6. DELIVERY
- [x]  Prepare a five-minute presentation using Google Sheets
     - [x]  Include an introduction of the project and goals
     - [x]  Provide an executive summary of findings, key takeaways, recommendations, and rationale
     - [x]  Create a walkthrough of the analysis 
     - [x]  Include 2 presentation-worthy visualizations that support the problem and recommendation
     - [x]  Provide final takeaways, recommend a course of action, and next steps
     - [x]  Be prepared to answer questions following the presentation
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

