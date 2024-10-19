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
    
    def print_rawdata_columns(self):
        column_names = self.read_rawdata().columns.tolist()
        pretty_string = ""
        list_groups =["Power Galley"]
        for curr_index, curr_value in enumerate(column_names):
            for curr_value2 in list_groups:
                # if curr_value.find(curr_value2) > -1:
                pretty_string += curr_value + "\n"
            # if len(curr_index) % 100 == 0:
            #     pretty_count = 1
            #     pretty_string += "\n"
        print(pretty_string)