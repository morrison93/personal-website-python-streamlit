import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

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
if language == "French":
    st.session_state['language']="French"
    st.session_state['index']=1



st.header("Resume",divider='blue')