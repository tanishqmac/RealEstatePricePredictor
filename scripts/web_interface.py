from flask import Flask, request, jsonify, render_template
import pickle
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Module 'pandas' not found. Please install it using: pip install pandas")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        size = float(request.form['Size_sqft'])
        rooms = int(request.form['Rooms'])
        age = float(request.form['Age'])
        crime_rate = float(request.form['Crime_Rate'])
        distance = float(request.form['Distance_to_City_Center'])
        # Feature vector
        features = pd.DataFrame([[size, rooms, age, crime_rate, distance]], columns=['Size_sqft', 'Rooms', 'Age', 'Crime_Rate', 'Distance_to_City_Center'])
        model = app.config['model']
        predicted_price = model.predict(features)[0]
        return render_template('index.html', prediction_text=f'Estimated Price: ${predicted_price:.2f}')
    except ValueError:
        return render_template('index.html', prediction_text='Invalid Input. Please enter valid numeric values for all fields.')

if __name__ == "__main__":
    from scripts.data_preprocessing import preprocess
from scripts.model_training import train_model

data = preprocess()
model = train_model(data)
app.config['model'] = model
app.run(debug=True)
