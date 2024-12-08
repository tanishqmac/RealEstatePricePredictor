import numpy as np

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Module 'pandas' not found. Please install it using: pip install pandas")

def preprocess():
    # Load the dataset
    try:
        historical_data = pd.read_csv('/Users/Desktop/RealEstatePricePredictor/data/US_Cities_Real_Estate_Data.csv')
    except FileNotFoundError:
        print("File 'historical_data.csv' not found. Please ensure the file exists in the 'data' folder.")
        return pd.DataFrame(columns=['Location', 'Size_sqft', 'Rooms', 'Price', 'Age', 'Crime_Rate', 'Distance_to_City_Center', 'Nearby_Schools'])
    
    # Handle missing values
    numerical_data = historical_data.select_dtypes(include=['number'])
    historical_data[numerical_data.columns] = numerical_data.fillna(numerical_data.mean())
    categorical_data = historical_data.select_dtypes(exclude=['number'])
    historical_data[categorical_data.columns] = categorical_data.fillna(categorical_data.mode().iloc[0])

    # Normalize the features (excluding categorical features like 'Location')
        # Normalize numerical features (excluding 'Price' for analysis)
    numeric_features = historical_data.select_dtypes(include=['number']).drop(columns=['Price'])
    normalized_data = (numeric_features - numeric_features.min()) / (numeric_features.max() - numeric_features.min())
    historical_data.update(normalized_data)

    return historical_data


