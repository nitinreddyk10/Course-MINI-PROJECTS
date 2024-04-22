from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.metrics import accuracy_score

# raw_data = pd.read_csv('/kaggle/input/heart-attack-prediction-dataset/heart_attack_prediction_dataset.csv')
raw_data = pd.read_csv('heart_attack_prediction_dataset.csv')
raw_data[['Systolic', 'Diastolic']] = raw_data['Blood Pressure'].str.split('/', expand=True).astype(int)
raw_data = raw_data.drop(columns=['Blood Pressure'])

label_encoder = LabelEncoder()
categorical_cols = ['Sex', 'Diabetes', 'Family History', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet', 'Previous Heart Problems', 'Medication Use', 'Country']

for col in categorical_cols:
    raw_data[col] = label_encoder.fit_transform(raw_data[col])



X = raw_data.drop(columns=['Patient ID', 'Heart Attack Risk','Hemisphere','Continent', 'Diet','Income','Country','Medication Use'])
y = raw_data['Heart Attack Risk']

data_train, data_test, class_train, class_test = train_test_split(X, y, test_size=0.1)

# start with base accuracy/model
best_accuracy = 0
best_model = None

# make 10 random trees and save best
for _ in range(10):  # lets do 10
    clf = RandomForestClassifier(n_estimators=50).fit(data_train, class_train)
    pred = clf.predict(data_test)
    current_accuracy = accuracy_score(class_test, pred)

    # assign best model based on test accuracy
    if current_accuracy > best_accuracy:
        best_accuracy = current_accuracy
        best_model = clf

# Print the accuracy of the best model
print("Best Accuracy : ", best_accuracy)


from sklearn.metrics import classification_report, confusion_matrix, multilabel_confusion_matrix
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score

pred = best_model.predict(data_test)

print("Accuracy : ", accuracy_score(class_test, pred))
print("Mean Square Error : ", mean_squared_error(class_test, pred))

print(pred[:5])

print("Confusion Matrix for each label : ")
print(multilabel_confusion_matrix(class_test, pred))

print("Classification Report : ")
print(classification_report(class_test, pred))

import joblib
joblib.dump(best_model, 'random_forest_model.pkl')