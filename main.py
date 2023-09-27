####################################################
# Joey Maillette and Ethan Ahn - MTE 201 Project 1 #
# ------------------------------------------------ #
# Testing our dataset for gaussian distribution    #
####################################################

import numpy as np
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors

# dataset (observed number of minutes students arrive to morning lectures past 8am)
observed_data = np.array([2.983333333, 5.6, 7.516666667, 8.833333333, 9.966666667, 11.23333333, 
                           13.9, 15.2, 15.78333333, 16.13333333, 17.51666667, 17.93333333, 18.36666667, 
                           18.63333333, 18.96666667, 19.48333333, 19.63333333, 19.65, 19.78333333, 
                           19.8, 19.83333333, 19.91666667, 19.93333333, 19.98333333, 20.41666667, 
                           20.48333333, 20.61666667, 21.9, 21.93333333, 22.4, 22.68333333, 22.7, 
                           23.03333333, 23.46666667, 23.63333333, 23.68333333, 23.71666667, 24.98333333,
                           25, 25.4, 25.41666667, 25.55, 25.9, 25.96666667, 26.23333333, 26.75, 26.76666667,
                           26.78333333, 27.03333333, 27.1, 27.28333333, 27.45, 27.45, 27.46666667, 27.58333333, 
                           27.63333333, 27.66666667, 27.68333333, 27.7, 27.75, 27.95, 27.96666667, 28.03333333, 
                           28.73333333, 28.85, 28.96666667, 28.98333333, 29, 29.25, 29.26666667, 29.31666667, 
                           29.33333333, 29.58333333, 29.63333333, 29.65, 29.68333333, 29.88333333, 29.88333333, 
                           29.96666667, 30.21666667, 30.53333333, 30.55, 30.83333333, 30.86666667, 30.9, 30.93333333, 
                           30.95, 31.15, 31.68333333, 31.73333333, 32.03333333, 32.5, 33.16666667, 33.18333333, 33.2, 
                           33.23333333, 33.25, 33.26666667, 33.3, 33.31666667, 33.33333333, 33.53333333, 34.11666667, 
                           34.15, 34.43333333, 34.46666667, 34.48333333, 34.5, 35.45, 35.61666667, 35.85, 36.75, 
                           36.76666667, 38.23333333, 38.63333333, 39.11666667, 41.8, 44.35, 46.95, 48.16666667, 0.4])

# standardized value for testing wrt. to a normal/gaussian distribution
alpha = 0.05

# Shapiro-Wilk test
stat, p_value = stats.shapiro(observed_data)
if p_value > alpha:
    print('Shapiro-Wilk: Data appears to be normally distributed.')
else:
    print('Shapiro-Wilk: Data does not appear to be normally distributed.')
# OUTPUT: Shapiro-Wilk: Data does not appear to be normally distributed.

# Anderson-Darling test
result = stats.anderson(observed_data)
if result.statistic < result.critical_values[2]:  # At the 5% significance level
    print("Anderson-Darling: Data appears to be normally distributed.")
else:
    print("Anderson-Darling: Data does not appear to be normally distributed.")
# OUTPUT: Anderson-Darling: Data does not appear to be normally distributed.

# Lilliefors test
stat, p_value = lilliefors(observed_data)
if p_value > alpha:
    print("Lilliefors: Data appears to be normally distributed.")
else:
    print("Lilliefors: Data does not appear to be normally distributed.")
# OUTPUT: Lilliefors: Data does not appear to be normally distributed.
