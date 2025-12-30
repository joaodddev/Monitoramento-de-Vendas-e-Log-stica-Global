import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚀 Dashboard no Google Colab")
st.write("Se você está vendo isso, o Streamlit está funcionando!")

# Aqui você colaria o código de ETL que te passei anteriormente
df = pd.DataFrame({'Vendas': [10, 20, 30], 'Mes': ['Jan', 'Fev', 'Mar']})
fig = px.bar(df, x='Mes', y='Vendas')
st.plotly_chart(fig)
