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

    def __read_column_description(self):
        import pandas as pd
        
        list_descriptions = []
        with open(self.raw_data_path + "data_description.txt", "r", encoding='utf-8') as file:
            for line in file:
                line_tmp = line.strip()
                line_tmp2 = line_tmp[line_tmp.index("|")+1:].strip()
                list_descriptions.append(line_tmp2)
        return list_descriptions

    def print_rawdata_columns(self):
        import pandas as pd
        df = pd.DataFrame(columns=['column', 'description'])
        column_names = self.read_rawdata().columns.tolist()
        column_description = self.__read_column_description()
        pretty_string = ""
        for curr_index, curr_value in enumerate(column_names):
            new_row = {'column': str(curr_value), 'description': str(column_description[curr_index].strip())}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        return df
