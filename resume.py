import streamlit as st
import pdfplumber

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

import matplotlib.pyplot as plt
st.markdown(
    """
        <style>
    .stApp {
    background-image: url("https://mir-s3-cdn-cf.behance.net/project_modules/1400/c207d098033077.5ed3061499944.png");
    background-size: cover;
    background-position: center;
    background-repeat: no repeat;
    background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("🤖 AI Resume Analyzer")
st.write("Analyze your resume, compare it with a job description, and improve your chances of getting shortlisted.")

st.text_input("Enter your name")
stream=st.selectbox("select your stream",
            ["Computer Science",
            "Information Technology (IT)",
            "Data Science",
            "Artificial Intelligence & Machine Learning",
            "Cyber Security",
            "Electronics & Communication",
            "Electrical Engineering",
            "Mechanical Engineering",
            "Civil Engineering",
            "Business Administration (BBA)",
            "Commerce",
            ]
    )
if st.button("submit"):
        st.success("✅ Stream added succesfully")


st.subheader("📄 Upload resume")    
uploaded_file=st.file_uploader(
        "upload your resume file",
        type=["pdf"]
    )
resume_text = ""

job_description=st.subheader("Enter a job descrpition")
job=st.text_area("📄 Paste the Job Description",
        placeholder="Paste the complete job description here...",
    )
if st.button("🔍 Analyze Resume"):
    if uploaded_file is None:
        st.error("❌ Please upload your Resume")

    elif job .strip()=="":
        st.error("❌ Please upload job Description")

    else:
        resume_text = ""

        with pdfplumber.open(uploaded_file)as pdf:
            for  page in pdf.pages:
                text=page.extract_text()

                if text:
                    resume_text += text + "\n"    

        st.success("✅ Resume Uploaded Successfully!")

        st.subheader("📑 Extracted Resume Text")
        st.write(resume_text)

        if resume_text.strip()=="":
            st.error("Resume text could not bee extracted")
        elif job.strip()=="":
            st.error("Please enter a job descriotion")
        else:
            v=TfidfVectorizer ()
            ve=v.fit_transform([resume_text,job])
            simplify=cosine_similarity(ve[0],ve[1])
            score=simplify[0][0]*100
            st.subheader("Resume match score")
            st.progress(int(score))
            st.success(f"{score:2f}% Match")

    skills=[    "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "Git",
        "GitHub",
        "Statistics",
        "Streamlit",
        "OpenCV",
        "Power BI",
        "Excel"
    ]

    match=[]
    for skill in skills:
        if skill.lower()in resume_text.lower()and skill.lower()in job.lower():
            match.append(skill)

    st.success("MATCHED SKILLS")
    for skill in match:
        st.write("✔",skill)

    missing=[]
    for skill in skills:
        if skill.lower()in job.lower()and skill.lower()not in resume_text.lower():
            missing.append(skill)

    st.subheader("❌ Missing Skills")
    for skill in missing:
        st.write("✖",skill)

    matcount=len(match)
    miscount=len(missing)

    lable=["Matched skills","Missing skills"]
    sizes=[matcount,miscount]

    fig,ax=plt.subplots()

    ax.pie(
        sizes,
        labels=lable,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")
    st.subheader("Skill Distribution")
    st.pyplot(fig)
