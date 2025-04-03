from pandas import DataFrame, read_table


class Base():
    _df: DataFrame

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    
    def __init__(self) -> None:
        self._df = None
        super().__init__()

    def read(self, path: str) -> None:
        df = read_table(path, encoding="ansi")
        self._df = self._fill(df)

    def _fill(self, df: DataFrame) -> DataFrame:
        df = df.fillna(0)
        df[["celular_solic", "tel_trab_solic", "tel_solicitante"]]=df[["celular_solic", "tel_trab_solic", "tel_solicitante"]].astype(int)
        return df

    def getInfo(self, process: int) -> DataFrame:
        return self._df.loc[self._df.cod_processo == process]

    def getData(self) -> DataFrame:
        return self._df



