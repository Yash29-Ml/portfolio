import streamlit as st
from PIL import Image

# --- Home Section ---
def home():
    st.title("👋 Hi, I'm Yash Shinde")
    st.subheader("Machine Learning Enthusiast | Streamlit Developer | Python Certified")

    col1, col2 = st.columns([1, 3])
    with col1:
        profile_img = Image.open("WhatsApp Image 2025-08-17 at 21.57.36_8c21d9d0.jpg")
        st.image(profile_img, caption="Yash Shinde", width=200)
    with col2:
        st.markdown("""
        I'm a self-driven data science enthusiast who thrives on turning raw data into meaningful insights and intuitive tools.  
        My journey blends strong technical foundations with a passion for user-friendly design and real-world impact.

        🔍 **What I Do**:
        - Clean and preprocess datasets to extract actionable features  
        - Build and evaluate machine learning models for both prediction and classification  
        - Design interactive Streamlit apps that make complex models accessible to users  
        - Modularize code for clarity, scalability, and reproducibility  
        - Explore data deeply to uncover patterns, trends, and opportunities

        🧠 **My Approach**:
        I believe in learning by doing—whether it's deploying a model, debugging a pipeline, or refining a user interface.  
        I combine mathematical intuition with practical experimentation, always aiming to understand not just how things work, but why.

        🎯 **My Goal**:
        To contribute to impactful data-driven solutions, collaborate with forward-thinking teams, and grow into a well-rounded ML engineer.  
        I'm currently building my portfolio, refining my skills, and actively seeking internship opportunities to apply what I've learned in a professional setting.
        """)

# --- Projects Section ---
def projects():
    st.header("📊 My Projects")

    st.subheader("1. Student Marks Predictor")
    st.markdown("""
    Predicts final grades and pass/fail status using SVR and SVC.  
    - Dataset: UCI Student Performance  
    - Models: SVR (regression), SVC (classification)  
    [🔗 Live App](https://student-marks-predictor-mfzpe3rffzdikb5shaewxg.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/Student-Marks-Predictor)
    """)

    st.subheader("2. Car Price Prediction")
    st.markdown("""
    Predicts resale value of cars based on user inputs.  
    - Features: Brand, Year, Mileage, Fuel Type  
    - Model: Linear Regression  
    [🔗 Live App](https://carsprediction-5awdp3kpapplfktkbzsukz.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/Car-Price-Prediction)
    """)

    st.subheader("3. CVD Risk Predictor")
    st.markdown("""
    Estimates 10-year cardiovascular disease risk using logistic regression.  
    - Dataset: Framingham Heart Study  
    [🔗 Live App](https://health-split-g3cgjzzvfzvw8sykljgcpo.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/CVD-Predictor)
    """)

    st.subheader("4. Wine Quality Classifier")
    st.markdown("""
    Classifies wine quality based on physicochemical properties.  
    - Dataset: UCI Wine Quality  
    - Models: Random Forest, Logistic Regression  
    [🔗 Live App](https://wine-quality-app-wizx5yc6dtgzvwdtg3dtlj.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/Wine-Quality-App)
    """)

    st.subheader("5. Insurance Risk Analyzer")
    st.markdown("""
    Dual-mode app for predicting insurance charges and classifying risk level.  
    - Dataset: Medical Cost Personal Dataset  
    - Models: Linear Regression, Logistic Regression  
    [🔗 Live App](https://shf9fthadcwgevgzyw8hat.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/Health-Split-ML)
    """)

    st.subheader("6. Golf Play Predictor")
    st.markdown("""
    Predicts golf scores and classifies performance tiers.  
    - Dataset: Custom golf performance data  
    - Models: Regression & Classification  
    [🔗 Live App](https://golf-play-predictor-d6nncnjp6wwf8t4prcexs7.streamlit.app/)  
    [📁 GitHub Repo](https://github.com/Yash29-Ml/Golf-play-predictor)
    """)

# --- Certifications Section ---
def certifications():
    st.header("📜 Certifications")

    st.subheader("Python (Basic) – HackerRank")
    st.markdown("""
    - 🗓️ Earned: 05 Sep, 2024  
    - 🆔 Credential ID: 250C85093395  
    - ✅ Validated by: Harishankaran K, CTO of HackerRank  
    - 📚 Topics Covered: Scalar Types, Operators and Control Flow, Strings, Collections and Iteration, Modularity, Objects and Types, Classes  
    [🔗 View Verified Certificate](https://www.hackerrank.com/certificates/250c85093395)
    """)
    # Uncomment if you have the image
    # cert_img = Image.open("python_basic_certificate.jpg")
    # st.image(cert_img, caption="Python (Basic) Certificate", width=400)

# --- Achievements Section ---
def achievements():
    st.header("🏆 Achievements")

    st.subheader("3rd Rank – Data Insights 2024–25")
    st.markdown("""
    - Event: Coding Competition  
    - Organized by: Department of Data Science, YCIS Satara  
    - Recognized by: Dr. S.K. Shinde & Dr. B.T. Jadhav  
    """)
    trophy_img = Image.open("WhatsApp Image 2025-08-17 at 21.56.37_4066e8ac.jpg")
    st.image(trophy_img, caption="Proud Moment!", width=350)

# --- Contact Section ---
def contact():
    st.header("📬 Contact Me")

    st.markdown("""
    - 📧 Email: yashshinde292005@gmail.com  
    - 💼 LinkedIn: [Yash Shinde](https://www.linkedin.com/in/yash-shinde-a0731037a)  
    - 🧑‍💻 GitHub: [Yash29-Ml](https://github.com/Yash29-Ml)
    """)

# --- Main App ---
def main():
    st.set_page_config(page_title="Yash Shinde | ML Portfolio", page_icon="🧠", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Certifications", "Achievements", "Contact"])

    if page == "Home":
        home()
    elif page == "Projects":
        projects()
    elif page == "Certifications":
        certifications()
    elif page == "Achievements":
        achievements()
    elif page == "Contact":
        contact()

if __name__ == "__main__":
    main()
