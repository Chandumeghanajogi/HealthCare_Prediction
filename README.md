<h1>🌟 Healthcare Prediction System for Diabetic Patients </h1>

 
Welcome to the **Healthcare Prediction System for Diabetic Patients**! 

This web application leverages **machine learning** to predict whether an individual is diabetic based on their health parameters. It also provides dietary recommendations and health tips for diabetic individuals.  

---

## 🌟 Features  
- **Diabetes Prediction**: Predict if a person is diabetic using key health metrics like glucose level, BMI, insulin, and more.  
- **Interactive Diet Plans**: For diabetic users, the app provides a redirect to a beautifully designed page offering dietary plans and tips.  
- **User-Friendly Interface**: Minimalistic, responsive design with attractive pink, teal, and cream colors for a delightful experience.  
- **Real-Time Predictions**: Enter your details, and get instant predictions powered by machine learning.  
- **Tailored Recommendations**: Personalized insights for users based on prediction results.

---

## 🖥️ Tech Stack  
- **Frontend**: HTML, CSS, Tailwind CSS  
- **Backend**: Python (Flask Framework)  
- **Machine Learning**: Pre-trained classification model using scikit-learn  
- **Data Processing**: Pandas  
- **Deployment**: Flask server  

---

## 🚀 How It Works  
1. Users enter their health data into a form (e.g., glucose level, BMI, age, etc.).  
2. Data is sent to the Flask backend.  
3. The pre-trained machine learning model predicts whether the user is diabetic or non-diabetic.  
4. The result is displayed on a new page, with options for dietary recommendations for diabetic users.  

---

## 📸 Screenshots  

### 1️⃣ Home Page  
![Home Page](https://github.com/Chandumeghanajogi/HealthCare_Prediction/blob/main/images1/home.jpeg?raw=true)  
A welcoming page with a brief introduction to healthcare prediction.  

### 2️⃣ Prediction Page  
![Prediction Page](https://github.com/Chandumeghanajogi/HealthCare_Prediction/blob/main/images1/prediction.jpeg?raw=true)  
User-friendly form to input health metrics.  

### 3️⃣ Result Page  
![Result Page](https://github.com/Chandumeghanajogi/HealthCare_Prediction/blob/main/images1/nondiabetic.jpeg?raw=true)
![Result Page](https://github.com/Chandumeghanajogi/HealthCare_Prediction/blob/main/images1/diabetic.jpeg?raw=true) 
Displays the prediction result with an option to view dietary plans for diabetic users.  

### 4️⃣ Diet Recommendations  
![Diet Page](https://github.com/Chandumeghanajogi/HealthCare_Prediction/blob/main/images1/diet%20recommendation.jpeg?raw=true)  
A visually appealing page with meal plans and tips.  

---

## ⚙️ Installation  

### Prerequisites  
1. Python 3.8 or later  
2. pip (Python package manager)  

### Steps  
1. Clone this repository:  
   ```code
   git clone https://github.com/your-username/healthcare-prediction-system.git
   cd healthcare-prediction-system
2.Install the required Python libraries:
    
    pip install -r requirements.txt
    
3. Run the Flask app:
    ```code
    python app.py
    
4. Open your browser and go to http://127.0.0.1:5000/.



<h2>📂 Project Structure</h2>

├── static/
│   ├── styles.css                            # Styling for the application
│   ├── script.js                             # Any JS logic
│   └── assets/                               # Images and assets for UI
├── templates/
│   ├── index.html                            # Home and form page
│   ├── result.html                           # Prediction result page
│   ├── diet.html                             # Diet recommendations page
├── app.py                                    # Flask backend code
├── healthcare_prediction_model.pkl           # Pre-trained ML model
├── requirements.txt                          # Dependencies
└── README.md                                 # Project documentation

---



## 🧠 Machine Learning Model:

The model is trained on the Pima Indians Diabetes Dataset, which contains 768 samples with 8 health metrics.
**Algorithm**: Random Forest Classifier
Achieved an accuracy of over 80% on the validation set.

---

## 🌱 Future Enhancements:

**Exercise Plans** : Introduce workout routines for diabetic individuals.
**Doctor Consultation**: Add a feature for connecting with medical professionals.
**Mobile App** : Extend functionality to mobile platforms.

----

## 💬 Get in Touch
**Have questions or suggestions? Reach out!**

Email: **jogiveera1234@gmail.com.com**

GitHub: **https://github.com/Chandumeghanajogi**

LinkedIn: **https://www.linkedin.com/in/jogi-chandu-meghana-04969b289**



