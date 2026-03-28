import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(
    page_title="DHL Inbound Optimization", 
    layout="wide", 
    page_icon="📦"
)

# 2. Estilização Customizada (Cores DHL)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { color: #D40511; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.title("📦 Dashboard de Otimização Operacional – Inbound XPTO")
st.markdown("### Foco: Incremento de +20% na Eficiência de Packaging")

# 4. Estrutura de Dados
data = {
    "Métrica": ["Produtividade (pç/h)", "Capacidade Mensal", "Headcount"],
    "AS-IS": [944, 5480000, 30],
    "TO-BE": [1132, 6570000, 25]
}
df = pd.DataFrame(data)

# 5. KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Produtividade Alvo", 
        value="1.132 pç/h", 
        delta="+20% vs Atual",
        help="Peças processadas por hora/colaborador."
    )

with col2:
    st.metric(
        label="Capacidade Sistêmica", 
        value="6,57 Mi", 
        delta="+1,09 Mi pç/mês",
        help="Aumento da vazão mensal."
    )

with col3:
    st.metric(
        label="Dimensionamento (FTE)", 
        value="25 Colaboradores", 
        delta="-5 Postos de Trabalho",
        delta_color="inverse",
        help="Redução de headcount operacional."
    )

st.markdown("---")

# 6. Visualização Gráfica
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📈 Evolução da Produtividade")
    df_prod = df.set_index("Métrica").loc["Produtividade (pç/h)"].to_frame().T
    st.bar_chart(df_prod)

with right_col:
    st.subheader("👥 Otimização de Recursos")
    df_hc = df.set_index("Métrica").loc["Headcount"].to_frame().T
    st.bar_chart(df_hc)

# 7. Interatividade (diferencial)
st.markdown("---")
st.subheader("📊 Análise Interativa")

metric_choice = st.selectbox(
    "Selecione a Métrica para análise:",
    df["Métrica"]
)

filtered = df.set_index("Métrica").loc[metric_choice].to_frame().T
st.bar_chart(filtered)

# 8. Tabela + Insights
st.markdown("---")
st.subheader("📋 Racional Técnico do Case")

c1, c2 = st.columns([1, 2])

with c1:
    st.table(df)

with c2:
    st.info("""
    **Principais Alavancas de Ganho:**
    
    * **Layout & Fluxo:** Eliminação de movimentações manuais com célula integrada.
    * **Ergonomia:** Redução do tempo de ciclo (5S + ferramentas adequadas).
    * **Tecnologia:** Uso de esteiras para fluxo contínuo e menor ociosidade.
    """)

# 9. KPI adicional calculado
st.markdown("---")
prod_gain = (1132 - 944) / 944
st.metric("📊 Ganho Real de Produtividade", f"{prod_gain:.1%}")

# Rodapé
st.caption("Desenvolvido para o Processo Seletivo DHL - Analista de Process Excellence")