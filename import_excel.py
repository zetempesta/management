import pandas as pd
from model.mensagem import Mensagem
from model.tipo_propositura import TipoPropositura
from datetime import datetime as dt
from sqlmodel import select
from db.orm import select_table_first, insert
from core.parameters import DATE_FORMAT_PT_BR


df = pd.read_excel("/home/zetempesta/Casa Civil/Mensagens/novas_mensagens.xlsx")

for index, row in df.iterrows():

    numero= row['Número'] if isinstance(row['Número'], int) else None
    ano= row['Ano'] if isinstance(row['Ano'], int) else None
    sigla = row['Proposição'] if isinstance(row['Proposição'], str) else None

    id_tipo = None
    tipo:TipoPropositura
    if sigla:
        statement =  select(TipoPropositura).where(TipoPropositura.sigla==sigla)
        tipo = select_table_first(TipoPropositura,statement=statement) # type: ignore
        id_tipo = tipo.id if tipo else None

    resumo = row['Resumo'] if isinstance(row['Resumo'], str) else None
    protocolo = None
    if isinstance(row['Protocolo'], dt):
        protocolo = row['Protocolo']
    elif  isinstance(row['Protocolo'], str):
        protocolo = dt.strptime(row['Protocolo'], DATE_FORMAT_PT_BR)
    
    leitura = None
    if isinstance(row['Leitura'], dt): 
        leitura = row['Leitura']
    elif  isinstance(row['Leitura'], str):
        leitura = dt.strptime(row['Leitura'], DATE_FORMAT_PT_BR)

    if id_tipo:
        m = Mensagem(numero=numero, ano=ano,resumo=resumo,tipo=id_tipo, data_protocolo=protocolo,do_edicao=None, do_data=None,extra_do=None,norma_gerada=None, sessao_plenaria_leitura=None, propositura=None) # type: ignore
        insert(m)
    
    