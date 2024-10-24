Crop Recommendation System 🌱

This project is a machine learning-based application that recommends suitable crops for cultivation based on environmental parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH level, and rainfall.

Table of Contents
Introduction
Features
Technologies Used
Getting Started
Installation
Usage
Model Training
License
Introduction
The Crop Recommendation System helps farmers and agricultural planners choose the right crop to grow in a specific area based on a set of environmental features. By inputting values such as soil nutrient content and climatic conditions, the system predicts the top crops that are most likely to thrive, thus improving productivity and sustainability.

Features
Multi-crop recommendation: Recommends the top 3 crops suitable for the input conditions.
Machine learning model: The recommendation is powered by a pre-trained machine learning model.
User-friendly interface: A simple web-based form for inputting environmental parameters.
Accurate predictions: The model is trained on real agricultural datasets to provide reliable recommendations.
Technologies Used
Flask: A micro-framework for the web interface.
Scikit-learn: For machine learning algorithms.
HTML/CSS: For the front-end user interface.
Pickle: To save and load the trained machine learning model.
Python: Core programming language for back-end logic and machine learning model implementation.
Getting Started
Prerequisites
To run this project, you need to have Python 3.6+ installed on your system along with the following libraries:

bash
Copy code
Flask
Numpy
Scikit-learn
Pickle

Usage
Open the web application.
Enter the environmental parameters:
Nitrogen (N): Nitrogen content in soil.
Phosphorus (P): Phosphorus content in soil.
Potassium (K): Potassium content in soil.
Temperature: Current temperature in °C.
Humidity: Current humidity percentage.
pH: pH value of the soil.
Rainfall: Annual rainfall in mm.
Click on the Predict button.
The system will display the top 3 crops recommended for your input conditions.
Model Training
The machine learning model was trained on a dataset of crop growth conditions with the following algorithms evaluated:

Logistic Regression
Naive Bayes
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Decision Tree
Random Forest
AdaBoost
Gradient Boosting
The final model was chosen based on accuracy and prediction performance, and it was serialized using pickle.
