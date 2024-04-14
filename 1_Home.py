import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image


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

# ---- HEADER SECTION ----
st.header("About Me",divider='blue')

with st.container():
    st.write(
        """
        I am passionate about technology and exploring new ways of applying my knowledge to real life problems and business settings.
        """
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who Am I?")
        st.write("##")
        st.write(
            """
            I'm a Telecommunication and Informatics Engineer graduated in Lisbon, Portugal in 2019 specializing in service management, network and security. I'm currently living in Toulouse, France since 2021 and this webpage is mainly too:
            - Leverage my technical skills by building small projects and trying to exercise some skills that I haven't acquired or I'm still in the process of acquiring.
            - Present myself to the world through this small project.
            - Keep a track of my career by hopefully keeping this webpage up to date.
            - Make connections throughout the world regarding projects or some other interesting topic.

            If this sounds interesting to you, please consider to contact me though the "Get In Touch With Me!" section.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("About this webpage")
    st.write("##")
    st.write("""
            If you like this webpage I'm obliged to say, that I hate pretty much every aspect of front-end development and I can say quite confidently that I am prety awful in it too.
            I was looking for a fast solution for making a fast presentation webpage and I stumbled upon Sven's youtube channel and I also forked the repo that he made available.
            Let it be known that I intend to iterate upon this webpage and it will distantiate itself from Sven's solution in time.
            Being this said, I will leave the links for his youtube channel and the repository that gave origin to this webpage. 
            """)
    st.write("[Sven's YouTube Channel](https://youtube.com/c/CodingIsFun)")
    st.write("[Sven's Streamlit Repo](https://github.com/Sven-Bo/personal-website-streamlit)")
