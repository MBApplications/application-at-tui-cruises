class DataVisualization:

    def __init__(self):
        pass

    @staticmethod
    def plot_x_y(x_values, y_values, *args, **kwargs):
        import plotly.graph_objects as go

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=x_values, y=y_values, mode="lines+markers", name="Line Plot")
        )
        fig.update_layout(
            title="Simple Line Plot Example",
            xaxis_title="X Axis",
            yaxis_title="Y Axis",
        )

        return fig.show()

    @staticmethod
    def map_x_y(df, *args, **kwargs):
        import pandas as pd
        import folium
        import matplotlib.pyplot as plt
        import branca
        import matplotlib
        import matplotlib.pyplot as plt

        cmap = plt.get_cmap("jet", len(df["coordinates"]))
        granularity = 100

        if "cmap" in kwargs.keys():
            cmap = plt.get_cmap(kwargs["cmap"], len(df["coordinates"]))

        if "granularity" in kwargs.keys():
            granularity = kwargs["granularity"]

        if "color_representation" in kwargs.keys():
            color_representation = kwargs["color_representation"]
            max_value = df[color_representation].max()

        map = folium.Map(
            location=[47.00395, -10.40428], tiles="OpenStreetMap", zoom_start=3
        )

        # cmap = plt.get_cmap('jet', len(df['coordinates']))
        hex_colors = [matplotlib.colors.rgb2hex(cmap(i)[:3]) for i in range(cmap.N)]
        for curr_index, curr_value in enumerate(df["coordinates"]):
            if curr_index % granularity == 0:
                # folium.Marker(location=curr_value).add_to(map)
                if curr_index != 0:

                    if "color_representation" in kwargs.keys():
                        color_index_tmp = df[color_representation][curr_index]
                        color_index_tmp2 = round(len(df["coordinates"])*color_index_tmp/max_value)
                        folium.PolyLine(
                            locations=[previous_value, curr_value],
                            color=hex_colors[color_index_tmp2],
                            weight=5,
                            opacity=0.7,
                        ).add_to(map)
                    else:
                        folium.PolyLine(
                            locations=[previous_value, curr_value],
                            color=hex_colors[curr_index],
                            weight=5,
                            opacity=0.7,
                        ).add_to(map)

                previous_value = curr_value

        folium.Marker(location=[curr_value[0], curr_value[1]],
                popup=f"CURRENT POSITION:<br>"
                    f"Lattitude: {curr_value[0]}<br>"
                    f"Longitude: {curr_value[1]}<br>",
                icon=folium.Icon(color='#C154C1')
                ).add_to(map)
        # map.add_child(cmap)
        return map
