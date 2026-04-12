# 🚗 Car Price Prediction API (FastAPI + Machine Learning)

## 📌 Project Overview

This project is a **Machine Learning + FastAPI web application** that predicts the price of a used car based on multiple features such as year, kilometers driven, fuel type, transmission, owner type, and company.

It includes:

* 🤖 Machine Learning model (Random Forest)
* ⚡ FastAPI backend (REST API)
* 🎨 Streamlit frontend (User Interface)

---

## 🚀 Features

* Predict car prices using ML model
* REST API built with FastAPI
* Interactive UI using Streamlit
* Data preprocessing with OneHotEncoding
* Clean modular project structure

---

## 🧠 Tech Stack

* Python
* FastAPI
* Uvicorn
* Scikit-learn
* Pandas
* NumPy
* Streamlit

---

## 📂 Project Structure

```
car_price_predict_AI/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── models/
│   └── schemas/
│
├── ml/
│   ├── train.py
│   ├── preprocess.py
│   └── model.pkl
│
├── data/
│   └── car_data.csv
│
├── frontend.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Train the Model

```bash
python ml/train.py
```

---

## ⚡ Run FastAPI Server

```bash
python run.py
```

👉 Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Run Frontend (Streamlit)

```bash
python -m streamlit run frontend.py
```

👉 Open:

```
http://localhost:8501
```

---

## 📊 API Usage

### Endpoint:

```
POST /predict
```

### Sample Input:

```json
{
  "year": 2020,
  "km_driven": 25000,
  "fuel": "Petrol",
  "transmission": "Manual",
  "owner": "First",
  "company": "Maruti"
}
```

### Sample Output:

```json
{
  "predicted_price": 634000
}
```

---

## 📈 Model Details

* Algorithm: Random Forest Regressor
* Preprocessing: OneHotEncoding
* Features:

  * Year
  * KM Driven
  * Fuel Type
  * Transmission
  * Owner
  * Company

---



## 👨‍💻 Author

Kushal B G

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and free to use.
