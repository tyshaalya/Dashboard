#library yang digunakan

import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Judul Dashboard
st.title("🚴Let's Go Bike Sharing🚴")
st.caption("by Tysha Alya Ramadhany")
st.header("Hello, Bikers!")
st.text("Welcome to Bike Sharing Dashboard ✨ ")

##1. Visualisasi Distribusi total pengguna sepeda berdasarkan waktu 
#Judul Grafik
st.subheader("Distribution of Total Number Bike Users Based on Usage Time")
hour_df = pd.read_csv('https://github.com/tyshaalya/DataAnalis/raw/2b859d7d6d7692e3b31a1b397a104eec38612ac0/bikers/hour.csv')
distribusi_waktu_hari = hour_df.groupby('hr')['cnt'].sum().reset_index()
#Menampilkan barchart 
plt.figure(figsize=(10, 5))
plt.bar(distribusi_waktu_hari['hr'], distribusi_waktu_hari['cnt'], color='red')
plt.title('Distribusi Jumlah Pengguna Sepeda Berdasarkan Waktu')
plt.ylabel('Jumlah Pengguna')
plt.xlabel('Waktu')

st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

#2. Visualisasi total pengguna sepeda berdasarkan musim
day_df = pd.read_csv('https://raw.githubusercontent.com/tyshaalya/DataAnalis/2b859d7d6d7692e3b31a1b397a104eec38612ac0/bikers/day.csv')
st.subheader("Total of Bike Users Based on Season")
sum_musim_day = day_df.groupby(['yr', 'season'])['cnt'].sum().reset_index()
#Menampilkan barchart perbandingan pengguaan sepeda pada tahun berbeda
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24,6))

colors=["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]

sns.barplot(x="season", y="cnt", data=sum_musim_day[sum_musim_day['yr']==0], palette=colors, ax=ax[0])
ax[0].set_ylabel("Jumlah Pengguna")
ax[0].set_xlabel("Musim")
ax[0].set_title("Pengguna Sepeda Berdasarkan Musim (2011)", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="season", y="cnt", data=sum_musim_day[sum_musim_day['yr']==1], palette=colors, ax=ax[1])
ax[1].set_ylabel("Jumlah Pengguna")
ax[1].set_xlabel("Musim")
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Pengguna Sepeda Berdasarkan Musim (2012)", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
st.pyplot(fig)
#ax[0] kanvas pertama
#ax[1] kanvas kedua