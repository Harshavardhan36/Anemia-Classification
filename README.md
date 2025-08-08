# 🩸 Anemia Classification Using CBC Data

This is a Flask-based web application that classifies anemia types using Complete Blood Count (CBC) data.  
It uses a pre-trained machine learning model to predict whether a patient has **No Anemia**, **Iron Deficiency Anemia**, or **Vitamin Deficiency Anemia**.

---

## 🚀 Features
- **Machine Learning Models**: Gradient Boosting Classifier (trained with SMOTE to handle imbalance)
- **Accuracy**: 93.2% on validation data
- **Real-Time Predictions** via a simple web interface
- **Immediate Use**: Pre-trained model (`anemia_model.pkl`) included in the repo

---

## 🛠 Tech Stack
- Python
- Flask
- Pandas, NumPy, Scikit-learn
- Imbalanced-learn (SMOTE)
- HTML/CSS

---

## 📂 Project Structure
anemia-classification-cbc/
├── app.py # Flask application
├── train_model.py # Model training script
├── utils.py # Preprocessing functions
├── anemia_model.pkl # Pre-trained ML model
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Web interface
└── static/
└── style.css # UI styles

---

## 📥 Installation & Running the App

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Harshavardhan36/Anemia-Classification.git
cd Anemia-Classification
```

2️⃣ Create a virtual environment (optional but recommended)  
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

4️⃣ Run the app
```bash
python app.py
```

---

5️⃣ Open the app in your browser
```
http://127.0.0.1:5000/
```

---

📊 **How to Use**
- Enter patient CBC parameters:  
  - Hemoglobin (g/dL)  
  - Hematocrit (%)  
  - MCV (fL)  
  - MCH (pg)  
  - RDW (%)  
- Click **Classify**  
- The app will display the predicted anemia type.

---

🧪 **Training the Model (Optional)**
If you want to retrain the model:
```bash
python train_model.py
```
This will regenerate `anemia_model.pkl`.

---

📜 **License**  
MIT License — feel free to use and modify.

---

👨‍💻 **Author**  
Sri Harshavardhan Pulluru  
[LinkedIn](https://www.linkedin.com/in/harshavardhan3636/) | [GitHub](https://github.com/Harshavardhan36)

---
