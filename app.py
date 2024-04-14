import requests
import streamlit as st
from streamlit_lottie import st_lottie
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
with st.container():
    st.subheader("Hi, I am Rodrigo :wave:")
    st.title("A Systems Engineer From Portugal!")
    st.write(
        "I am passionate about technology and exploring new ways of applying my knowledge to real life problems and business settings."
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

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("In this section, you can check small projects/exercises that I do from time to time in order to upgrade my skills or trying some take on solutions for problems that I thought of. In this spirit I will sometimes provide the context of the so called project/exercise with some notes if needed and usually followed by some reference (github link or other).")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rodrigo.rocha582@gmail.COM" method="POST">
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

with st.container():
    st.write("---")
    st.header("About this webpage")
    st.write("##")
    st.write("""
            If you like this page I'm obliged to say, that I hate pretty much every aspect of front-end development and I can say quite confidently that I am prety awful in it too.
            I was looking for a fast solution for making a fast presentation webpage and I stumbled upon Sven's youtube channel and I also forked the repo that he made available.
            Let it be known that I intend to iterate upon this webpage and it will distantiate itself from Sven's solution in time.
            Being this said, I will leave the links for his youtube channel and the repository that gave origin to this webpage. 
            """)
    st.write("[Sven's YouTube Channel](https://youtube.com/c/CodingIsFun)")
    st.write("[Sven's Streamlit Repo](https://github.com/Sven-Bo/personal-website-streamlit)")
