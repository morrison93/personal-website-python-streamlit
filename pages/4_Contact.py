import streamlit as st 
from constants import *

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
language=st.radio("",("English","French"))

# ---- Language Settings ----
if language == "English":
    header=header_contact_en
if language == "French":
    header=header_contact_fr

st.header(header[0], divider="blue")

# ---- CONTACT ----
with st.container():
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rodrigo.rocha582@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


st.header(header[1],divider='blue')

st.markdown(f"##### 📞 Phone: {phone}")   
st.markdown(f"##### ✉️ Email: {email}")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(linkedin_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"#####  Linkedin: {linkedin_link}")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(github_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"#####  Github: {github_link}")