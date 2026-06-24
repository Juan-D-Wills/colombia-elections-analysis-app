import pandas as pd
from pathlib import Path
from typing import Generator, Tuple

def from_csv(path:Path, **kwargs) -> Generator[Tuple[pd.DataFrame | str], Tuple[pd.DataFrame | str], Tuple[pd.DataFrame | str]]:
    if path.is_dir():
        csv_paths = path.rglob('*.csv')
        for csv in csv_paths:
            try:
                yield (pd.read_csv(csv, **kwargs), csv.name)
            except Exception as e:
                print("File failed to load:", csv.name, '\nReason:', e)
                continue

    if path.is_file() and path.name.endswith('.csv'):
        try:       
            df = pd.read_csv(path, **kwargs)
            if "chunksize" in kwargs.keys():
                yield (df.get_chunk(), path.name) 
            yield (df, path.name)
        
        except Exception as e:
            print("File failed to load:", csv.name, '\nReason:', e)
            raise

if "__main__" == __name__:
    pass
    # print((Path().cwd() / "data" / "raw").is_dir())