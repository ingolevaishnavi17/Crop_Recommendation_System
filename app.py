from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('crop_recommendation_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/predict_page')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # Extract features from form input (you will need to map this from your form)
    nitrogen = float(request.form['N'])
    phosphorus = float(request.form['P'])
    potassium = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])


        # Prepare feature array
    features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

        # Get predicted probabilities for each crop
    probabilities = model.predict_proba(features)

        # Get the top 3 crops with the highest probabilities
    top_n = 3  # You can adjust this to 2, 3, or more crops
    top_indices = np.argsort(probabilities[0])[-top_n:][::-1]
    top_crops = [model.classes_[i] for i in top_indices]

        # Format the output
    predicted_crops = ''.join([f'<li>{crop}</li>' for crop in top_crops])

        # Return the predictions as bold and centered
    return render_template('result.html', crops=top_crops)

if __name__ == '__main__':
    app.run(debug=True)
