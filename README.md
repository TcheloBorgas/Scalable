# Projeto Scalable

## Descrição

O projeto Scalable é uma aplicação web que utiliza Flask e Streamlit para lidar com arquivos CSV contendo dados de usuários, realizar validações e retornar dados em formato JSON, incluindo análises estatísticas. O backend será hospedado no Railway.app e segue padrões de código limpo. O projeto é modular e permite a realização de análises estatísticas como máximo, mínimo, média, moda, desvio padrão e variância.


## Estrutura de arquivos

```
C:.
│   Dockerfile
│   README.md
│   requirements.txt
│   supervisord.conf
│   Template Scalable Test - Página1.csv
│   temp_file.csv
│
└───app
    │   app.py
    │   app_streamlit.py
    │   cliente.py
    │   factory.py
    │   routes.py
    │   utils.py
    │   __init__.py
    │
    ├───template
    └───__pycache__
            app.cpython-311.pyc
            cliente.cpython-311.pyc
            factory.cpython-311.pyc
            routes.cpython-311.pyc
            utils.cpython-311.pyc
            __init__.cpython-311.pyc
```

## Requisitos

- Python 3.8 ou superior
- Flask
- Streamlit
- Pandas
- Docker
- Supervisord

## Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/scalable.git
cd scalable
```

2. Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

# Uso
## Executando Localmente

1. Inicie o servidor Flask:

```
python app.py
```

2. Em outro terminal, inicie o Streamlit:

```
streamlit run app_streamlit.py
```

# Usando Docker

1. Construa a imagem Docker:

```
docker build -t scalable:latest .
```

2. Inicie o container:

```
docker run -d -p 5000:5000 scalable:latest
```


# Configuração do Supervisord
O arquivo supervisord.conf é usado para gerenciar processos do Flask e do Streamlit. Certifique-se de que o Supervisord esteja instalado e configurado corretamente.

# API Endpoints
## Upload de CSV
* URL: /upload
* Método: POST
* Descrição: Faz o upload de um arquivo CSV para validação e análise.


# Análises Estatísticas
* URL: /stats
* Método: GET
* Descrição: Retorna análises estatísticas (máximo, mínimo, média, moda, desvio padrão, variância).


# Estrutura dos Arquivos
## app.py
Define a aplicação Flask e seus endpoints.

## app_streamlit.py
Configura a interface Streamlit para visualização e interação com os dados.

## cliente.py
Contém funções relacionadas ao cliente, como manipulação de dados e validação.

## factory.py
Implementa o padrão de fábrica para criar instâncias de objetos necessários.

## routes.py
Define as rotas da aplicação Flask.

## utils.py
Contém funções utilitárias para análise de dados e operações auxiliares.

## Dockerfile
Define a configuração Docker para a construção da imagem da aplicação.

## supervisord.conf
Configura o Supervisord para gerenciar e monitorar processos da aplicação.

## __init__.py
Inicializa o pacote Python.


