import pandas as pd
from openpyxl.styles.builtins import total


class DataPreprocessor:

    @staticmethod
    def get_columns(df):
        print(df.columns)
        return list(df.columns)

    @staticmethod
    def select_column(df,column_name):
        if column_name in df.columns:
            return df[[column_name]]
        else:
            print(f"Column Name {column_name} not available")
            return None


    @staticmethod
    def merge_df(source_df,target_df,column_name):
        if column_name in source_df.columns:
            target_df[column_name] = source_df[column_name]
            return target_df
        else:
            print(f"Column {column_name} Not Found")
            return None


    @staticmethod
    def calculate_total_hours(source_df):
        source_df['check_in'] = pd.to_datetime(source_df['check_in'],format='%H:%M:%S',errors='coerce')
        source_df['check_out'] = pd.to_datetime(source_df['check_out'],format='%H:%M:%S',errors='coerce')

        source_df['total_hours'] = (source_df['check_out'] - source_df['check_in']).dt.total_seconds() / 3600

        return source_df


