import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler  # Added for scaling

# 1. Load your dataset
df = pd.read_csv('car_prediction_data.csv') 

# 2. Preprocessing
df['Car_Age'] = 2024 - df['Year']

# Select features
features = ['Present_Price', 'Kms_Driven', 'Owner', 'Car_Age', 'Fuel_Type', 'Seller_Type', 'Transmission']
X = df[features]
y = df['Selling_Price']

# ONE-HOT ENCODING
X = pd.get_dummies(X, drop_first=True)

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- SCALING SECTION ---
# Create the scaler and fit it ONLY on the training data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# -----------------------

# 4. Train on SCALED data
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train_scaled, y_train)

# 5. Save the Model AND the Scaler
with open('best_random_forest_tuned.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)

print("Model and Scaler saved successfully!")
print("Feature Order:", list(X.columns))