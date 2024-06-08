import streamlit as st
import requests
import pandas as pd

st.title("CSV Upload")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    # Salvar o arquivo temporariamente e depois enviar
    with open("temp_file.csv", "wb") as f:
        f.write(uploaded_file.getvalue())  # Salva os dados do arquivo
    with open("temp_file.csv", "rb") as f:
        response = requests.post("http://localhost:5000/upload", files={"file": f})
        if response.status_code == 200:
            data = response.json()
            st.write("Mediana do Valor Monetário:", data['mediana'])  # KeyError likely occurs here
            st.write(data['res'])
        else:
            st.error(response.json().get("error"))




    if st.button("Análises Adicionais para Possíveis Insights"):
        insights_response = requests.post(
            "http://localhost:5000/additional_insights",
            files={"file": uploaded_file.getvalue()}
        )
        if insights_response.status_code == 200:
            insights_data = insights_response.json()
            st.write("Máxima:", insights_data['maxima'])
            st.write("Mínima:", insights_data['minima'])
            st.write("Moda:", insights_data['moda'])
            st.write("Variância:", insights_data['variancia'])
            st.write("Desvio Padrão:", insights_data['desvio_padrao'])
        else:
            st.error(insights_response.json().get("error"))
