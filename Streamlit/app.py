import streamlit as st
import pandas as pd
import plotly.express as px 
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.offline as py
import plotly.tools as tls
from plotly.subplots import make_subplots
import io
pd.options.mode.chained_assignment = None

### Config
st.set_page_config(
    page_title="Getaround",
    layout="wide"
)

### Import dataset
@st.cache(allow_output_mutation=True)
def load_data():
  df = pd.read_excel("get_around_delay_analysis.xlsx")
  return df

df = load_data()


### App
st.title("*GetAround*")
st.markdown("Hello there! Welcome to this Getaround app. GetAround is the Airbnb for cars. You can rent cars from any person for a few hours to a few days! Founded in 2009, this company has known rapid growth. In 2019, they count over 5 million users and about 20K available cars worldwide.")
st.markdown("Check out our data here ⬇️")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df) 

### Some cleaning
df["delay"]=df["delay_at_checkout_in_minutes"].apply(lambda x : "After time/Late" if x>0 else "In advance/On time")

col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("Checkin types proportion")
        fig = px.pie(df,names="checkin_type")
        st.plotly_chart(fig, use_container_width=True)
    
with col2:
        st.subheader("Status of rental proportion")
        fig = px.pie(df,names="state")
        st.plotly_chart(fig, use_container_width=True)
        

with col3:        
        st.subheader("Delays proportion")
        fig = px.pie(df, names="delay")
        st.plotly_chart(fig , use_container_width=True)
        

col1, col2 = st.columns(2)
with col1:
        st.subheader("Checkin type & drivers")
        fig = px.histogram(df, x="delay",
                color="checkin_type",
                barmode = "group",
                width = 800,
                height = 600,
                histnorm = "percent",
                text_auto = True)
        fig.update_traces(textposition = "outside", textfont_size = 15)
        fig.update_layout(margin=dict(l=50,r=50,b=50,t=50,pad=4),
                  yaxis = {"visible": False}, 
                  xaxis = {"visible": True})
        fig.update_xaxes(tickfont_size=15)                     
        st.plotly_chart(fig)
        
st.subheader("Checkin type & status of rental")
fig = px.histogram(df, x = "state",
                   color = "checkin_type",
                   barmode ="group",
                   width= 800,
                   height = 600,
                   histnorm = "percent",
                   text_auto = True)
fig.update_traces(textposition = "outside", textfont_size = 15)
fig.update_layout(margin=dict(l=50,r=50,b=50,t=50,pad=4),
                  yaxis = {"visible": False}, 
                  xaxis = {"visible": True})
fig.update_xaxes(tickfont_size=15)                     
st.plotly_chart(fig)