import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Car Price AI", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
html, body, [class*="css"] {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.center-card {
    background: rgba(30, 41, 59, 0.8);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
}

.stTextInput input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 8px;
}

.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "token" not in st.session_state:
    st.session_state.token = None

if "page" not in st.session_state:
    st.session_state.page = "login"

# ---------- HEADER ----------
st.markdown("<div class='title'>🚗 Car Price AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered car price prediction</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------- AUTH ----------
if st.session_state.token is None:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='center-card'>", unsafe_allow_html=True)

        # Toggle buttons
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Login"):
                st.session_state.page = "login"
        with c2:
            if st.button("Signup"):
                st.session_state.page = "signup"

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- LOGIN ----------
        if st.session_state.page == "login":
            st.subheader("🔐 Login")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login Now"):

                res = requests.post(
                    f"{API_URL}/login",
                    params={"username": username, "password": password}
                )

                if res.status_code == 200:
                    try:
                        data = res.json()
                    except:
                        st.error("Invalid server response ❌")
                        st.text(res.text)
                        st.stop()

                    if "access_token" in data:
                        st.session_state.token = data["access_token"]
                        st.success("Login successful ✅")
                        st.rerun()
                    else:
                        st.error(data.get("error", "Login failed ❌"))
                else:
                    st.error("Server error ❌")
                    st.text(res.text)

        # ---------- SIGNUP ----------
        else:
            st.subheader("📝 Signup")

            username = st.text_input("Create Username")
            password = st.text_input("Create Password", type="password")

            if st.button("Create Account"):

                res = requests.post(
                    f"{API_URL}/signup",
                    params={"username": username, "password": password}
                )

                if res.status_code == 200:
                    st.success("Account created 🎉 Please login")
                    st.session_state.page = "login"
                else:
                    st.error("Signup failed ❌")
                    st.text(res.text)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------- MAIN APP ----------
else:

    col1, col2 = st.columns([8,1])
    with col2:
        if st.button("Logout"):
            st.session_state.token = None
            st.rerun()

    st.subheader("🚘 Enter Car Details")

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year", 2000, 2025, 2020)
        fuel = st.selectbox("Fuel", ["Petrol", "Diesel"])
        owner = st.selectbox("Owner", ["First", "Second"])

    with col2:
        km = st.number_input("KM Driven", value=20000)
        transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
        company = st.selectbox("Company", ["Maruti", "Hyundai", "Honda"])

    if st.button("🚀 Predict Price"):

        headers = {"Authorization": f"Bearer {st.session_state.token}"}

        data = {
            "year": year,
            "km_driven": km,
            "fuel": fuel,
            "transmission": transmission,
            "owner": owner,
            "company": company
        }

        res = requests.post(
            f"{API_URL}/predict",
            json=data,
            headers=headers
        )

        try:
            result = res.json()
            st.success(f"💰 Price: ₹ {int(result['predicted_price']):,}")
        except:
            st.error("Prediction failed ❌")