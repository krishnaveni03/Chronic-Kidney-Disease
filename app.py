# Importing the necessary dependencies
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)  # Initializing a Flask app
model = pickle.load(open('CKD.pkl', 'rb'))  # Loading the model

@app.route('/predict', methods=['POST'])  # Route to display the single-page application
def predict():
    if request.method == 'POST':
        # Reading the inputs given by the user
        input_features = [float(request.form[x]) for x in request.form.keys()]
        features_name = ['pus_cell', 'blood glucose random', 'blood_urea',
                         'pedal_edema', 'anemia', 'diabetesmellitus', 'hypertension',
                         'hemoglobin', 'specific_gravity', 'packed_cell_volume',
                         'red_blood_cell_count', 'appetite']
        df = pd.DataFrame([input_features], columns=features_name)

        # Predictions using the loaded model file
        output = model.predict(df)

        # Showing the prediction results in a UI
        return render_template('result.html', prediction_text=output[0])
    else:
        return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Running the app
    app.run(debug=True)
