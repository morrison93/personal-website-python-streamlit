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

st.title("Projects Page")

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