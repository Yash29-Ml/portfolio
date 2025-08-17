import streamlit as st
from PIL import Image

def home():
    st.title("👋 Hi, I'm Yash Shinde")
    st.subheader("Machine Learning Enthusiast | Streamlit Developer | Python Certified")

    # --- Layout with Columns ---
    col1, col2 = st.columns([1, 3])

    with col1:
        profile_img = Image.open("WhatsApp Image 2025-08-17 at 21.57.36_8c21d9d0.jpg")  # Replace with your actual image filename
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



def main():
    # --- Page Config ---
    st.set_page_config(page_title="Yash Shinde | ML Portfolio", page_icon="🧠", layout="wide")

    # --- Sidebar ---
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Certifications", "Achievements", "Contact"])

    # --- Page Routing ---
    if page == "Home":
        home()

    elif page == "Projects":
        st.header("📊 My Projects")

        st.subheader("1. Student Marks Predictor")
        st.markdown("""
        Predicts student final grades (G3) and pass/fail status using SVR and SVC.  
        - Dataset: UCI Student Performance  
        - Models: SVR, SVC  
        - Tech: Python, scikit-learn, Streamlit  
        [🔗 Live App](https://student-marks-predictor-mfzpe3rffzdikb5shaewxg.streamlit.app/)  
        [📁 GitHub Repo](https://github.com/Yash29-Ml/Student-Marks-Predictor)
        """)

        st.subheader("2. Car Price Prediction")
        st.markdown("""
        Predicts resale value of cars based on user inputs.  
        - Features: Brand, Year, Mileage, Fuel Type  
        - Model: Regression  
        [🔗 Live App](https://carsprediction-5awdp3kpapplfktkbzsukz.streamlit.app/)
        """)

        st.subheader("3. CVD Risk Predictor")
        st.markdown("""
        Estimates 10-year cardiovascular disease risk using logistic regression.  
        - Dataset: Framingham Heart Study  
        [📁 GitHub Repo](https://github.com/Yash29-Ml/CVD-Predictor)
        """)

    elif page == "Certifications":
        st.header("📜 Certifications")

        st.subheader("Python (Basic) – HackerRank")
        st.markdown("""
        - Earned: 05 Sep, 2024  
        - Credential ID: 250C85093395  
        - Validated by: Harishankaran K, CTO of HackerRank  
        [🔗 View Certificate](https://www.hackerrank.com/certificates)
        """)
        # Uncomment if you have the image
        # cert_img = Image.open("python_basic_certificate.jpg")
        # st.image(cert_img, caption="Python (Basic) Certificate", width=400)

    elif page == "Achievements":
        st.header("🏆 Achievements")

        st.subheader("3rd Rank – Data Insights 2024–25")
        st.markdown("""
        - Event: Coding Competition  
        - Organized by: Department of Data Science, YCIS Satara  
        - Recognized by: Dr. S.K. Shinde & Dr. B.T. Jadhav  
        """)
        trophy_img = Image.open("WhatsApp Image 2025-08-17 at 21.56.37_4066e8ac.jpg")
        st.image(trophy_img, caption="Proud Moment!", width=350)

    elif page == "Contact":
        st.header("📬 Contact Me")

        st.markdown("""
        - 📧 Email: yashshinde292005@gmail.com  
        - 💼 LinkedIn: [Yash Shinde](https://www.linkedin.com/in/yash-shinde-a0731037a)  
        - 🧑‍💻 GitHub: [Yash29-Ml](https://github.com/Yash29-Ml)
        """)

 

# --- Run the app ---
if __name__ == "__main__":
    main()