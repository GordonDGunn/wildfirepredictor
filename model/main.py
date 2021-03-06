# Random Forest Example - Use for Reference
# https://machinelearningmastery.com/random-forest-ensemble-in-python/

# Pandas is used for data manipulation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Import the model we are using
from sklearn.ensemble import RandomForestClassifier
# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
# Use datetime for creating date objects for plotting
import datetime
# trying to calc accuracies
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
import joblib

# Read in data and display first 5 rows
features = pd.read_csv('Train&TestData.csv')
# print(features.head(5))
# print('The shape of our features is:', features.shape)

# Descriptive statistics for each column
features.describe()


# One-hot encode the data using pandas get_dummies
features = pd.get_dummies(features)
# Display the first 5 rows of the last 12 columns
# print(features.iloc[:,5:].head(5))

# Labels are the values we want to predict
labels = np.array(features['Risk'])

# Remove the labels from the features
# axis 1 refers to the columns
features= features.drop('Risk', axis = 1)

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

# print('Training Features Shape:', train_features.shape)
# print('Training Labels Shape:', train_labels.shape)
# print('Testing Features Shape:', test_features.shape)
# print('Testing Labels Shape:', test_labels.shape)

# # The baseline predictions are the historical averages
# baseline_preds = test_features[:, feature_list.index('AvgRisk')]
# # Baseline errors, and display average baseline error
# baseline_errors = abs(baseline_preds - test_labels)
# print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Instantiate model with 20 decision trees
rf = RandomForestClassifier(n_estimators=20)
# evaluate the model
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(rf, features, labels, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
# report performance
print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))

# Train the model on training data
rf.fit(train_features, train_labels)

joblib.dump(rf, "my_random_forest.joblib")

# Pull out one tree from the forest
tree = rf.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree.dot')
# Write graph to a png file
graph.write_png('tree.png')


# # Limit depth of tree to 3 levels
# rf_small = RandomForestRegressor(n_estimators=10, max_depth = 3)
# rf_small.fit(train_features, train_labels)
# # Extract the small tree
# tree_small = rf_small.estimators_[5]
# # Save the tree as a png image
# export_graphviz(tree_small, out_file = 'small_tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# (graph, ) = pydot.graph_from_dot_file('small_tree.dot')
# graph.write_png('small_tree.png');


# Get numerical feature importances
importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];

# # New random forest with only the two most important variables
# rf_most_important = RandomForestRegressor(n_estimators= 1000, random_state=42)
# # Extract the two most important features
# important_indices = [feature_list.index('temp_1'), feature_list.index('average')]
# train_important = train_features[:, important_indices]
# test_important = test_features[:, important_indices]
# # Train the random forest
# rf_most_important.fit(train_important, train_labels)
# # Make predictions and determine the error
# predictions = rf_most_important.predict(test_important)
# errors = abs(predictions - test_labels)
# # Display the performance metrics
# print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
# mape = np.mean(100 * (errors / test_labels))
# accuracy = 100 - mape
# print('Accuracy:', round(accuracy, 2), '%.')
#
# # Set the style
# plt.style.use('fivethirtyeight')
# # list of x locations for plotting
# x_values = list(range(len(importances)))
# # Make a bar chart
# plt.bar(x_values, importances, orientation = 'vertical')
# # Tick labels for x axis
# plt.xticks(x_values, feature_list, rotation='vertical')
# # Axis labels and title
# plt.ylabel('Importance'); plt.xlabel('Variable');
# plt.title('Variable Importances');
# plt.show()
#
#
# # Dates of training values
# months = features[:, feature_list.index('Month')]
# days = features[:, feature_list.index('Day')]
# years = features[:, feature_list.index('Year')]
# # List and then convert to datetime object
# dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]
# dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]
# # Dataframe with true values and dates
# true_data = pd.DataFrame(data = {'date': dates, 'actual': labels})
# # Dates of predictions
# months = test_features[:, feature_list.index('Month')]
# days = test_features[:, feature_list.index('Day')]
# years = test_features[:, feature_list.index('Year')]
# # Column of dates
# test_dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]
# # Convert to datetime objects
# test_dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in test_dates]
# # Dataframe with predictions and dates
# predictions_data = pd.DataFrame(data = {'date': test_dates, 'prediction': predictions})
# # Plot the actual values
# plt.plot(true_data['date'], true_data['actual'], 'b-', label = 'actual')
# # Plot the predicted values
# plt.plot(predictions_data['date'], predictions_data['prediction'], 'ro', label = 'prediction')
# plt.xticks(rotation = '60');
# plt.legend()
# # Graph labels
# plt.xlabel('Date'); plt.ylabel('Maximum Temperature (F)'); plt.title('Actual and Predicted Values');
# plt.show()


# Use this to plot the data to find any outliers
# date_list = list()
# for rows in features:
#     date_list.append(str(int(rows[1])) + "/" + str(int(rows[2])) + "/" + str(int(rows[0])))
# plt.plot(date_list, features[:,11])  # update number for different columns
# plt.xlabel("Date")
# plt.ylabel("HumidityMin")
# plt.xticks(date_list[::2], rotation='vertical')
# plt.locator_params(axis='x', nbins=len(date_list)/3)
# plt.show()