import plotly.express as px


def create_interactive_scatter(df):

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    if len(numeric_cols) < 2:
        return None

    fig = px.scatter(
        df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        title="Interactive Dashboard"
    )

    return fig.to_html(
        full_html=False
    )