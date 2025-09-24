import numpy as np
import pandas as pd

# -------------------------------
# RANDOM SEED
# -------------------------------
# Setting a seed makes the random numbers reproducible.
# That means every time you run the code, you'll get the same results.
np.random.seed(42)

# -------------------------------
# RANDOM.UNIFORM
# -------------------------------
# np.random.uniform(low, high, size) generates random numbers 
# uniformly between 'low' and 'high'.
# Example: between 0.5 and 10, for 100 values.
years = np.random.uniform(0.5, 10, 100).round(2)

# -------------------------------
# RANDOM.NORMAL
# -------------------------------
# np.random.normal(mean, std_dev, size) generates random numbers 
# following a "normal distribution" (bell curve).
# mean = 0, standard deviation = 4000, size = 100
# This adds some realistic "noise" to our salaries dataset.
salaries = (30000 + years * 6000 + np.random.normal(0, 4000, size=100)).round(2)

df = pd.DataFrame({
    "YearsExperience": years,
    "Salary": salaries
})

df.to_csv("experience_salary.csv", index=False)
print("Data saved in file ✅")