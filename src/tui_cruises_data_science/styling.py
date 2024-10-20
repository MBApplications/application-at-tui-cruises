# @staticmethod
def styling(df):
    import pandas as pd
    from IPython.display import display

    styled_df = df.style.set_table_attributes('style="width: 90%; margin: auto; text-align: center;"') \
                        .set_table_styles([{
                            'selector': 'th',
                            'props': [('text-align', 'left')]
                        }, {
                            'selector': 'td',
                            'props': [('text-align', 'left')]
                        }])
    return styled_df