import duckdb as dk
from pprint import pprint

def select_5():
    with dk.connect() as con:
        path = con.read_csv("/home/juan-wills/Documents/colombia-elections-analysis-app/data/presidential/2006_presidencia.csv")
        pprint(con.query(f'SELECT * FROM  path LIMIT 5').df())
        
def get_settings(max_rows= 5):
    with dk.connect() as con:
        con.query("SELECT * FROM duckdb_settings()").show(max_rows=max_rows)

get_settings()
select_5()