import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


data = pd.read_csv(r"C:\Users\impec\Downloads\netflix_titles.csv.zip")

print(data.head())

print("Total rows:", len(data))

print("Columns:", data.columns)

print("Movies vs TV Shows:")
print(data["type"].value_counts())

counts = data["type"].value_counts()

counts.plot(kind="bar")

plt.title("Movies vs TV Shows")

plt.show()

data = pd.read_csv("netflix_titles.csv")

st.title("Netflix Data Analysis")

st.write("Dataset Preview")

st.dataframe(data.head())

st.write("Movies vs TV Shows")

st.bar_chart(data["type"].value_counts())