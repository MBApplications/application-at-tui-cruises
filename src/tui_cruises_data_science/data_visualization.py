class DataVisualization:

    def __init__(self):
        pass

    def plot_x_y(self, x_values, y_values, *args, **kwargs):
        import plotly.graph_objects as go

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Line Plot'))
        fig.update_layout(
            title='Simple Line Plot Example',
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
        )

        return fig.show()
