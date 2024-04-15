import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from constants import *


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

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

# ---- ---- Language Button ---- -----
# Waiting for emojis support to replace the buttons
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
language=st.radio("",("English","French"),index=index_lang)

if language not in st.session_state:
    st.session_state['language']="English"
    st.session_state['index']=0

if language == "English":
    info=info_en
    header=header_home_en
    file_name="CV_SYS_EN_RodrigoRocha_2024.pdf"
    file_path="attachments/CV_SYS_EN_RodrigoRocha_2024.pdf"
    st.session_state['language']="English"
    st.session_state['index']=0
if language == "French":
    info=info_fr
    header=header_home_fr
    file_name="CV_SYS_FR_RodrigoRocha_2024.pdf"
    file_path="attachments/CV_SYS_FR_RodrigoRocha_2024.pdf"
    st.session_state['language']="French"
    st.session_state['index']=1

# ---- HEADER SECTION ----
st.header(header[0],divider='blue')

col1, col2, col3 = st.columns([2 ,0.2, 1])


with col1:
    if language == "English":
        st.write(info['brief'])
        st.markdown(f"###### 😄 Name: {info['name']}")
        st.markdown(f"###### 👉 Study: {info['study']}")
        st.markdown(f"###### 📍 Location: {info['location']}")
        st.markdown(f"###### 📚 Interests: {info['interest']}")
        st.markdown(f"###### 👀 Linkedin: {linkedin_link}")
    if language == "French":
        st.write(info['brief'])
        st.markdown(f"###### 😄 Nom: {info['name']}")
        st.markdown(f"###### 👉 École: {info['study']}")
        st.markdown(f"###### 📍 Basée sur: {info['location']}")
        st.markdown(f"###### 📚 Intérêts: {info['interest']}")
        st.markdown(f"###### 👀 Linkedin: {linkedin_link}")
    
    with open(file_path, "rb") as file:
        pdf_file = file.read()

    st.download_button(
        label="Download my :blue[resume]",
        data=pdf_file,
        file_name=file_name,
        mime="application/pdf")

with col3:
    st.image("attachments/rodrigo.png", width=300)


# skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.header(header[1],divider='blue')

def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()


# ---- WHAT I DO ----
st.header(header[2],divider='blue')

with st.container():
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(info['WAI'])
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
