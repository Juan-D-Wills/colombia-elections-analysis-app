from typing import Generator, Tuple, Dict, List
import pandas as pd 

def cat_string(
        df_gen:Generator[pd.DataFrame | str], 
        to_cat:list[str] | str,
        sep=' ', 
        new_col='str_concat', 
        replace:Tuple[str,str]=None, 
        strip:str=None, 
        fillna:str=None,
        drop:list[str] | bool=True, 
    ):
    for df_tup in df_gen:
        df, file_name = df_tup

        if fillna:
            df.fillna(fillna, inplace=True)

        df[new_col] = df[to_cat[0]].str.cat(df[to_cat[1:]], sep=sep)

        if replace:
            df[new_col] = df[new_col].str.replace(*replace)

        if strip:
            df[new_col] = df[new_col].str.strip(strip)

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

if "__main__" == __name__:
    pass