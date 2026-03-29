routewise-ai-travel-assistant
# RouteWise AI Travel Assistant

## Project Overview
RouteWise AI Travel Assistant is a command-line based intelligent travel planning system that helps users choose the best transportation mode between cities. The system evaluates travel options such as **Car, Bus, Train, and Flight** and recommends the most suitable option based on **travel time, cost, and predicted comfort** using machine learning.

This project was created as part of the **Fundamentals of AI and ML – Bring Your Own Project (BYOP)** assignment.

---

## Problem Statement
When planning a trip, travelers often struggle to decide which transport option is best. Factors such as travel time, cost, comfort, and road conditions must all be considered.

Comparing these factors manually can be confusing and time-consuming.

This project solves that problem by creating an **AI-based travel assistant** that automatically compares travel options and recommends the best one.

---

## Features
- AI-based comfort prediction using **Decision Tree Classifier**
- Travel planning between cities
- Comparison of **travel time and cost**
- Intelligent travel recommendations
- Destination travel guide information
- **Graph visualization** comparing transport modes
- Interactive command-line interface

---

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Colorama
- Pickle

---

## Machine Learning Model

The project uses a **Decision Tree Classifier** to predict the comfort level of transportation modes.

### Input Features
- Travel Time
- Seat Comfort
- Noise Level
- Stability

### Output
- Comfort Level (Low / Medium / High)

The model is trained using the dataset **transport_conditions.csv** and saved as **comfort_model.pkl**.

---

## How to Run the Project

### Install Dependencies

pip install pandas scikit-learn matplotlib colorama
Train the Model
python train_model.py
Run the Travel Assistant
python travel_assistant.py
Example Workflow
User selects Plan a Trip
User enters starting city and destination
System calculates travel options
Machine learning model predicts comfort level
Assistant recommends:
Fastest mode
Cheapest mode
Most comfortable mode
Learning Outcomes
Through this project, the following AI/ML concepts were applied:
Machine learning model training
Decision Tree classification
Data processing using Pandas
Model serialization using Pickle
Data visualization using Matplotlib
