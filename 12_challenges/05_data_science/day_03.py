import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load the dataset from the CSV file
data = pd.read_csv("experience_salary.csv")

# 2. Prepare the data
# X should be a 2D array, so we use [[]]
X = data[["YearsExperience"]]
# y can be a 1D series or a 2D array
y = data["Salary"]

# 3. Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# 4. Extract model parameters
slope = model.coef_[0]
intercept = model.intercept_

# 5. Print the results
print("\n--- Linear Regression Model Results ---")
# The f-string formats the numbers with 2 decimal places and a thousand separator
print(f"Model Intercept (Base Salary): Rs.{intercept:,.2f}")
print(f"Model Coefficient (Slope):     Rs.{slope:,.2f}")
print("\nThis means for each additional year of experience, the salary is predicted to increase by $" + f"{slope:,.2f}.")

# 6. Visualize the results
plt.figure(figsize=(10, 6)) # Make the plot a bit larger
plt.scatter(X, y, color="blue", label="Actual Salary Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line (Predicted Salary)")

# Adding titles and labels for clarity
plt.title("Salary vs. Years of Experience", fontsize=16)
plt.xlabel("Years of Experience", fontsize=12)
plt.ylabel("Salary ($)", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout() # Adjusts plot to ensure everything fits without overlapping

# Display the plot
plt.show()