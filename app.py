import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Configurações da página
st.set_page_config(page_title="Modelo de Confiança - Angola", layout="wide")

# Título
st.title("Modelo Preditivo de Confiança nas Instituições Públicas em Angola")

# Introdução
st.markdown("""
Este aplicativo apresenta os resultados de um estudo baseado nos dados da 10ª rodada do Afrobarômetro (2024), com foco em Angola.
O objetivo é prever a confiança nas instituições públicas (Presidência, Parlamento e Tribunais) a partir de variáveis sociodemográficas e percepções políticas.
""")

# Carregamento de dados
st.subheader("Visualização dos Dados")
try:
    df = pd.read_excel("data/angola_afrobarometro_r10.xlsx")

    # Filtros interativos na barra lateral
    st.sidebar.header("🔎 Filtros Interativos")

    # Gênero
    genero_map = {1: "Masculino", 2: "Feminino"}
    genero_opcao = st.sidebar.selectbox("Gênero", options=["Todos"] + list(genero_map.values()))
    if genero_opcao != "Todos":
        genero_cod = [k for k, v in genero_map.items() if v == genero_opcao][0]
        df = df[df["Q1"] == genero_cod]

    # Idade
    if "Q2" in df.columns:
        idade_min = int(df["Q2"].min())
        idade_max = int(df["Q2"].max())
        idade_sel = st.sidebar.slider("Faixa Etária", idade_min, idade_max, (idade_min, idade_max))
        df = df[(df["Q2"] >= idade_sel[0]) & (df["Q2"] <= idade_sel[1])]

    # Escolaridade
    if "Q3" in df.columns:
        escolaridades = df["Q3"].dropna().unique()
        escolaridade_sel = st.sidebar.selectbox("Escolaridade (código)", ["Todos"] + list(map(int, escolaridades)))
        if escolaridade_sel != "Todos":
            df = df[df["Q3"] == escolaridade_sel]

    # Região
    if "REGION" in df.columns:
        regioes = df["REGION"].dropna().unique()
        regiao_sel = st.sidebar.selectbox("Região (código)", ["Todas"] + list(regioes))
        if regiao_sel != "Todas":
            df = df[df["REGION"] == regiao_sel]

    # Avaliação do Presidente (Q95)
    if "Q95" in df.columns:
        avaliacoes = df["Q95"].dropna().unique()
        avaliacao_sel = st.sidebar.selectbox("Avaliação do Presidente (Q95)", ["Todas"] + list(avaliacoes))
        if avaliacao_sel != "Todas":
            df = df[df["Q95"] == avaliacao_sel]

    # Exibir dados filtrados
    st.dataframe(df.head(20))

except:
    st.warning("Arquivo de dados não encontrado. Certifique-se de que 'angola_afrobarometro_r10.xlsx' está na pasta 'data'.")

# Exibição de gráficos de importância
st.subheader("Importância das Variáveis nos Modelos")
cols = st.columns(3)

with cols[0]:
    st.markdown("**Presidência (Q70A)**")
    try:
        img = Image.open("imagens/grafico_q70a.png")
        st.image(img, caption="Importância das variáveis - Presidência")
    except:
        st.warning("Imagem 'grafico_q70a.png' não encontrada.")

with cols[1]:
    st.markdown("**Parlamento (Q70B)**")
    try:
        img = Image.open("imagens/grafico_q70b.png")
        st.image(img, caption="Importância das variáveis - Parlamento")
    except:
        st.warning("Imagem 'grafico_q70b.png' não encontrada.")

with cols[2]:
    st.markdown("**Tribunais (Q70C)**")
    try:
        img = Image.open("imagens/grafico_q70c.png")
        st.image(img, caption="Importância das variáveis - Tribunais")
    except:
        st.warning("Imagem 'grafico_q70c.png' não encontrada.")

# Resultados principais
st.subheader("📊 Principais Resultados do Estudo")
st.markdown("""
- A **classe mais previsível** nos três modelos foi "bastante confiança" (classe 4), com F1-score médio superior a 0.57.
- As **variáveis mais importantes** foram:
    - Avaliação do presidente (Q95)
    - Percepção de corrupção (Q60A e Q60B)
    - Escolaridade (Q3)
    - Satisfação com a democracia (Q103)
- As **classes extremas** ("nenhuma confiança" e "muita confiança") apresentaram menor desempenho preditivo.
- A técnica **SMOTE** foi essencial para equilibrar as classes e melhorar a performance dos modelos Random Forest.
- O modelo sugere que **atitudes institucionais são fortemente moldadas por percepções políticas e fatores socioeducacionais**.
""")

# Metodologia
st.subheader("Resumo da Metodologia")
st.markdown("""
- **Base de Dados:** Afrobarômetro R10 Angola (2024).
- **Variáveis Dependentes:** Confiança na Presidência, Parlamento e Tribunais.
- **Algoritmo:** Random Forest com balanceamento via SMOTE.
- **Métricas de Avaliação:** F1-score, precisão, recall.

Principais variáveis explicativas:
- Avaliação do presidente (Q95)
- Percepção de corrupção (Q60A, Q60B)
- Escolaridade (Q3)
- Satisfação com a democracia (Q103)
""")

# Rodapé
st.markdown("---")
st.markdown("Pedro Joao | © 2025")


