import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input")

## creating a slider
age=st.slider("Select your age:",0,100,20)
st.write(f"Your age is: {age}")

## select box
options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose ypur favorite language:", options)
st.write(f"You selected {choice}.")

## Dataframe
data = {
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["NewYolk","LosAngeles","Chicago","Houston"]
}
df = pd.DataFrame(data)
st.write(df)

## Uploading a file
uploaded_files=st.file_uploader("Choose a CSV file", type="csv")

if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)


name=st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}")