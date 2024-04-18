import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from constants import *

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- Language Settings ----

if 'language' not in st.session_state:
    st.session_state['language']="English"
    st.session_state['index']=0
if 'language' in st.session_state:
    language=st.session_state['language']
    index_lang=st.session_state['index']

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;margin-top:-90px;} </style>', unsafe_allow_html=True)
language=st.radio("",("English","French"),index=index_lang)

if language == "English":
    st.session_state['language']="English"
    st.session_state['index']=0
    info=info_en
    label_str="Download my :blue[resume]"
    file_name="CV_SYS_EN_RodrigoRocha_2024.pdf"
    file_path="attachments/CV_SYS_EN_RodrigoRocha_2024.pdf"
    thesis_file_name="Dissertation_METI_Rodrigo_Rocha.pdf"
    thesis_file_path="attachments/Dissertation_METI_Rodrigo_Rocha.pdf"
    education=Education_Resume_EN
    header=headers_resume_en
    experience=Experience_Resume_EN
if language == "French":
    st.session_state['language']="French"
    st.session_state['index']=1
    info=info_fr
    label_str="Télecharger mon :blue[CV]"
    file_name="CV_SYS_FR_RodrigoRocha_2024.pdf"
    file_path="attachments/CV_SYS_FR_RodrigoRocha_2024.pdf"
    thesis_file_name="Dissertation_METI_Rodrigo_Rocha.pdf"
    thesis_file_path="attachments/Dissertation_METI_Rodrigo_Rocha.pdf"
    education=Education_Resume_FR
    header=headers_resume_fr
    experience=Experience_Resume_FR

# ---- Resume ----

st.header("Resume",divider='blue')

with st.container():
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("attachments/rodrigo.png", width=325)

    with col2:
        st.title(info["name"])
        st.write(info["description"])

        with open(file_path, "rb") as file:
            pdf_file = file.read()

        st.download_button(
            label=label_str,
            data=pdf_file,
            file_name=file_name,
            mime="application/pdf")
        
        st.write("📫", "rodrigo.rocha582@gmail.com")
        st.write("#")

        with st.container():
            col1, col2 = st.columns([0.1, 3])
            with col1:
                st.write(linkedin_logo, unsafe_allow_html=True)
                st.write(github_logo, unsafe_allow_html=True)
            with col2:
                st.markdown(f"######  Linkedin: {linkedin_link}")
                st.markdown(f"######  Github: {github_link}")

st.markdown("""---""")

st.write('\n')
st.subheader(header[0])
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader(header[1])
st.write(
    """
- Programming: Scripting - Python Shell and Powershell, Java, Matlab, C. 
- Databases: Postgres, MySQL
- Tools: Docker, Kubernetes, Postman, Amazon S3, Azure DevOps, Git, Github, Gitlab CI, Grafana, Control M, Apache, Nagios
- Methodologies: Agile - SCRUM
- Operating Systems: Linux, Windows
- Network: TCP/IP stack
- Requirements & Planning: ServiceNow, Atlassian JIRA and Confluence
"""
)

# --- Languages ---
st.write('\n')
st.subheader(header[2])
st.write(
    """
- Portuguese - native
- English - C2
- French - C1
- Spanish - C1
""")

st.markdown("""---""")

# --- WORK HISTORY ---
st.subheader(header[3])

# --- JOB 1
st.write(experience[0][0])
st.write(experience[0][1])
st.write(experience[0][2])

# --- JOB 2
st.write('\n')
st.write(experience[1][0])
st.write(experience[1][1])
st.write(experience[1][2])

# --- JOB 3
st.write('\n')
st.write(experience[2][0])
st.write(experience[2][1])
st.write(experience[2][2])

# --- JOB 4
st.write('\n')
st.write(experience[3][0])
st.write(experience[3][1])
st.write(experience[3][2])

# --- Education ---
st.markdown("""---""")
st.write('\n')
st.subheader(header[4])

st.write('\n')
st.write(education[1])
st.write(education[0])

# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")

