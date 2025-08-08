from flask import Flask, render_template, request
import pickle
import numpy as np
from utils import preprocess_input

app = Flask(__name__)
model = pickle.load(open('anemia_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(request.form[field]) for field in ['hemoglobin', 'hematocrit', 'mcv', 'mch', 'rdw']]
        features = preprocess_input(np.array(input_data).reshape(1, -1))
        prediction = model.predict(features)[0]

        classes = {0: 'No Anemia', 1: 'Iron Deficiency Anemia', 2: 'Vitamin Deficiency Anemia'}
        result = classes.get(prediction, "Unknown")

        return render_template('index.html', prediction_text=f"Predicted Anemia Type: {result}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
