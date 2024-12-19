import streamlit as st
import pandas as pd
from os import path
import numpy as np
data=pd.read_csv(path.join("auto-mpg.csv"))
st.title("Welcome to my streamlit website")
st.write("Hellow")
df=pd.DataFrame({"first col":[1,2,3,4],"second col":[10,20,30,40] })
st.write(df)
st.write(df["first col"])
st.write(data)
st.write(data["mpg"])
#map_data=pd.DataFrame(
 #   np.array([["8.55709","76.8819745"]]),columns=["lat","lon"])
#st.map(map_data)
x=st.slider("x",min_value=10,max_value=200)
st.title("{} squared is {}".format(x,x*x))
