import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load the enhanced dataset
df = pd.read_csv("C:/Users/evapa.EVAPATSBITCES/ship_fuel_model/data/merged_fuel_ais_enhanced.csv")



# Encode categorical variables
label_cols = ['fuel_type']
df_encoded = df.copy()
for col in label_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])

# Define features and target
features = [
    "distance", "fuel_type", "engine_efficiency",
    "avg_sog", "speed_std", "idle_time_pct", "trip_duration_min",
    "estimated_distance_km", "num_position_reports"
]

X = df_encoded[features]
y = df_encoded["fuel_consumption"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5]
}

grid = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=3, n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)

model = grid.best_estimator_

print("🔧 Best Parameters:", grid.best_params_)


# Evaluate
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "ship_fuel_model_enhanced.pkl")

print("✅ Enhanced model saved as ship_fuel_model_enhanced.pkl")

print("\n✅ MODEL TRAINING COMPLETE")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):,.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")



