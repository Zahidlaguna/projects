import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix ,classification_report
import matplotlib.pyplot as plt

disease = pd.read_csv('/Users/zahidlaguna/Downloads/archive (2)/dataset.csv')
disease.dropna()
disease.describe()
print(disease)

