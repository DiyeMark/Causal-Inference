import pandas as pd


class DataCleaner:
    def __init__(self) -> None:
        pass

    def remove_unwanted_columns(self,  df: pd.DataFrame, columns: list) -> pd.DataFrame:
        df.drop(columns, axis=1, inplace=True)
        return df

    def remove_nulls(self,  df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna()

    def remove_duplicates(self,  df: pd.DataFrame) -> pd.DataFrame:
        remove = df[df.duplicated()].index
        return df.drop(index=remove, inplace=True)

    def missing_percentage(self, df: pd.DataFrame):
        percent_missing = df.isnull().sum() * 100 / len(df)
        missing_value_df = pd.DataFrame(
            {"column_name": df.columns, "percent_missing": percent_missing}
        )
        missing_value_df.reset_index(drop=True, inplace=True)
        return missing_value_df

