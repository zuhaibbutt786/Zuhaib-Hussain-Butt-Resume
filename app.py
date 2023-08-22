from pathlib import Path

import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "zuhaib_cv.pdf"
profile_pic = current_dir / "assets" / "zuhaib.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zuhaib Hussain Butt"
PAGE_ICON = ":wave:"
NAME = "Zuhaib Hussain Butt"
DESCRIPTION = """
Data Analyst,Machine Learning Engineer assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "Zuhaibbutt3@gmail.com"
SOCIAL_MEDIA = {
    "📉 Kaggle": "https://www.kaggle.com/zuhaibbutt",
    "💻 LinkedIn": "https://www.linkedin.com/in/zuhaib-hussain-butt-6628141a4/",
    "📊 GitHub": "https://github.com/zuhaibbutt786",
    "😎 Facebook": "https://www.facebook.com/zuhaib.butt.50/",
    "📞 Whatsapp": "https://wa.link/nt3x5e",
}
PROJECTS = {
    "🏆 Covid case study using folium": "https://www.kaggle.com/code/zuhaibbutt/covid-casestudy-using-folium",
    "🏆 Roman Urdu predition using machine learning models": "https://www.kaggle.com/code/zuhaibbutt/roman-urdu-prediction-with-test-value",
    "🏆 Dashboard on Tableau ":"https://public.tableau.com/app/profile/zuhaib3028/viz/lab12_16630698501100/Story1",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualification")
st.write(
    """
- ✔️ 2 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python,R, Matlab and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, foilum , numpy , pyspark), SQL, R, Matlab
- 📊 Data Visulization: PowerBi, MS Excel, Plotly , weka 3.0
- 📚 Modeling: supervised and unsupervised learning models
- 🗄️ Databases: MySQL
"""
)



# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- Edu 1
st.write("📚", "**University of Engineering & Technology Lahore | MS Computer Science**")
st.write("08/2022 -present ")
st.write(
    """
- ► Major Computer Science with minor Data science Courses
- ► 4+ paper submitted in IEEE
- ► Data Science Domain
"""
)

# --- Edu 2
st.write('\n')
st.write("📚", "**GIFT University Gujranwala | BS Software Engineering**")
st.write("08/2017 - 08/2021")
st.write(
    """
- ► Major Software Engineering With elective subjects of Machine learning and AI 
- ► Final year project based on IOT
- ► Member of YCPS,SSG,GSID and GGT
- ► Elected to Vice president for young computer professional society 2020 to 2021
"""
)

# --- Edu 3
st.write('\n')
st.write("📚", "**University of Dundee - Scotland, United Kingdom | Exchange Program: Web Development**")
st.write("10/2020 - 11/2020")


# --- Edu 4
st.write('\n')
st.write("📚", "**St Petersburg State Transport University, Russia | Exchange Program: Language & Multicultural Exchange**")
st.write("11/2020 - 12/2020")



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | get-solutions.site**")
st.write("08/2021 -12/2021 ")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | ATC, Gujranwala**")
st.write("12/2021 - 03/2022")
st.write(
    """
- ► Produced monthly reports using advanced Excel spreadsheet functions.
- ► Created various Excel documents to assist with pulling metrics data and presenting  information to stakeholders for concise explanations of best placement for needed resources.
- ► Utilized data visualization tools to effectively communicate business insights.
- ► Extracted and interpreted data patterns to translate findings into actionable outcomes.
- ► Tested data prediction algorithms based on historical data.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Science Lab Instructor | GIFT University**")
st.write("01/2022 - present")
st.write(
    """
- ► Worked with program director to develop and implement successful lesson plans.
- ► Applied advanced education to help students struggling with material and techniques.
- ► Facilitated student participation by delivering fun, engaging lessons.
- ► Designed and implemented course curriculum that reflected relevance of Data science to everyday world.
- ► Teach Labs of Data science courses.

"""
)





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

    
    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)    
