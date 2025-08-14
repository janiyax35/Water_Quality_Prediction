from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Check if model exists, otherwise train a new one
model_path = 'water_quality_model.pkl'

if not os.path.exists(model_path):
    print("Model file not found! Please train the model first using Google Colab or create_model.py")
    print("Attempting to create a simple placeholder model...")
    
    try:
        # Try to create a simple model if dataset is available
        if os.path.exists('water_potability.csv'):
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler
            from sklearn.impute import SimpleImputer
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.pipeline import Pipeline
            
            df = pd.read_csv('water_potability.csv')
            X = df.drop('Potability', axis=1)
            y = df['Potability']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler()),
                ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
            ])
            
            pipeline.fit(X_train, y_train)
            
            with open(model_path, 'wb') as file:
                pickle.dump(pipeline, file)
            
            print("Successfully created and saved a new model!")
        else:
            print("Dataset not found! Please download water_potability.csv from Kaggle first.")
    except Exception as e:
        print(f"Error creating model: {e}")
        print("Please train the model manually and place it in the same directory as app.py")

# Load the model
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"ERROR: Could not find the model file {model_path}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded. Please train the model first.'})
            
        # Get input values from form
        features = [
            float(request.form['ph']),
            float(request.form['Hardness']),
            float(request.form['Solids']),
            float(request.form['Chloramines']),
            float(request.form['Sulfate']),
            float(request.form['Conductivity']),
            float(request.form['Organic_carbon']),
            float(request.form['Trihalomethanes']),
            float(request.form['Turbidity'])
        ]
        
        # Make prediction
        input_data = np.array(features).reshape(1, -1)
        columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                  'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']
        
        input_df = pd.DataFrame(input_data, columns=columns)
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1] * 100
        
        result = {
            'potability': int(prediction),
            'probability': round(probability, 2),
            'message': 'Water is potable (safe to drink)' if prediction == 1 else 'Water is not potable (unsafe to drink)'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)