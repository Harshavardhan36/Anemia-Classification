# 🩸 Anemia Classification Using CBC Data

This is a Flask-based web application that classifies anemia types using Complete Blood Count (CBC) data.  
It uses machine learning models trained on sample CBC data to predict whether a patient has **No Anemia**, **Iron Deficiency Anemia**, or **Vitamin Deficiency Anemia**.

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
├── app.py               # Flask application
├── train_model.py       # Model training script
├── utils.py             # Preprocessing functions
├── anemia_model.pkl     # Pre-trained ML model
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Web interface
└── static/
    └── style.css        # UI styles

---

### Why this works:
- The triple backticks (```) before and after keep everything in a **monospaced block**.
- The tree uses Unicode characters (`├──`, `└──`, `│`) so it looks clean.
- Each file has its **comment aligned** for easy reading.

---

Do you want me to **update the full README** with this fixed structure so you can just copy and paste it in GitHub? That way it will look perfect when recruiters see it.

