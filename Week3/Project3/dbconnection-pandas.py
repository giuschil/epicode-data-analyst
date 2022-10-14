import pandas
from sqlalchemy import create_engine
import pandas as pd

u = 'root'
p = 'giuschil91'
h = 'localhost'
d = 'ecommerce'

def connect_pandas(u,p,h,d):
    db_connection_str = 'mysql+pymysql://' + u +':'+p+'@'+h+'/'+d
    return db_connection_str

#db_connection_str = 'mysql+pymysql://root:giuschil91@127.0.0.1/ecommerce'
#db_connection = create_engine(db_connection_str)

db_connection = create_engine(connect_pandas(u,p,h,d))
utente = pd.read_sql('prodotto',db_connection)

# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
#pandas.read_sql_table(table_name, con, schema=None, index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None)

help(pd.read_sql())

sql = 'select distinct u.nome,u.cognome from utente u, ordine o where u.uid = o.uid and newsletter = 1;'

tabella_prodotto = pandas.read_sql('prodotto',db_connection)
tabella_orpr01 = pandas.read_sql('orpr01',db_connection)



