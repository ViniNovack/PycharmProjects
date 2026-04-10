import streamlit
import pandas
import plotly.express

# Define o título da página
st.title("Análise de Arrecadação - 23 Meses")
st.write("Edite os valores na tabela abaixo para atualizar o gráfico em tempo real!")

# 1. Gerando a lista de meses (Conceito: List Comprehension)
meses = [f"Mês {i}" for i in range(1, 24)]

# 2. Estruturando os dados (Conceito: Pandas DataFrame)
dados_iniciais = pd.DataFrame({
    "Mês": meses,
    "Arrecadação (R$)": [0.0] * 23  # Cria uma lista com 23 zeros
})

# 3. Criando a interface de entrada (Conceito: Reatividade)
dados_usuario = st.data_editor(dados_iniciais, hide_index=True)

# 4. Criando o gráfico interativo (Conceito: Plotly Express)
fig = px.bar(
    dados_usuario, 
    x="Mês", 
    y="Arrecadação (R$)", 
    title="Evolução da Arrecadação",
    text_auto=True # Mostra o número em cima da coluna
)

# 5. Desenhando o gráfico na tela
st.plotly_chart(fig)
