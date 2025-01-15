import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Step 1: Generate hypothetical dataset
np.random.seed(42)  # For reproducibility

data = {
    "Week": range(1, 11),
    "Hours_Studied": np.random.randint(2, 11, size=10),  # Random hours between 2 and 10
    "Attendance_Rate": np.random.randint(70, 101, size=10),  # Random attendance % between 70 and 100
}
# Simulate Final Grade as a function of Hours_Studied and Attendance_Rate with some randomness
data["Final_Grade"] = (
    5 * data["Hours_Studied"] + 0.3 * data["Attendance_Rate"] + np.random.normal(0, 5, 10)
).astype(int)

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Perform regression analysis
def run_regression(df, predictor, outcome="Final_Grade"):
    X = sm.add_constant(df[predictor])  # Add constant for intercept
    y = df[outcome]
    model = sm.OLS(y, X).fit()  # Fit the model
    return model

# Regressions for Hours_Studied and Attendance_Rate
hours_model = run_regression(df, "Hours_Studied")
attendance_model = run_regression(df, "Attendance_Rate")

# Step 3: Visualizations
def plot_regression(df, predictor, outcome, model, title):
    plt.scatter(df[predictor], df[outcome], color="blue", label="Data points")
    plt.plot(df[predictor], model.predict(sm.add_constant(df[predictor])), color="red", label="Fit line")
    plt.xlabel(predictor)
    plt.ylabel(outcome)
    plt.title(title)
    plt.legend()
    plt.show()

# Plot Hours_Studied vs Final_Grade
plot_regression(df, "Hours_Studied", "Final_Grade", hours_model, "Final Grade vs Hours Studied")

# Plot Attendance_Rate vs Final_Grade
plot_regression(df, "Attendance_Rate", "Final_Grade", attendance_model, "Final Grade vs Attendance Rate")

# Results summary
hours_summary = hours_model.summary()
attendance_summary = attendance_model.summary()

df, hours_summary, attendance_summary
