import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('Data/cmu-sleep.csv')

# Selecting relevant columns while dropping rows with missing values
data = data[['TotalSleepTime', 'term_gpa']].dropna()

# Reshaping data for skLearn
X = data[['TotalSleepTime']]
y = data['term_gpa']

# Creating and training model
model = LinearRegression()
model.fit(X,y)

# Predictions
y_pred = model.predict(X)

# print model results
print("Slope (cofficient):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R^2 Score:", model.score(X, y))

# sorting data for plotting regression line

X_sorted = X.sort_values(by='TotalSleepTime')
y_sorted_pred = model.predict(X_sorted)

# Plotting data and regression line

plt.style.use('seaborn-v0_8')
plt.scatter(X, y, alpha=0.5,color='steelblue',label='Data points') # data points
plt.plot(X_sorted,y_sorted_pred, color='crimson', linewidth=2,label='Regression line') # regression line



plt.xlabel("Total Sleep Time (minutes)")
plt.ylabel("Term GPA")
plt.title("Link between Student Sleep Habits and GPA (Linear Regression)")

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()