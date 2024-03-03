import pandas as pd
import streamlit as st
#clean data


import os

# Get the current working directory
current_dir = os.path.dirname(__file__)

x_axis = ['max_day','min_day','max_stat','min_stat']

# Specify the file path to access day.csv
file_path_1 = os.path.join(current_dir, 'answer_1.csv')
file_path_2 = os.path.join(current_dir, 'answer_2.csv')

# Read the CSV file
df_1 = pd.read_csv(file_path_1)

df_2 = pd.read_csv(file_path_2)

df_1['temp'] *= 41
df_1['atemp'] *= 50
df_1['windspeed'] *= 67
df_1['windspeed'] *= 100

st.title('Bike Sharing Statistic Analysis')

st.subheader('Your Analyst')
st.write('Name : Fadhlan Nazhif Azizy')
st.write('Email: fadhlannazhif5@gmail.com')
st.write('Bangkit-ID : fadhlan_nazhif_azizy_KOlf')

tab1, tab2 = st.tabs(["analysis 1", "analysis 2"])

st.write('    ')
st.write('    ')

with tab1:
    col1, col2 = st.columns(2) 
    col3, col4 = st.columns(2)

    with col1:
        st.header('temperature measurement')
        st.bar_chart(df_1.loc[:,['temp','index']], x='index',y='temp', width=1)

    with col2:
        st.header('feeling temperature measurement')
        st.bar_chart(df_1.loc[:,['atemp','index']], x='index',y='atemp', width=1)

    with col3:
        st.header('windspeed measurement')
        st.bar_chart(df_1.loc[:,['windspeed','index']], x='index',y='windspeed', width=1)

    with col4:
        st.header('humidity measurement')
        st.bar_chart(df_1.loc[:,['hum','index']], x='index',y='hum', width=1)

    st.subheader('conclusion')
    st.write('Jumlah perental akan banyak apabila suhu udara cenderung hangat, kelembapan udara sedang dan kecepatan angin sedang. Serta jumlah perental akan sedikit apabila suhu udara cenderung sejuk, kelembapan udara tinggi, dan kecepatan angin tinggi.')

with tab2:
    st.header('')
    st.bar_chart(df_2, x='weather', y='cnt')

    st.subheader('conclusion')
    st.write('Jumlah perental akan cenderung tinggi ketika kondisi lingkungan memenuhi kategori weathersit 1, yaitu Clear, Few clouds, Partly cloudy, Partly cloudy. Jumlah perental akan sedang ketika memnuhi kategori weathersit 2 yaitu Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist. Dan jumlah perental akan cenderung rendah ketika kondisi lingkungan memenuhi kategori 3 yaitu Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')


