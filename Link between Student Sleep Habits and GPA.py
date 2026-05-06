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

# Plotting data and regression line
plt.scatter(X, y, alpha=0.5,color='blue')
plt.plot(X,y,alpha=0.5, color = 'red')


plt.xlabel("Total Sleep Time (minutes)")
plt.ylabel("Term GPA")
plt.title("Link between Student Sleep Habits and GPA (Linear Regression)")

plt.show()