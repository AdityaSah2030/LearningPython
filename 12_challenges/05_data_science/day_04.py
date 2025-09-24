import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load Data and Train Model
data = pd.read_csv("experience_salary.csv")

# Prepare data for the model
X = data[["YearsExperience"]]
y = data[["Salary"]]

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)


# Streamlit App Interface
st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary:")

# Create a number input widget for the user
years_input = st.number_input(
    "Years of experience", 
    min_value=0.0, 
    max_value=50.0, 
    step=0.1
)


# Prediction and Output
# Check if the user has provided an input
if years_input:
    # Get the prediction. model.predict returns an array like [[value]],
    # so we get the first row [0] and the first item in that row [0].
    predicted_salary_value = model.predict([[years_input]])[0][0]
    
    # Display the formatted salary in Rupees, rounded to a whole number.
    st.success(f"Estimated Salary: ₹ {predicted_salary_value:,.0f}")


# Display Regression Plot
st.subheader("Regression Line")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Scatter plot of the actual data points
ax.scatter(X, y, color="blue", label="Actual Data")

# Line plot of the model's predictions
ax.plot(X, model.predict(X), color="red", label="Regression line")

# Add labels and a title to the plot
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

# Display the plot in the Streamlit app
st.pyplot(fig)