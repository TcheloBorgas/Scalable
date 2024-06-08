import numpy as np
import pandas as pd
import re


def calculate_median(values):
    try:
        return np.median(values.astype(float))  # Assegura que os valores são floats
    except ValueError:
        return "Erro: Dados inválidos."


def convert_currency_to_float(value):
    """Converte valor monetário de string para float."""
    cleaned_value = re.sub(r'[^\d,]', '', value)  # Remove tudo exceto dígitos e vírgulas
    return float(cleaned_value.replace(',', '.'))

def reformat_to_currency(value):
    """Reverte o valor float para o formato de moeda string com R$."""
    return f"R$ {value:,.2f}".replace(',', 'x').replace('.', ',').replace('x', '.')


def calculate_additional_insights(values):
    max_value = values.max()
    min_value = values.min()
    mode_value = values.mode().iloc[0] if not values.mode().empty else None
    variance_value = values.var()
    std_dev_value = values.std()

    return {
        "maxima": max_value,
        "minima": min_value,
        "moda": mode_value,
        "variancia": variance_value,
        "desvio_padrao": std_dev_value
    }
