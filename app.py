from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open('healthcare_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)  # Load the model globally

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        pregnancies = request.form.get('pregnancies')
        glucose = request.form.get('glucose')
        blood_pressure = request.form.get('bloodPressure')
        skin_thickness = request.form.get('skinThickness')
        insulin = request.form.get('insulin')
        bmi = request.form.get('bmi')
        diabetes_pedigree_function = request.form.get('diabetesPedigreeFunction')
        age = request.form.get('age')

        # Check if any of the required fields are missing
        if not all([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]):
            raise ValueError("Missing input values")

        # Convert input to float and create features array in the correct order
        features = [
            float(pregnancies),  # Correct order based on feature importance
            float(glucose),
            float(blood_pressure),
            float(skin_thickness),
            float(insulin),
            float(bmi),
            float(diabetes_pedigree_function),
            float(age)
        ]

        # Create a DataFrame with the correct column names in the order as per the model's training
        columns = [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 
            'BMI', 'DiabetesPedigreeFunction', 'Age'
        ]
        input_data = pd.DataFrame([features], columns=columns)

        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

        # return render_template('result.html', prediction_text=f'Prediction: {result}')
        return render_template('result.html', prediction_text=f'Prediction: {result}', is_diabetic=(prediction[0] == 1))

        # return render_template('index.html', prediction_text=f'Prediction: {result}')

    except ValueError as e:
        # Handle missing input data or invalid data gracefully
        return render_template('index.html', prediction_text=f'Error: {e}')

    except Exception as e:
        # Catch any other errors
        return render_template('index.html', prediction_text=f'Error: {str(e)}')
    
@app.route('/diet')
def diet():
    return render_template('diet.html')





if __name__ == '__main__':
    app.run(debug=True)
