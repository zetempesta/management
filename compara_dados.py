from datetime import date, datetime
import pandas as pd
from sqlalchemy import Null
from sqlmodel import select
from model.mensagem import Mensagem
from core.utils import string_to_date
from db.orm import select_table

df_xlsx = pd.read_excel("/home/zetempesta/Casa Civil/Mensagens/novas_mensagens.xlsx")


def converte_para_datetime(entrada)->date:
    retorno:date
    
    if isinstance(entrada, str):
        return string_to_date(entrada)
    else:
        v:datetime
        v=entrada
        return v.date()


m:Mensagem
sql = select(Mensagem).where(Mensagem.data_leitura != None).order_by(Mensagem.ano, Mensagem.numero) # type: ignore
for m in select_table(Mensagem,sql):
    encontrou = False
    
    for index, row in df_xlsx.iterrows():
        numero = int(row["Número"])
        ano = int(row["Ano"])
        leitura = row["Leitura"]
      
        if ( numero == m.numero) and (ano == m.ano):
            encontrou = True

            if m.data_leitura != converte_para_datetime(leitura):
                print(f"""Diferente - Número: {numero} - Ano: {ano} - DataXLS: {leitura}  - DataBD: {m.data_leitura}""")
            