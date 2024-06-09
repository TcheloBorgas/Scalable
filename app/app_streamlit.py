#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import streamlit as st
import pandas as pd
import json
import base64
from cliente import Cliente
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

#━━━━━━━━━━━━━━❮Plano de fundo❯━━━━━━━━━━━━━━


def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
    
    
encoded_image = img_to_base64(r'template\fundo.jpg')  # Ajuste o caminho conforme necessário

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """, unsafe_allow_html=True)

# Chama a função para adicionar a imagem de fundo
add_bg_from_local()

#━━━━━━━━━━━━━━❮Configuração inicial do site❯━━━━━━━━━━━━━━
st.set_page_config(page_title="Análise de Dados de Clientes", page_icon=":bar_chart:", layout="wide")

st.title("Análise de Dados de Clientes")


#━━━━━━━━━━━━━━❮upload de arquivo❯━━━━━━━━━━━━━━
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")


#━━━━━━━━━━━━━━❮Verificação de coluna❯━━━━━━━━━━━━━━
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if 'Valor Monetario' not in df.columns:
        st.error("CSV does not have required 'Valor Monetario' column")
    
    
    #━━━━━━━━━━━━━━❮Renderização de estatisticas❯━━━━━━━━━━━━━━

    else:
        st.write(df)

        cliente = Cliente(df)


        with st.expander("Estatísticas"):
            st.write("Estatísticas")

            if st.button("Calcular Mediana"):
                mediana = cliente.calcular_mediana()
                st.write({"mediana": mediana})

        with st.expander("Análises Adicionais"):
            if st.button("Calcular Análises Adicionais"):
                insights = cliente.calcular_analises_adicionais()
                st.write(insights)

        with st.expander("Exportar JSON"):
            if st.button("Exportar JSON"):
                json_data = cliente.converter_para_json()
                st.download_button(label="Baixar JSON", data=json_data, file_name="dados_clientes.json", mime="application/json")
                st.json(json.loads(json_data))
