from src.pipeline.utils import src_path, dtypes, custom_dtypes
from src.pipeline.extract import from_csv, stage_csv


def standard_data_process():
    load_config = {"dtype":dtypes, "converters":custom_dtypes, "encoding":'utf-8', "engine":'python', "sep":','}
    df_gen = from_csv(src_path, **load_config)

    staged_config = {"index":False}
    stage_csv(df_gen, **staged_config)

def exceptional_data_process(p1=True, p2=True):
    def p1_2022_pv():
        load_config = {"skipinitialspace":True, "encoding":'unicode_escape', "engine":'python', "sep":';', "skiprows":[3422], "chunksize":30}
        path = src_path / "presidential" / "2022_presidencia_primera_vuelta.csv"
        df_tup = from_csv(path, **load_config)


    def p2_2022_sv():
        load_config = {"skipinitialspace":True, "encoding":'unicode_escape', "engine":'python', "sep":';', "skiprows":[413], "chunksize":30}
        path = src_path / "presidential" / "2022_presidencia_segunda_vuelta.csv"
        df_tup = from_csv(path, **load_config)
    
    if p1:
        p1_2022_pv()
    if p2:
        p2_2022_sv()

# standard_data_process()