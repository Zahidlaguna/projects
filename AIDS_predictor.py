import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn import tree

disease_Data = pd.read_csv('/content/dataset.csv')
symptoms_Data = pd.read_csv('/content/Symptom-severity.csv')

disease_Data['Target'] = np.where(disease_Data['Disease'].str.contains('AIDS', case=False, na=False), 1, 0)

X = disease_Data.drop(["Target", "Disease"], axis=1)
y = disease_Data["Target"]
print("The shape of the dataset is:", disease_Data.shape)

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

aids_pred = model.predict(X_test)

aids_accuracy = accuracy_score(y_test, aids_pred)
accuracy_percentage = aids_accuracy * 100

print("Accuracy score: {:.2f}%".format(accuracy_percentage))

importances = model.feature_importances_
feature_names = X.columns

indices = np.argsort(importances)[::-1]

top_k = 10

sorted_feature_names = np.array(feature_names)[indices][:top_k]
sorted_importances = importances[indices][:top_k]

plt.figure(figsize=(10, 6))
plt.bar(sorted_feature_names, sorted_importances)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Random Forest Feature Importances (Top {})'.format(top_k))
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()

model = RandomForestRegressor()
model.fit(X_train, y_train)

aids_pred = model.predict(X_test)

r2 = r2_score(y_test, aids_pred)
print("R^2 score:", r2)

estimator = model.estimators_[0] 
plt.figure(figsize=(10, 10))
tree.plot_tree(estimator, feature_names=X.columns, filled=True)
plt.title("Random Forest Regressor Tree")
plt.show()
