import pandas as pd
def load_dataset(filepath):

    if filepath.endswith(".csv"):

        return pd.read_csv(
            filepath,
            low_memory=False
        )

    elif filepath.endswith(
        (".xlsx", ".xls")
    ):

        return pd.read_excel(filepath)

    else:

        raise Exception(
            "Unsupported file type"
        )


def detect_target(df):

    binary_cols = []

    for col in df.columns:

        if df[col].nunique() == 2:
            binary_cols.append(col)

    if len(binary_cols) > 0:
        return binary_cols[-1]

    return None


def get_numeric_columns(df, target=None):

    cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    if target in cols:
        cols.remove(target)

    return cols