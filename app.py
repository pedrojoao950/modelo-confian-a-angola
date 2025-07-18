import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Page configuration
st.set_page_config(page_title="Trust Model - Angola", layout="wide")

# Title
st.title("Predictive Model of Public Trust in Angolan Institutions")

# Introduction
st.markdown("""
This app presents the results of a study based on data from the 10th round of Afrobarometer (2024), focusing on Angola.
The goal is to predict trust in public institutions (Presidency, Parliament, and Courts) based on sociodemographic variables and political perceptions.
""")

# Data loading
st.subheader("Data Visualization")
try:
    df = pd.read_excel("data/angola_afrobarometro_r10.xlsx")

    # Interactive filters in the sidebar
    st.sidebar.header("🔎 Interactive Filters")

    # Gender
    genero_map = {1: "Male", 2: "Female"}
    genero_opcao = st.sidebar.selectbox("Gender", options=["All"] + list(genero_map.values()))
    if genero_opcao != "All":
        genero_cod = [k for k, v in genero_map.items() if v == genero_opcao][0]
        df = df[df["Q1"] == genero_cod]

    # Age
    if "Q2" in df.columns:
        idade_min = int(df["Q2"].min())
        idade_max = int(df["Q2"].max())
        idade_sel = st.sidebar.slider("Age Range", idade_min, idade_max, (idade_min, idade_max))
        df = df[(df["Q2"] >= idade_sel[0]) & (df["Q2"] <= idade_sel[1])]

    # Education
    if "Q3" in df.columns:
        escolaridades = df["Q3"].dropna().unique()
        escolaridade_sel = st.sidebar.selectbox("Education Level (code)", ["All"] + list(map(int, escolaridades)))
        if escolaridade_sel != "All":
            df = df[df["Q3"] == escolaridade_sel]

    # Region
    if "REGION" in df.columns:
        regioes = df["REGION"].dropna().unique()
        regiao_sel = st.sidebar.selectbox("Region (code)", ["All"] + list(regioes))
        if regiao_sel != "All":
            df = df[df["REGION"] == regiao_sel]

    # President rating (Q95)
    if "Q95" in df.columns:
        avaliacoes = df["Q95"].dropna().unique()
        avaliacao_sel = st.sidebar.selectbox("President's Performance (Q95)", ["All"] + list(avaliacoes))
        if avaliacao_sel != "All":
            df = df[df["Q95"] == avaliacao_sel]

    # Display filtered data
    st.dataframe(df.head(20))

except:
    st.warning("Data file not found. Make sure 'angola_afrobarometro_r10.xlsx' is in the 'data' folder.")

# Variable importance plots
st.subheader("Variable in Models")
cols = st.columns(3)

with cols[0]:
    st.markdown("**Presidency (Q70A)**")
    try:
        img = Image.open("imagens/grafico_q70a.png")
        st.image(img, caption="Variable - Presidency")
    except:
        st.warning("Image 'grafico_q70a.png' not found.")

with cols[1]:
    st.markdown("**Parliament (Q70B)**")
    try:
        img = Image.open("imagens/grafico_q70b.png")
        st.image(img, caption="Variable - Parliament")
    except:
        st.warning("Image 'grafico_q70b.png' not found.")

with cols[2]:
    st.markdown("**Courts (Q70C)**")
    try:
        img = Image.open("imagens/grafico_q70c.png")
        st.image(img, caption="Variable - Courts")
    except:
        st.warning("Image 'grafico_q70c.png' not found.")

# Main results
st.subheader("📊 Main Study Findings")
st.markdown("""
- The **most predictable class** in all three models was "somewhat trust" (class 4), with an average F1-score above 0.57.
- The **most important variables** were:
    - President's evaluation (Q95)
    - Perception of corruption (Q60A and Q60B)
    - Education level (Q3)
    - Satisfaction with democracy (Q103)
- **Extreme classes** ("no trust" and "full trust") had lower predictive performance.
- The **SMOTE technique** was essential to balance classes and improve Random Forest performance.
- The model suggests that **institutional attitudes are strongly shaped by political perceptions and educational factors**.
""")

# Methodology
st.subheader("Methodology Summary")
st.markdown("""
- **Database:** Afrobarometer R10 Angola (2024).
- **Dependent Variables:** Trust in the Presidency, Parliament, and Courts.
- **Algorithm:** Random Forest with SMOTE class balancing.
- **Evaluation Metrics:** F1-score, precision, recall.

Main explanatory variables:
- President's evaluation (Q95)
- Perception of corruption (Q60A, Q60B)
- Education level (Q3)
- Satisfaction with democracy (Q103)
""")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | © 2025 Pedro Joao | All Rights Reserved")


