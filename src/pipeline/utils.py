from pandas import Int64Dtype
from pathlib import Path
from datetime import datetime

src_path = Path().cwd() / "data" / "raw"
stg_path = src_path.parent / "staged"

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'noviembre', 'Diciembre']
month_dict = {month:str(i) for i, month in enumerate(months, start=1)}
dtypes = {
    "id_electoral":Int64Dtype(),
    "ano":str,
    "tipo_eleccion":str,
    "coddpto":Int64Dtype(),
    "departamento":str,
    "codmpio":Int64Dtype(),
    "municipio":str,
    "circunscripcion":str,
    "codigo_partido":Int64Dtype(),
    "codigo_lista":Int64Dtype(),
    "primer_apellido":str,
    "segundo_apellido":str,
    "nombres":str,
    "votos":Int64Dtype(),
    "curules":Int64Dtype(),
    
}

column_order = ["id_electoral",
    "tipo_eleccion",
    "fecha_elecciones",
    "codigo_departamento",
    "departamento",
    "codigo_municipio",
    "municipio",
    "circunscripcion",
    "codigo_partido",
    "codigo_lista",
    "candidato",
    "votos",
    "curules",
]

column_rename_general ={
    "coddpto":'codigo_departamento',
    "codmpio":'codigo_municipio',
}

column_rename_p_2022 = {
    "CORNOMBRE":"tipo_eleccion",
    "DEP":"codigo_departamento",
    "DEPNOMBRE":"departamento",
    "MUN":"codigo_municipio",
    "MUNNOMBRE":"municipio",
    "CIR":"circunscripcion",
    "PAR":"codigo_partido",
    "CAN":"codigo_lista",
    "CANNOMBRE":"nombres_apellidos",
    "VOTOS":"votos"
}

def month_index(s:str):
    for month, i in month_dict.items():
        r = s.replace(month, i)
        if r != s:
            return r
        
custom_dtypes = {
    "fecha_eleccion": month_index
}

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")