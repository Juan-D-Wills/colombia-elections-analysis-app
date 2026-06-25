from .utils import stg_path
import shutil as sh


def stage_csv(df_gen, flush_current=False, **kwargs):
    if flush_current:
        for stg_dir in ('presidential', 'senate'):
            stg_rel_path = stg_path / stg_dir
            sh.rmtree(stg_rel_path)
            stg_rel_path.mkdir()

    for df_tup in df_gen:
        df, file_name = df_tup
        stg_dir = "presidential" if "presidencia" in file_name else "senate"
        df.to_csv(stg_path / stg_dir / f"{file_name[:4]}_{stg_dir}.csv", **kwargs)

if "__main__" == __name__:
    pass