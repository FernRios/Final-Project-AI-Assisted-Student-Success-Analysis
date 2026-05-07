# Student Sleep & GPA Analysis

A simple linear regression model that explores the relationship between student sleep duration and academic performance using the CMU Sleep dataset.

## Overview

This script loads sleep and GPA data, trains a linear regression model, and produces a scatter plot with a fitted regression line to visualize the relationship between total sleep time and term GPA.

## Requirements

Install dependencies with:

```bash
pip install pandas matplotlib scikit-learn
```

## Dataset

Place `cmu-sleep.csv` in a `Data/` folder in the project root. The script uses two columns:

- `TotalSleepTime` — total sleep time in minutes (predictor)
- `term_gpa` — student's term GPA (target)

## Usage

```bash
python sleep_GPA_Relationship.py
```

The script will print the model's slope, intercept, and R² score to the console, then display a scatter plot with the regression line.

## Output

**Console:**
```
Slope (coefficient): <value>
Intercept: <value>
R^2 Score: <value>
```

**Plot:** Scatter plot of sleep time vs. GPA with a fitted regression line.
