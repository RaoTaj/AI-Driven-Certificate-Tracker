# 🔒 AI-Driven Certificate Expiry & Security Monitoring

This project is a **Streamlit-based dashboard** that helps you upload and analyze certificate logs, monitor expiry details, and visualize certificate status in real-time.  
It also includes a **login authentication system** to restrict access.

---

## 🚀 Features
- Secure **login authentication** (username/password)
- Upload certificate logs in **CSV format**
- **Interactive DataFrame view** for uploaded logs
- **Summary charts** of certificate status
- Highlight **critical certificates (<7 days expiry)**
- Responsive and modern UI with centered login

---

## 🛠️ Tech Stack
- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

## 📂 Project Structure
📦 AI-Driven-Certificate-Tracker
┣ 📜 app.py # Main Streamlit app
┣ 📜 cert_checker.py # Script for checking certificates
┣ 📜 requirements.txt # Python dependencies
┣ 📜 README.md # Documentation
┗ 📂 sample_data # Example CSV logs

📊 Example CSV Format

  Certificate, Status, Expiry_Days
    cert1.example.com, OK, 45
    cert2.example.com, Warning, 12
    cert3.example.com, Critical, 3

---

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-driven-certificate-tracker.git
   cd ai-driven-certificate-tracker

## ⚡ Usage:

1. Run this command on terminal first:
   python cert_checker.py

2. Run this command secondly: 
   python -m streamlit run app.py

   
