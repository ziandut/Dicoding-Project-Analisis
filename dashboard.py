import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load Data
hour_df = pd.read_csv("all_data.csv")

#Sidebar with author information
st.sidebar.header("Author Information")
st.sidebar.text("Name: Teuku Muhammad Faiz Nuzullah")
st.sidebar.text("Kaggle: skydream12")
st.sidebar.text("Bangkit ID: m322d4ky2761")

# Title
st.header('Bike Rental Dashboard :sparkles:')

# 1. Distribusi Penyewaan Sepeda per Jam
st.subheader("Distribusi Penyewaan Sepeda per Jam")

# Visualisasi
plt.figure(figsize=(12,6))
ax = sns.boxplot(x='hr', y='cnt', data=hour_df)
plt.title('Distribusi Penyewaan Sepeda per Jam')
sns.despine(top=True, right=True, left=False, bottom=False)

# Adding labels to the boxplot
for box in ax.artists:
    if box.get_xdata() is not None and len(box.get_xdata()) > 0:
        box_coords = [(box.get_xdata()[j], box.get_ydata()[j]) for j in range(len(box.get_xdata()))]
        box_height = box_coords[3][1] - box_coords[0][1]
        median_x = box_coords[2][0]
        ax.text(median_x, box_coords[0][1] + box_height * 0.5, f"{int(box.get_height())}",
                va='center', ha='center', fontsize=10)

st.pyplot(plt)

# 2. Distribusi Penyewaan Sepeda per Minggu
st.subheader("Distribusi Penyewaan Sepeda per Minggu")

# Visualisasi
plt.figure(figsize=(12,6))
sns.boxplot(x='weekday', y='cnt', data=hour_df)
sns.despine(top=True, right=True, left=False, bottom=False)
plt.title('Distribusi Penyewaan Sepeda per Minggu')
st.pyplot(plt)

# 3. Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim
st.subheader("Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim")

#  Visualisasi
plt.figure(figsize=(12, 6))
bar = sns.barplot(data=hour_df, x="season", y="cnt", hue="yr", palette="rocket", errorbar=None)
sns.despine(top=True, right=True, left=False, bottom=False)

plt.ylabel('Count of rents')
plt.xlabel('Season')
plt.title("Jumlah Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim", size=14, y=1.12)

plt.xticks([0, 1, 2, 3], ['Springer', 'Summer', 'Fall', 'Winter'])

plt.legend(title='Year', loc='best', labels=['2011', '2012'], frameon=False)
st.pyplot(plt)

st.caption("Copyright © faiz_nuzullah")
