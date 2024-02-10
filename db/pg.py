
from sqlalchemy import  create_engine, text
from sqlalchemy.engine import URL
from db.db_conf import database, host, password, port, user


url_object = URL.create(
                    "postgresql+psycopg2",
                    username=user,
                    password=password,
                    host=host,
                    database=database,
                    port=int(port)
                )

engine = create_engine(url=url_object)

def truncate_table(table_name:str):
    sql = f"""truncate table {table_name}"""
    conn = engine.connect()
    conn.execute(text(sql))
    conn.commit()


engine.dispose()