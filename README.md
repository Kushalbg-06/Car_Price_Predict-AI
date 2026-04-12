# 🚗 Car Price Predictor AI (Full Stack ML + FastAPI + Supabase)

## 📌 Overview

This is a **full-stack AI-powered web application** that predicts the price of a used car based on user inputs.
The system includes:

* 🤖 Machine Learning model (price prediction)
* ⚡ FastAPI backend (secure REST API)
* 🎨 Streamlit frontend (modern UI)
* 🔐 JWT Authentication (login system)
* 🗄️ Supabase (PostgreSQL database)

---

## 🚀 Features

✅ Predict car prices using AI
✅ Secure login system (JWT)
✅ Store predictions in database
✅ Modern dark-themed UI
✅ Full-stack architecture
✅ Real-time API integration

---

## 🧠 Tech Stack

* Python
* FastAPI
* Uvicorn
* Streamlit
* scikit-learn
* Supabase
* python-jose
* passlib

---

## 🏗️ Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend
   ├── Auth (JWT)
   ├── Prediction API
   └── Supabase Database
        ↓
ML Model (scikit-learn)
```

---

## 📂 Project Structure

```bash
car_price_predict_AI/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── routes.py
│   │   └── auth.py
│   ├── core/
│   │   ├── security.py
│   │   ├── hash.py
│   │   └── deps.py
│   ├── services/
│   │   └── predictor.py
│   ├── db/
│   │   └── supabase.py
│   └── schemas/
│
├── ml/
│   ├── train.py
│   └── model.pkl
│
├── frontend.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/car-price-predictor-ai.git
cd car-price-predictor-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Train ML Model

```bash
python ml/train.py
```

---

## 🔐 Environment Variables

Create `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
```

---

## ⚡ Run Backend (FastAPI)

```bash
python run.py
```

👉 Open:

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

## 🔐 Authentication Flow

1. Signup → create user
2. Login → get JWT token
3. Use token to access `/predict`

---

## 📊 API Example

### Request:

```json
{
  "year": 2020,
  "km_driven": 20000,
  "fuel": "Petrol",
  "transmission": "Manual",
  "owner": "First",
  "company": "Maruti"
}
```

### Response:

```json
{
  "predicted_price": 634000
}
```

---

## 🗄️ Database (Supabase)

Table: `predictions`

| Column       | Type |
| ------------ | ---- |
| id           | int  |
| year         | int  |
| km_driven    | int  |
| fuel         | text |
| transmission | text |
| owner        | text |
| company      | text |
| price        | int  |

---

## 🔥 Future Improvements

* 📊 Add prediction history dashboard
* 📈 Add charts & analytics
* 🌐 Deploy on cloud (Render / Railway)
* 🔐 OAuth login (Google login)
* 🤖 Add AI chatbot assistant

---

## 🎤 Resume Description

**Car Price Predictor AI (Full Stack ML Project)**

* Built an end-to-end ML system using scikit-learn
* Developed secure REST APIs with FastAPI
* Implemented JWT authentication using python-jose
* Integrated Supabase PostgreSQL database
* Designed modern UI using Streamlit

---

## 👨‍💻 Author

Kushal B G

---


