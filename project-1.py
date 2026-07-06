import streamlit as st

st.markdown(
    """
    <style>
    .stApp{
        background-image:
        url("https://wallpapercave.com/wp/wp3006091.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    */Title color */
    h1{
        color: white;
    }
    */ Main text color */
    h2,h3,title {
        color: white;
    }
    /* st.write() aur normal text */
    p{
        color: white;
    }
    */ sidebar background color */
    [data-testid=stsidebar]{
        background-image:
        url("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/dark-pink-background-template-design-04eeaaaf9ea63502ddd92ad5e20f8f3e_screen.jpg?ts=1561436711");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    */ sidebar text color */
    [data-testid=stsidebar] {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("AI-Powered Fraud Detection System")
st.write("welcome to the AI-Powered Fraud Detection System! This application uses machine learning algorithms to detect fraudulent transactions in real-time.")

st.image("https://tse4.mm.bing.net/th/id/OIP.JaaWz2FLA-eHDRHL7m8fEQHaD4?cb=thfc1falcon4&rs=1&pid=ImgDetMain&o=7&rm=3",width=700)

signin, signup = st.columns(2)
signin, signup = st.tabs(["🔐 sign in","✍️ sign up"])

with signin:
    username = st.text_input(
        "username", 
        placeholder="enter your username",
        key="signin_username"
        )
    password = st.text_input(
        "password", 
        placeholder="enter your password",
          type="password",
          key="signin_password"
        )
    st.write("forgot your password? [click here](https://www.goggle.com) to reset the password.")
    if st.button("sign in"):
        st.success("sign in successful! welcome back.")


with signup:
    st.subheader("create a new account")
    username = st.text_input(
        "username",
          placeholder="enter your username",
          key="signup_username"
          )
    email = st.text_input(
        "email", 
        placeholder="enter your email",
        key="signup_email"
        )
    password = st.text_input(
        "password", 
        placeholder="enter your password",
          type="password"
          )
    if st.button("sign up"):
        st.success("you have successfully signed up for the AI-powered fraud detection system.")

st.sidebar.title("AI-Powered Fraud Detection System")
page=st.sidebar.radio("select a page", ["home", "about", "contact"])
mode=st.sidebar.selectbox("select a model", ["logistic regression","decision tree", "random forest", "support vector machine","other"])
st.sidebar.write("you have selected the ",mode,"model for fraud detection.")
