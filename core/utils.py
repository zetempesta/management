from calendar import month
from curses.ascii import isdigit
from datetime import date


def only_numbers(text:str)->str:
    retorno=""
    for s in text:
        if isdigit(s):
            retorno += s
    return retorno

def string_to_date(data_string:str)->date:
    year = int(data_string.split("/")[2] )
    month = int(data_string.split("/")[1] )
    day = int(data_string.split("/")[0] )
    retorno = date(year=year, month=month,day=day)

    return retorno
