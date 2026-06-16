import pandas as pd
from pathlib import Path
from .utils import current_time, stg_path

def from_csv(path:Path, **kwargs):
    if path.is_dir():
        csv_paths = path.rglob('*.csv')
        for csv in csv_paths:
            try:
                yield (pd.read_csv(csv, **kwargs), csv.name)
                
            except Exception as e:
                print("File failed to load:", csv.name, '\nReason:', e)
                continue

    elif path.is_file():
        try:
            if not path.name.endswith('.csv'):
                raise TypeError
            
            return (pd.read_csv(path, **kwargs), path.name) 
        
        except TypeError("Last element of path is not a CSV file") as e:
            print(e, f", got {path.name[:-3]} file type.")
            raise
        
        except Exception as e:
            print("File failed to load:", csv.name, '\nReason:', e)
            raise

def stage_csv(df_gen, **kwargs):
    for df, file_name in df_gen:
        # Join datetime data
        df["fecha"] = df.ano.str.cat(df.fecha_eleccion, sep=' ').str.replace(' ', '-')
        df.drop(columns=['ano', 'fecha_eleccion'], inplace=True)
        
        # Safe to staged folder
        stg_dir = "presidential" if "presidencia" in file_name else "senate"
        df.to_csv(stg_path / stg_dir / f"{file_name[:-4]}_{current_time}.csv", **kwargs)   

if "__main__" == __name__:
    print("Hi There")