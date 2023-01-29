# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())
# Create a scatter plot of score vs completed
plt.scatter(codecademy.score, codecademy.completed)
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot
# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data = codecademy)
results = model.fit()
print(results.params)
# Intercept interpretation:
print("y = 1.3 x + 13.21")
print("Intercept: The expected score for a learner with 0 content items is 13.2 ")
# Slope interpretation:
print("Slope: For every item completed, the student is expected to score 1.3 higher ")
# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot
# Predict score for learner who has completed 20 prior lessons
pred= results.predict({'completed':[20]})
print("predicted quiz score for a learner who has previously completed 20 other content items:" + str(pred))
# Calculate fitted values
fitted_values = results.predict(codecademy)
# Calculate residuals
residuals = codecademy.score - fitted_values
# Check normality assumption
plt.hist(residuals)
# Show then clear the plot
plt.show() # Show the plot
plt.clf() # Clear the plot
# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
# Show then clear the plot
plt.show() # Show the plot
plt.clf() # Clear the plot
# Create a boxplot of score vs lesson
sns.boxplot(x= 'lesson', y= 'score', data=codecademy)
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot
# Fit a linear regression to predict score based on which lesson they took
model2 = sm.OLS.from_formula('score ~ lesson', data= codecademy)
results2 = model2.fit()
print(results2.params)
# Calculate and print the group means and mean difference (for comparison)
mean_score_lessonA = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
mean_score_lessonB = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
print('Mean score (A): ', mean_score_lessonA)
print('Mean score (B): ', mean_score_lessonB)
print('Mean score difference: ', mean_score_lessonA - mean_score_lessonB)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()
