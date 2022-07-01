import pandas as pd


class DataCleaner:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def remove_nulls(self) -> pd.DataFrame:
        return self.df.dropna()

    def remove_duplicates(self) -> pd.DataFrame:
        remove = self.df[self.df.duplicated()].index
        return self.df.drop(index=remove, inplace=True)
