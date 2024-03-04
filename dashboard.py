import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load Data
hour_df = pd.read_csv("all_data.csv")

# Sidebar with author information
st.sidebar.header("Author Information")
st.sidebar.text("Name: Teuku Muhammad Faiz Nuzullah")
st.sidebar.text("Kaggle: skydream12")
st.sidebar.text("Bangkit ID: m322d4ky2761")

# Title
st.header('Bike Rental Dashboard :sparkles:')
def handle_boxplot(data, x_col, y_col, title):
    """
    Creates and displays boxplots with custom logic to handle empty plots.

    Args:
        data (pd.DataFrame): Input DataFrame containing the data.
        x_col (str): Name of the column to use for the x-axis.
        y_col (str): Name of the column to use for the y-axis.
        title (str): Title for the boxplot.
    """

    if data[x_col].nunique() > 1:  # Check for sufficient unique values
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=x_col, y=y_col, data=data)
        plt.title(title)
        sns.despine(top=True, right=True, left=False, bottom=False)

        # Adding labels to the boxplot
        for box in plt.gca().artists:  # Use gca() to ensure correct access to artists
            if box.get_xdata() is not None and len(box.get_xdata()) > 0:
                box_coords = [(box.get_xdata()[j], box.get_ydata()[j]) for j in range(len(box.get_xdata()))]
                box_height = box_coords[3][1] - box_coords[0][1]
                median_x = box_coords[2][0]
                plt.text(median_x, box_coords[0][1] + box_height * 0.5, f"{int(box.get_height())}",
                          va='center', ha='center', fontsize=10)
        st.pyplot(plt)
    else:
        st.write("Insufficient data for boxplot. Please review your data for unique values.")

# 1. Distribusi Penyewaan Sepeda per Jam
st.subheader("Distribusi Penyewaan Sepeda per Jam")

handle_boxplot(hour_df, "hr", "cnt", "Distribusi Penyewaan Sepeda per Jam")

# 2. Distribusi Penyewaan Sepeda per Minggu
st.subheader("Distribusi Penyewaan Sepeda per Minggu")

handle_boxplot(hour_df, "weekday", "cnt", "Distribusi Penyewaan Sepeda per Minggu")

# 3. Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim
st.subheader("Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim")

# Visualisasi
plt.figure(figsize=(12, 6))
bar = sns.barplot(data=hour_df, x="season", y="cnt", hue="yr", palette="rocket", errorbar=None)
plt.title('Jumlah Penggunaan Sepeda Dalam Satu Tahun Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan')
sns.despine(top=True, right=True, left=False, bottom=False)

plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])

plt.legend(title='Tahun', loc='best', labels=['2011', '2012'], frameon=False)
st.pyplot(plt)

st.caption("Copyright © faiz_nuzullah")
