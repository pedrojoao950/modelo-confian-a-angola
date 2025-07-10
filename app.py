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
st.subheader("Visualização dos Dados (exemplo)")
try:
    df = pd.read_excel("data/angola_afrobarometro_r10.xlsx")
    st.dataframe(df.head())
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
st.markdown("Desenvolvido com Streamlit | © 2025 Pedro Joao | All Rights Reserved")
