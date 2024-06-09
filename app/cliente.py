#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import pandas as pd
import json
from utils import calculate_additional_insights, calculate_median, convert_currency_to_float
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

class Cliente:
    #━━━━━━━━━━━━━━❮Conversão de string para float❯━━━━━━━━━━━━━━

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.dataframe['Valor Monetario'] = self.dataframe['Valor Monetario'].apply(convert_currency_to_float)

    #━━━━━━━━━━━━━━❮Calculos Estatisticos❯━━━━━━━━━━━━━━
    
    def calcular_estatisticas(self):
        estatisticas = {
            "máximo": self.dataframe.max().to_dict(),
            "mínimo": self.dataframe.min().to_dict(),
            "média": self.dataframe.mean().to_dict(),
            "moda": self.dataframe.mode().iloc[0].to_dict(),
            "desvio_padrão": self.dataframe.std().to_dict(),
            "variância": self.dataframe.var().to_dict()
        }
        return estatisticas

    def calcular_mediana(self):
        return calculate_median(self.dataframe['Valor Monetario'])

    def calcular_analises_adicionais(self):
        insights = calculate_additional_insights(self.dataframe['Valor Monetario'])
        return insights

    def converter_para_json(self):
        data_json = self.dataframe.to_dict(orient="records")
        mediana_geral = self.calcular_mediana()
        result = {
            "dados": data_json,
            "mediana_geral": mediana_geral
        }
        return json.dumps(result, ensure_ascii=False)
