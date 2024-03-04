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
for line in ax.lines:
    x_data = line.get_xdata()
    y_data = line.get_ydata()
    if len(x_data) > 0:  # Ensure there is data in the line
        median_x = x_data[0]  # Median line's x-coordinate
        median_y = y_data[0]  # Median line's y-coordinate
        ax.text(median_x, median_y, f"{int(median_y)}",
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