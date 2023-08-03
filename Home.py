import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")

st.markdown("""<p style="font-family:Futura; color:white; font-size: 80px;">Liga.Footy</p>""",unsafe_allow_html=True)

st.markdown(
    """
    <p style="font-family:Gill Sans; color:white; font-size: 18px;">
    Liga.Footy is a user-friendly Streamlit web application designed for football enthusiasts, analysts, and fans to gain deeper insights into their favorite players' performance. 
    This intuitive app offers three key features that allow users to explore and analyze player statistics in an interactive and visually appealing manner.
    
    <p style="font-family:Futura; color:#38B6FF; font-size: 17px;">1. Player Pizza Plots</p>
    <p style="font-family:Gill Sans; color:white; font-size: 17px;">Visualize a player's performance distribution across different statistical categories using engaging pizza plots</p>
    
    <p style="font-family:Futura; color:#38B6FF; font-size: 17px;">2. Player Comparison Radar Plots</p>
    <p style="font-family:Gill Sans; color:white; font-size: 17px;">Compare the performance of two players using radar plots, also known as spider plots</p>
    
    <p style="font-family:Futura; color:#38B6FF; font-size: 17px;">3. Player Match Reports</p>
    <p style="font-family:Gill Sans; color:white; font-size: 17px;">Dive into detailed match reports for a selected player's recent game using event data</p>
    
    </p>
    """,unsafe_allow_html=True
)




image1 = Image.open('data/images/pizza.jpeg')
image2 = Image.open('data/images/Radar.jpeg')
image3 = Image.open('data/images/matcha.jpeg')

st.image([image1,image2,image3],caption=["Pizza Plot","Radar Plot","Match Report"],width=260)

st.markdown('<p style="font-family:Futura; color:#38B6FF; font-size: 15px;">Data: FBREF,Opta Made by : Ligandro</p>',unsafe_allow_html=True)
