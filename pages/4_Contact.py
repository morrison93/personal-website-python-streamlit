import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.title("Contact me!")

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
            If you like this webpage I'm obliged to say, that I hate pretty much every aspect of front-end development and I can say quite confidently that I am prety awful in it too.
            I was looking for a fast solution for making a fast presentation webpage and I stumbled upon Sven's youtube channel and I also forked the repo that he made available.
            Let it be known that I intend to iterate upon this webpage and it will distantiate itself from Sven's solution in time.
            Being this said, I will leave the links for his youtube channel and the repository that gave origin to this webpage. 
            """)
    st.write("[Sven's YouTube Channel](https://youtube.com/c/CodingIsFun)")
    st.write("[Sven's Streamlit Repo](https://github.com/Sven-Bo/personal-website-streamlit)")