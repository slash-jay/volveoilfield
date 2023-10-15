import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")


# Read the CSV file
df = pd.read_csv('Volve.csv')

# Convert 'BORE_OIL_VOL' column to integers, handling NaN values
df['BORE_OIL_VOL'] = pd.to_numeric(df['BORE_OIL_VOL'], errors='coerce')

# Select feature columns (X) and target column (y)
X = df[['AVG_DOWNHOLE_PRESSURE', 'AVG_DOWNHOLE_TEMPERATURE', 'AVG_DP_TUBING']]
y = df['BORE_OIL_VOL']

# Initialize a SimpleImputer to fill NaN values with the mean of the respective columns
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Now, you can use X and y for training your machine learning model.
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=0)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
pickle.dump(log_reg, open('logistic.pkl', 'wb'))
