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
