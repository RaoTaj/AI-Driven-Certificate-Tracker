import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI-Driven Certificate & Security Monitoring", layout="wide")

# --- CSS for Center Heading ---
st.markdown("""
    <style>
    .login-title {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 30px;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Login Function ---
def login():
    # Heading
    st.markdown("<div class='login-title'>🔐 Ai Driven Certificate Monitoring</div>", unsafe_allow_html=True)

    # Center align inputs using columns
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.session_state["logged_in"] = True
            else:
                st.error("❌ Invalid username or password")

# --- Session State ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.sidebar.success("✅ Logged in as Admin")
    st.title("🔒 AI-Driven Certificate Expiry & Security Monitoring")
    st.write("Upload CSV logs or monitor live certificate expiry details")

    uploaded_file = st.file_uploader("Upload Certificate Logs (CSV)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)

        st.subheader("Summary")
        status_count = df["Status"].value_counts()
        st.bar_chart(status_count)

        st.subheader("Critical Certificates (<7 Days Left)")
        st.dataframe(df[df["Status"] == "Critical"])
