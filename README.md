# Prediction-customer-churn web app deployed on Heroku

![](https://github.com/kh-bilal/Data-Science-Portfolio/blob/main/Prediction_of_customer_churn_at_a_bank/img.png)

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run the Web App on the local machine](#run-the-Web-app-on-the-local-machine)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Bug or Feature Request](#bug-or-feature-request)
  * [Technologies Used](#technologies-used)
  
## Demo
Link: [https://prediction-customer-churn-api.herokuapp.com/](https://prediction-customer-churn-api.herokuapp.com/) 

[![](https://github.com/kh-bilal/Data-Science-Portfolio/blob/main/Prediction_of_customer_churn_at_a_bank/bank.png)](https://prediction-customer-churn-api.herokuapp.com/)


## Overview
As we know, it is much more expensive to sign in a new client than keeping an existing one. It is advantageous for banks to know what leads a client towards the decision to leave the company.Churn prevention allows companies to develop loyalty programs and retention campaigns to keep as many customers as possible.

This App predicts the likelihood that a bank customer will unsubscribe or not. 

To train the machine learning model, we used the bank_churn dataset. The data file contains 13 features about 10000 clients of the bank.

## Technical Aspect
This project is divided into four parts:
1. [Prediction of Customer Churn at a Bank: Comprehnsive data exploration, Evaluation and Comparison between several machine learning models.](https://github.com/kh-bilal/Data-Science-Portfolio/blob/main/Prediction_of_customer_churn_at_a_bank/prediction_of_customer_churn_at_a_bank.ipynb)
2. [Create pickle file for the best obtained ML model.](https://github.com/kh-bilal/Data-Science-Portfolio/blob/main/Prediction_of_customer_churn_at_a_bank/Create_pkl.ipynb)
3. [Building a Predict-Customer-Churn-Banc web app.](https://github.com/kh-bilal/Data-Science-Portfolio/blob/main/Prediction_of_customer_churn_at_a_bank/Predict-Customer-Churn-Banc.py)
4. Hosting a Streamlit web app on Heroku.

## Installation
The Code is written in Python 3.8.5. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
## Run the Web App on the local machine
Run this command in your terminal 
```bash
streamlit run Predict-Customer-Churn-Banc.py
```
## Deployement on Heroku
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Bug or Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/kh-bilal/Data-Science-Portfolio/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/kh-bilal/Data-Science-Portfolio/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://www.analyticsvidhya.com/wp-content/uploads/2015/01/scikit-learn-logo.png" width=280>](https://www.analyticsvidhya.com/wp-content/uploads/2015/01/scikit-learn-logo.png) [<img target="_blank" src="https://static.javatpoint.com/tutorial/pandas/images/python-pandas.png" width=200>](https://static.javatpoint.com/tutorial/pandas/images/python-pandas.png) [<img target="_blank" src="https://miro.medium.com/max/765/1*cyXCE-JcBelTyrK-58w6_Q.png" width=280>](https://miro.medium.com/max/765/1*cyXCE-JcBelTyrK-58w6_Q.png) [<img target="_blank" src="https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182ad27bcfbb9dff263a_RGB_Logo_Horizontal_Color_Light_Bg.png" width=200>](https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182ad27bcfbb9dff263a_RGB_Logo_Horizontal_Color_Light_Bg.png)

[<img target="_blank" src="https://logos-download.com/wp-content/uploads/2016/09/Heroku_logo.png" width=280>](https://logos-download.com/wp-content/uploads/2016/09/Heroku_logo.png)

