def __convert_to_datetime(tui_timeformat):
    from datetime import datetime

    datetime_tmp = datetime.strptime(tui_timeformat, '%Y-%m-%dT%H:%M:%S')
    return datetime_tmp

def __count_days(date1):
    from datetime import datetime
    date2 = datetime.strptime("2023-01-01 00:00:00", '%Y-%m-%d %H:%M:%S') #should be implemented dynamically, but no time
    time_difference = date2 - date1
    days_difference = abs(time_difference.days)
    return days_difference

def convert_time_columns(df, column_name):
    df[column_name + '_norm'] = df[column_name].apply(__convert_to_datetime)
    df[column_name + '_norm_total_days'] = df[column_name + '_norm'].apply(__count_days)
    return df

def sum_columns(df, column_names_list, sum_column_name):
    df_sum = df[column_names_list].sum(axis=1)
    df[sum_column_name] = df_sum
    return df

def divide_columns(df, column_names_list, divide_column_name):
    import pandas as pd
    df_divide = df[column_names_list[0]].divide(df[column_names_list[1]].replace(0, pd.NA))
    df[divide_column_name] = df_divide
    return df
