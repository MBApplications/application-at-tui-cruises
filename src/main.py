from tui_cruises_data_science import RawDataReader


if __name__ == "__main__":
    # import data
    raw_data_obj1 = RawDataReader()
    # print(raw_data_obj1.read_rawdata())
    print(raw_data_obj1.get_rawdata_columns())
