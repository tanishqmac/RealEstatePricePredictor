try:
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    import shap
except ModuleNotFoundError:
    print("Module 'sklearn' or 'shap' not found. Please install them using: pip install scikit-learn shap")

def train_model(data):
    if data.empty or 'Price' not in data.columns:
        print("Data is missing or 'Price' column not found. Cannot train model.")
        return None
    
    # Split the data into train and test sets
    X = data.drop(['Price', 'Location'], axis=1)
    y = data['Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a random forest regressor model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Evaluate the model
    predictions = rf_model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Random Forest Mean Squared Error: {mse}')

    # Hyperparameter tuning using GridSearchCV
    param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
    grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=3)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    print(f'Best parameters found: {grid_search.best_params_}')

    # SHAP feature importance
    explainer = shap.TreeExplainer(best_model)
    shap_values = explainer.shap_values(X_train)
    shap.summary_plot(shap_values, X_train)

    return best_model


