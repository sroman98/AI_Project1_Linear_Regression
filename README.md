# Life Expectancy (WHO) - Linear Regression

This program uses linear regression on Life Expectancy data from WHO (World Health Organization) to predict life expectancy given your BMI, income, drinking habits and scholarity. 

I got the dataset from https://www.kaggle.com/kumarajarshi/life-expectancy-who in case you want to check it out. The dataset contains data from the years 2000 to 2015 from countries all over the world. Predictions are based on this dataset.

The model's **coefficients** are:

[-2.47261553e-01  1.14518869e-02  6.09293093e+01 -4.71383539e-01]

This correspond to the **parameters**:

[Alcohol    BMI   Income composition of resources    Schooling]

The model has a **mean squared error** of 22.15 and a **coefficient of determination** of 0.79 (which seems ok to me).

## How to use it

Run the .py file:
`python3 linear_regression_life_expectancy.py`

The model's info will be displayed.

To make a prediction enter the requested info.

Scales for requested info are as follows:
1. **Alcohol consumption:** a number from **0** (I never drink alcohol) to **20** (I'm an alcoholic)
2. **BMI:** your body mass index (if you don't know this, enter the letter N when it asks if you know your BMI, you'll then need to enter you **height** in **m** and your **weight** in **kg**)
3. **Income:** a number from **0** (I'm broke) to **1** (I can't get richer)
4. **Schooling:** a number from **0** (I never went to school) to **20** (I have several PHDs)

After entering this info, the program will show you the prediction of your life expectancy. It will then ask you if you want to make another prediction (enter Y to make another prediction and N to stop the execution of the program).
