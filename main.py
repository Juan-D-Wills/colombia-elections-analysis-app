from src.pipeline.utils import src_path, dtypes, custom_dtypes, column_order, column_rename_general, current_time
from src.pipeline.extract import from_csv
import src.pipeline.transform as trans
from src.pipeline.load import stage_csv


def standard_data_process():
    print("Pipeline process started")
    
    # Load data from csv files on local filesystem
    load_config = {"dtype":dtypes, "converters":custom_dtypes, "encoding":'utf-8', "engine":'python', "sep":','}
    df_gen = from_csv(src_path, **load_config)

    # Join candidate names
    t1_gen = trans.cat_string(
         df_gen,
         ['nombres', 'primer_apellido'],# Safe to staged folder
                col_name='candidato', 
                fillna={'nombres':' ', 'segundo_apellido':' '},
                strip=' .', 
                drop=['nombres', 'primer_apellido', 'segundo_apellido']
            )

   # Join datetime strings
    t2_gen = trans.cat_string(
         t1_gen,
         ['ano', 'fecha_eleccion'],
                replace=(' ', '-'),
                col_name='fecha_elecciones'
            )
    
    # Reorder columns for schema compatibility
    t3_gen = trans.column_manipulation(t2_gen, rename=column_rename_general, order=column_order)
    
    # Add table creation info
    t4_gen = trans.add_columns(t3_gen, col_name='created_at', data=current_time)

    # Save to staged dir
    staged_config = {"index":False}
    stage_csv(t4_gen, flush_current=True, **staged_config)

    print("Pipeline process compleated successfully!")


def exceptional_data_process(p1=True, p2=False):
    def p1_2022_pv():
        load_config = {"skipinitialspace":True, "encoding":'unicode_escape', "engine":'python', "sep":';', "skiprows":[3422], "chunksize":30}
        path = src_path / "presidential" / "2022_presidencia_primera_vuelta.csv"
        
        df_gen = from_csv(path, **load_config)
        df, name = next(df_gen)

        # Rename columns
        original_columns = list(column_rename_p_2022.keys())
        print(df.loc[:, original_columns].rename(columns=column_rename_p_2022).head())

        # Create missing columns
        df["fecha"] = "2022-5-29"
        # df["primer_apellido"] = df.
        # df["segundo_apellido"] =
        # df["nombres"] =
        # df.group_by([])

    def p2_2022_sv():
        load_config = {"skipinitialspace":True, "encoding":'unicode_escape', "engine":'python', "sep":';', "skiprows":[413], "chunksize":30}
        path = src_path / "presidential" / "2022_presidencia_segunda_vuelta.csv"
        
        df, output_name = from_csv(path, **load_config)
    
    if p1:
        p1_2022_pv()
    if p2:
        p2_2022_sv()


if "__main__" == __name__:
    standard_data_process()

    # import pandas as pd
    # l= pd.DataFrame({'hi':[1,2], 'there':[3,4]})
    # l['baby'] = 3
    # print(l)
    # exceptional_data_process()
