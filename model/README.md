main.py in model folder contains the random forest
code for the model, this is where it is trained
and tested. The current accuracy of the model is 0.939.

my_random_forest.joblib is the export of the model.

to load the model into your code use: 
loaded_rf = joblib.load("my_random_forest.joblib")

then you can run the prediction function:
y = loaded_rf.predict(X)

where X is the features in an array. This can be done by
loading in a csv that matches the headers in Train&TestData.csv
without the "Risk" column. (Fill in PredictionData.csv)

y is the predicted value or array for each input in X
0 or 1 (no risk or yes risk)
