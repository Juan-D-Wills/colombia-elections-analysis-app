from typing import Generator, Tuple, Dict, List
import pandas as pd 

def cat_string(
        df_gen:Generator[pd.DataFrame | str], 
        to_cat:list[str] | str,
        sep=' ', 
        col_name='str_concat', 
        replace:Tuple[str,str]=None, 
        strip:str=None, 
        fillna:str=None,
        drop:list[str] | bool=True, 
    ):
    for df_tup in df_gen:
        df, file_name = df_tup

        if fillna:
            df.fillna(fillna, inplace=True)

        df[col_name] = df[to_cat[0]].str.cat(df[to_cat[1:]], sep=sep)

        if replace:
            df[col_name] = df[col_name].str.replace(*replace)

        if strip:
            df[col_name] = df[col_name].str.strip(strip)

        if drop:
            df.drop(columns=to_cat if isinstance(drop, bool) else drop, inplace=True)

        yield df, file_name
 
def column_manipulation(df_gen, order:List[str]=None, rename=None):
    for df_tup in df_gen:
        df, filename = df_tup
        if rename:
            df = df.rename(columns=rename)

        if order:
            df = df.reindex(columns=order)

        yield df, filename

def add_columns(df_gen, col_name='new_column', data=None):
    for df_tup in df_gen:
        df, filename = df_tup
        if col_name in df:
            print("Column name already present in dataframe")
            yield (df, filename)
        else:
            df[col_name] = data
            yield (df, filename)


if "__main__" == __name__:
    pass