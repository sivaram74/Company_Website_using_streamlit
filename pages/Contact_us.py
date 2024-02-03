import streamlit as st
from send_email import send_mail
st.header("Contact Us")
import pandas as pd

df=pd.read_csv('topics.csv')

with st.form(key="Form"):
    user=st.text_input("your email address")
    option= st.selectbox(
        'What topic do you want to discuss?',
        (df["topic"])
    )
    raw_message = st.text_area("text")
    button= st.form_submit_button("Click here")
    message=f"""\
Subject: New mail from {user}

From: {user}
{raw_message}. The user wants to discuss {option} with you.
    """
    if button:
        send_mail(message)
        st.info("your email has been sent successfully")

