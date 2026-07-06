import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
    background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230707/pngtree-d-illustration-of-red-heart-and-heartbeat-waves-against-white-background-image_3815370.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no repeat;
    background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("❤️ Heart Disease Prediction System")
st.write("THIS IS A HEART DISEASE PREDICTION SYSTEM. IT PREDICTS WHETHER A PERSON HAS HEART DISEASE OR NOT BASED ON THE INPUT PARAMETERS.")
st.write("Please enter the following parameters to predict whether a person has heart disease or not.")

name=st.text_input("Enter your name:")

age=st.number_input("AGE", min_value=1, max_value=100)

gender=st.selectbox("GENDER", ["Male", "Female", "Other"])

cp=st.selectbox("CHEST PAIN TYPE", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
st.image("https://tse1.explicit.bing.net/th/id/OIP.F_3mSVL4M7E-59uth6vcxQHaF7?cb=thfc1falcon4&rs=1&pid=ImgDetMain&o=7&rm=3",width=300)

trestbps=st.number_input("RESTING BLOOD PRESSURE", min_value=80, max_value=200)
st.image("https://c8.alamy.com/comp/2WHF9Y1/blood-pressure-chart-illustration-2WHF9Y1.jpg",width=300)

chol=st.number_input("SERUM CHOLESTEROL IN MG/DL", min_value=100, max_value=600)
st.image("https://thumbs.dreamstime.com/z/types-cholesterol-educational-cycle-scheme-fatty-food-to-ldl-artery-labeled-symbolic-diagram-explanation-how-192093070.jpg",width=300)

fbs=st.selectbox("FASTING BLOOD SUGAR > 120 MG/DL", [True, False])

heart=st.number_input("HEART RATE", min_value=50, max_value=200)
st.image("https://as1.ftcdn.net/v2/jpg/05/59/06/16/1000_F_559061642_EI2mq5GUGIle2SrV9uDyEcYNtQTz0X8H.jpg",width=300)

exang=st.selectbox("EXERCISE INDUCED ANGINA", [True, False])

st.sidebar.title("❤️ About")

st.sidebar.write("THIS IS A HEART DISEASE PREDICTION SYSTEM. IT PREDICTS WHETHER A PERSON HAS HEART DISEASE OR NOT BASED ON THE INPUT PARAMETERS.")

st.sidebar.header("Risk levels:")

st.sidebar.success("0-30% = Low Risk")

st.sidebar.warning("30-60% = Medium Risk")

st.sidebar.error("60%+ = High Risk")

risk=st.sidebar.radio("Enter a risk level to see the corresponding message:", ["low risk ", "medium risk", "high risk"])

if st.sidebar.button("submit"):
    if risk=="low risk":
        st.sidebar.success("You are at low risk of heart disease . keep up the good work and maintain a  healthy lifestyle.")
    elif risk=="medium risk":
        st.sidebar.warning("You are at medium risk of heart disease . please consult a doctor and take necessary precautions.")
    else :
        st.sidebar.error("You are at high risk of heart disease . please consult a doctor immediately.")
st.sidebar.subheader("Thank you for using our system.we hope you found it helpful ❤️")

if st.button("❤️ Predict Heart Disease Risk"):

    if age<= 20:
        st.success(" ✅ Heart disease risk is very low due to young age.")
    else:
        st.warning("⚠️ Further medical parameters are required for prediction.")

    if cp == "Asymptomatic":
        st.warning("⚠️ Higher risk indicator detected.")
    elif cp == "Typical Angina":
        st.info("ℹ️ Chest pain may be related to heart disease.")
    else:
        st.success("✅ Lower risk indicator.")

    if trestbps < 120:
        st.success("✅ Normal Blood Pressure")
    elif trestbps >= 120 and trestbps < 140:
        st.warning("⚠️ Elevated Blood Pressure")
    else:
        st.error("❌ High Blood Pressure - Increased Risk Factor")

    if chol < 200:
        st.success("✅ Normal Cholesterol Level")
    elif 200 <= chol <= 239:
        st.warning("⚠️ Borderline High Cholesterol")
    else:
        st.error("❌ High Cholesterol - Increased Risk Factor")

    if fbs:
        st.warning("⚠️ Fasting blood sugar is above 120 mg/dL.")
    else:
        st.success("✅ Fasting blood sugar is within normal range.")

    if heart < 60:
        st.warning("⚠️ Low Heart Rate (Bradycardia)")
    elif 60 <= heart <= 100:
        st.success("✅ Normal Heart Rate")
    else:
     st.error("❌ High Heart Rate (Tachycardia)")

    if exang:
        st.warning("⚠️ Exercise-induced angina present.")
    else:
        st.success("✅ No exercise-induced angina.")

st.header("Thanks for visiting Heart Disease Prediction System hope you like it and take care of yourself stay healty ❤️❤️")
