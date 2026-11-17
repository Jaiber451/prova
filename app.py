import pandas as pd
import plotly.express as px
import streamlit as st

from modelo import df_tabela, df_filtrado

st.set_page_config(page_title="Prova IQVU", layout="wide")
st.title("Prova — IQVU: Taquaril x Santa Ines")

CORES = {"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"}
DIMENSOES = ["Educacao", "Saude", "Habitacao", "Infraestrutura", "Cultura"]

df_2016 = df_filtrado[df_filtrado["ANO"] == 2016]
dados_longos = df_2016.melt(
    id_vars="NOMEUP",
    value_vars=DIMENSOES,
    var_name="Dimensao",
    value_name="Valor",
).rename(columns={"NOMEUP": "Bairro"})

dados_empilhado = dados_longos[["Bairro", "Dimensao", "Valor"]]
dados_radar = dados_longos.rename(columns={"Valor": "Nota"})[["Bairro", "Dimensao", "Nota"]]
dados_pizza = pd.DataFrame(
    {"Bairro": ["Taquaril", "Santa Ines"], "IQVU": [0.568, 0.756]}
)

# Questão 1 — Gráfico de linha individual (Taquaril)
st.header("Questão 1 — Linha (Taquaril)")
df_taquaril = df_tabela[df_tabela["NOMEUP"] == "Taquaril"]
fig1 = px.line(
    df_taquaril,
    x="ANO",
    y="IQVU",
    markers=True,
    title="Evolução do IQVU — Taquaril (1994 a 2016)",
    template="plotly_dark",
)
fig1.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
fig1.update_xaxes(type="category")
st.plotly_chart(fig1, use_container_width=True)

# Questão 2 — Gráfico de linha individual (Santa Inês)
st.header("Questão 2 — Linha (Santa Inês)")
df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "Santa Ines"]
fig2 = px.line(
    df_santa_ines,
    x="ANO",
    y="IQVU",
    markers=True,
    title="Evolução do IQVU — Santa Inês (1994 a 2016)",
    template="plotly_dark",
)
fig2.update_traces(line_color="#00F5D4", line_width=3, marker_size=8)
fig2.update_xaxes(type="category")
st.plotly_chart(fig2, use_container_width=True)

# Questão 3 — Gráfico de barras agrupadas
st.header("Questão 3 — Viagens agrupadas")
fig3 = px.bar(
    df_tabela,
    x="ANO",
    y="IQVU",
    quantidade= "quantidade de viagens"
    color="NOMEUP",
    barmode="group",
    title="Comparativo Anual de IQVU (Viagens Agrupadas)",
    color_discrete_map=CORES,
    template="plotly_dark",
)
fig3.update_xaxes(type="category")
st.plotly_chart(fig3, use_container_width=True)

st.header("— Viagens empilhadas")
fig4 = px.bar(
    dados_empilhado,
    x="Viagem ",
    y="Valor",
    color="Dimensao",
    barmode="stack",
    title="Composição do IQVU por Dimensão — Ano 2016 (Barras Empilhadas)",
    template="plotly_dark",
)
st.plotly_chart(fig4, use_container_width=True)

st.header("Questão 5 — Pizza")
fig5 = px.pie(
    dados_pizza,
    names="Bairro",
    values="IQVU",
    title="Proporção do IQVU entre os Bairros (2016)",
    color="Bairro",
    color_discrete_map=CORES,
    template="plotly_dark",
)
fig5.update_traces(textinfo="percent+label+value")
st.plotly_chart(fig5, use_container_width=True)

st.header("Questão 6 — Radar")
fig6 = px.line_polar(
    dados_radar,
    r="Nota",
    theta="Dimensao",
    color="Bairro",
    line_close=True,
    title="Perfil Multidimensional (Gráfico de Radar - 2016)",
    color_discrete_map=CORES,
    template="plotly_dark",
)
fig6.update_traces(fill="toself")
fig6.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
st.plotly_chart(fig6, use_container_width=True)

st.header("Questão 7 — Área")
fig7 = px.area(
    df_tabela,
    x="ANO",
    y="IQVU",
    color="NOMEUP",
    title="Evolução em Área do IQVU (1994 a 2016)",
    color_discrete_map=CORES,
    template="plotly_dark",
)
fig7.update_xaxes(type="category")
st.plotly_chart(fig7, use_container_width=True)

st.header("Questão 8 — Dispersão (bolhas)")
fig8 = px.scatter(
    df_filtrado,
    x="Educacao",
    y="Saude",
    color="NOMEUP",
    size="IQVU",
    hover_data=["ANO"],
    title="Dispersão: Educação vs Saúde (Tamanho = IQVU)",
    color_discrete_map=CORES,
    template="plotly_dark",
)
st.plotly_chart(fig8, use_container_width=True)

st.header("Questão 9 — Boxplot")
fig9 = px.box(
    df_tabela,
    x="NOMEUP",
    y="IQVU",
    color="NOMEUP",
    points="all",
    title="Distribuição Estatística do IQVU (Boxplot)",
    color_discrete_map=CORES,
    template="plotly_dark",
)
st.plotly_chart(fig9, use_container_width=True)
