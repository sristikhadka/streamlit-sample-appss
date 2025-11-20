import streamlit as st


st.title("My Dashboard")
st.header("Overview")
st.subheader("This is subtitle 1")
st.text("My sample text")
st.subheader("This is my subheader2")
st.markdown("**markdown**|Italic")
txt = st.text_input("Enter a text:")

txt = st.text_area("Enter your feedback")

if txt:
    st.write(f"Hello {txt}.How are you?")

user_num = st.number_input("Enter the number,limit = 5,min = 3 ,max = 98")