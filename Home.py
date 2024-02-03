import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best company")
content="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ultrices ornare sem, a porttitor nisi tempor in. Curabitur eu volutpat est. 
Suspendisse eget urna eu mauris sollicitudin vehicula. Donec accumsan nunc eu dui lobortis, gravida interdum justo vulputate. Vivamus dignissim egestas semper. Nulla quis finibus libero. Integer tincidunt volutpat eros, id pretium purus consectetur vitae. Donec lacinia mi ut enim euismod posuere. Etiam et finibus dui, et fringilla ligula. Curabitur commodo ac orci id finibus. Nunc mi justo, luctus ac hendrerit nec, malesuada ut erat. Sed eget semper nisi, sit amet sollicitudin ligula. Ut magna orci, sodales et risus quis, venenatis feugiat dolor. Nunc ac commodo augue, rutrum tempus justo.
"""
st.write(content)

st.header("Our team")

col1,col2,col3=st.columns(3)
df=pandas.read_csv("data.csv")

with col1:
    for index,data in df[:4].iterrows():
        first_name=data["first name"]
        last_name=data["last name"]
        st.subheader(first_name.capitalize()+" "+last_name.capitalize())
        st.write(data["role"])
        st.image("images/"+data["image"])
with col2:
    for index,data in df[4:8].iterrows():
        first_name=data["first name"]
        last_name=data["last name"]
        st.subheader(first_name.capitalize()+" "+last_name.capitalize())
        st.write(data["role"])
        st.image("images/" + data["image"])
with col3:
    for index,data in df[8:].iterrows():
        first_name=data["first name"]
        last_name=data["last name"]
        st.subheader(first_name.capitalize()+" "+last_name.capitalize())
        st.write(data["role"])
        st.image("images/" + data["image"])