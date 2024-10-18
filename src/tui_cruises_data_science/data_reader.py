class RawDataReader:

    def __init__(self):
        from dotenv import load_dotenv
        import os

        load_dotenv()
        self.raw_data_path = os.getenv("raw_data_path")

    def internal_vars(self):
        return self

    def read_rawdata(self):
        import pandas as pd

        df = pd.read_csv(self.raw_data_path + "data.csv")
        return df
    
    def get_rawdata_columns(self):
        return self.read_rawdata().columns