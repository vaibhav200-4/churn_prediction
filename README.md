# ANN-Based Customer Churn Classification 📊🤖

This project implements an **Artificial Neural Network (ANN)** for predicting customer churn based on a given dataset. The model is trained using TensorFlow and integrated into an interactive **Streamlit** web application for easy deployment and testing.

---

## 📌 Project Overview

- ✅ Built an ANN classification model to predict whether a customer will churn.
- ✅ Trained and saved the model using TensorFlow.
- ✅ Deployed an interactive web app using **Streamlit**.
- ✅ Packaged model artifacts (`.h5` and `.pkl` files) for deployment.
- ✅ Ensured version compatibility for seamless deployment on **Streamlit Cloud**.

---

## 📁 Project Structure

├── app.py # Streamlit app script
├── model.h5 # Trained ANN model
├── regression_model.h5 # (Optional) Regression model
├── label_encoder.pkl # Encoded labels
├── one_hot_encoder.pkl # One-hot encoded data
├── scaler.pkl # Scaler object for feature scaling
├── requirements.txt # Python dependencies
├── runtime.txt # Python version specification
├── *.ipynb # Experiment and development notebooks
├── pred.ipynb # Model prediction testing notebook
└── README.md # Project documentation

## 📊 Tech Stack

- **Python 3.10**
- **TensorFlow 2.15**
- **Streamlit**
- **NumPy**
- **Pandas**
- **Scikit-learn**

🌐 Deployment
This app is deployed on Streamlit Cloud.
You can try it live here: 🔗 https://ann-classification-churn-ew6pmz4retsdawgm7mplrt.streamlit.app/
