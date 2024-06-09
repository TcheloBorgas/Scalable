#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import numpy as np
import pandas as pd
import re
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

#━━━━━━━━━━━━━━❮Mediana❯━━━━━━━━━━━━━━

def calculate_median(values):
    try:
        return np.median(values.astype(float)) 
    except ValueError:
        return "Erro: Dados inválidos."


#━━━━━━━━━━━━━━❮Conversão para floar❯━━━━━━━━━━━━━━
def convert_currency_to_float(value):
    cleaned_value = re.sub(r'[^\d,]', '', value) 
    return float(cleaned_value.replace(',', '.'))

#━━━━━━━━━━━━━━❮Reformatação❯━━━━━━━━━━━━━━

def reformat_to_currency(value):
    return f"R$ {value:,.2f}".replace(',', 'x').replace('.', ',').replace('x', '.')


#━━━━━━━━━━━━━━❮Insights adicionais❯━━━━━━━━━━━━━━

def calculate_additional_insights(values):
    max_value = values.max()
    min_value = values.min()
    mode_value = values.mode().iloc[0] if not values.mode().empty else None
    variance_value = values.var()
    std_dev_value = values.std()

    return {
        "Maxima": max_value,
        "Minima": min_value,
        "Moda": mode_value,
        "Variância": variance_value,
        "Desvio Padrão": std_dev_value
    }
