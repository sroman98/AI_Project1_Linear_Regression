# Sandra Román Rivera
# Dataset obtained from:
# https://www.kaggle.com/kumarajarshi/life-expectancy-who

import numpy as np
import math
import pandas as pd

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv('Life Expectancy Data.csv', usecols=["Year", "Life expectancy ", "Alcohol", " BMI ", "Income composition of resources", "Schooling"])

# Clean data
df.replace(['', 0], np.nan, inplace=True)
df.dropna(inplace=True)

attributes = ["Alcohol", " BMI ", "Income composition of resources", "Schooling"]

df_x = df[attributes]
df_y = df["Life expectancy "]

# Use 20% of the data for testing
test_size = -1 * math.floor(df_y.size * 0.2)

# Split the data into training/testing sets
x_train = df_x[:test_size]
x_test = df_x[test_size:]
y_train = df_y[:test_size]
y_test = df_y[test_size:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model
regr.fit(x_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(x_test)

print("MODEL")
print('Coefficients: \n', regr.coef_)
print('Mean squared error: \n %.2f' % mean_squared_error(y_test, y_pred))
print('Coefficient of determination: \n %.2f' % r2_score(y_test, y_pred))

# Used in jupiter notebook to plot data
#pd.plotting.scatter_matrix(df, figsize=(12,12))

# Predictions with inputs
print("\nPREDICT YOUR LIFE EXPECTANCY BASED ON WORLD'S DATA FROM THE YEARS %i-%i" %(df["Year"].min(), df["Year"].max()))

predict = "Y"

while predict == "Y" or predict == "y":
  alcohol = float(input("Alcohol consumption (0-20): "))

  knowsBMI = input("Do you know your BMI? (Y/N): ")
  if knowsBMI == "Y" or knowsBMI == "y":
    bmi = float(input("BMI: "))
  else:
    # Calculate BMI
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    bmi = weight / height ** 2
    print("Your BMI is ", bmi)

  income = float(input("Income (0-1): "))
  schooling = float(input("Schooling (0-20): "))

  # Create data frame with predictions
  df_pred = pd.DataFrame([(alcohol, bmi, income, schooling)], columns = attributes)

  print("\nYou'll live around %i years" %round(regr.predict(df_pred)[0]))
  
  predict = input("Do you want to make another prediction? (Y/N): ")
  print("")

print("Spoiler: In the end we all die D:")
