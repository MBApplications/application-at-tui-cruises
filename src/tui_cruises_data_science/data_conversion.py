def __convert_to_datetime(tui_timeformat):
    from datetime import datetime

    datetime_tmp = datetime.strptime(tui_timeformat, "%Y-%m-%dT%H:%M:%S")
    return datetime_tmp


def __count_days(date1):
    from datetime import datetime

    date2 = datetime.strptime(
        "2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"
    )  # should be implemented dynamically, but no time
    time_difference = date2 - date1
    days_difference = abs(time_difference.days)
    return days_difference


def convert_time_columns(df, column_name):
    df[column_name + "_norm"] = df[column_name].apply(__convert_to_datetime)
    df[column_name + "_norm_total_days"] = df[column_name + "_norm"].apply(__count_days)
    return df


def sum_columns(df, column_names_list, sum_column_name):
    df_sum = df[column_names_list].sum(axis=1)
    df[sum_column_name] = df_sum
    return df


def divide_columns(df, column_names_list, divide_column_name):
    import pandas as pd

    df_divide = df[column_names_list[0]].divide(
        df[column_names_list[1]].replace(0, pd.NA)
    )
    df[divide_column_name] = df_divide
    return df


def __si_multiplication(x, si_conversion_factor):
    return x * si_conversion_factor


def si_conversion(df, source_column_name, si_column_name, si_conversion_factor):
    df[si_column_name] = df.apply(
        lambda row: __si_multiplication(row[source_column_name], si_conversion_factor),
        axis=1,
    )
    return df


def __sliding_window_deque(lst, window_size):
    from collections import deque
    import numpy as np

    d = deque(maxlen=window_size)
    result = []

    for item in lst:
        d.append(item)
        if len(d) == window_size:
            result.append(list(d))

    result_tmp = []
    for curr_value in result:
        result_tmp.append(np.mean(curr_value))
    return result_tmp


def smoothen_data_reduction(df, window_size):
    import pandas as pd

    dict_tmp = {}
    for curr_index, curr_value in enumerate(df.columns):
        result = __sliding_window_deque(df[curr_value], window_size)
        dict_tmp[curr_value] = result

    return pd.DataFrame(dict_tmp)


def get_city_name(latitude, longitude, filename, **kwargs):
    ########################################################
    # # geopy-package: queries seem to be rate-limited !!! #
    ########################################################

    from geopy.geocoders import Nominatim
    from geopy.distance import geodesic
    import os

    data_renew = False
    if "data_renew" in kwargs.keys():
        data_renew = kwargs["data_renew"]

    file_path = "../data/tracked_ports/"

    if os.path.isfile(file_path + filename):
        file_exists = True
    else:
        file_exists = False

    if file_exists and data_renew:
        os.remove(file_path + filename)

    if data_renew:
        print("renewing data")
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse((latitude, longitude), exactly_one=True)

        if location is not None:
            if "city" in location.raw["address"]:
                result = location.raw["address"]["city"]
                with open(file_path + filename, "w") as file:
                    file.write(result)
                return result
            elif "town" in location.raw["address"]:
                result = location.raw["address"]["town"]
                with open(file_path + filename, "w") as file:
                    file.write(result)
                return result
            elif "village" in location.raw["address"]:
                result = location.raw["address"]["village"]
                with open(file_path + filename, "w") as file:
                    file.write(result)
                return result
            elif "suburb" in location.raw["address"]:
                result = location.raw["address"]["suburb"]
                with open(file_path + filename, "w") as file:
                    file.write(result)
                return result

        nearby_locations = []
        for delta_lat in [-0.1, 0, 0.1]:
            for delta_lon in [-0.1, 0, 0.1]:
                new_latitude = latitude + delta_lat
                new_longitude = longitude + delta_lon
                nearby_location = geolocator.reverse(
                    (new_latitude, new_longitude), exactly_one=True
                )
                if nearby_location is not None:
                    nearby_locations.append(nearby_location)

        unique_cities = set()
        for nearby_location in nearby_locations:
            if "city" in nearby_location.raw["address"]:
                unique_cities.add(nearby_location.raw["address"]["city"])
            elif "town" in nearby_location.raw["address"]:
                unique_cities.add(nearby_location.raw["address"]["town"])
            elif "village" in nearby_location.raw["address"]:
                unique_cities.add(nearby_location.raw["address"]["village"])
            elif "suburb" in nearby_location.raw["address"]:
                unique_cities.add(nearby_location.raw["address"]["suburb"])

        if unique_cities:
            result = ", ".join(unique_cities)
            with open(file_path + filename, "w") as file:
                file.write(result)
            return result
        else:
            result = "No nearby locations found"
            with open(file_path + filename, "w") as file:
                file.write(result)
            return result
    elif not data_renew and file_exists:
        with open(file_path + filename, "r") as file:
            result = file.read()
        return result
    else:
        raise FileNotFoundError(f"There is no data available")
