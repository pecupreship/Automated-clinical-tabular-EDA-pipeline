import os
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

from sklearn.preprocessing import (
    StandardScaler
)

from sklearn.decomposition import PCA

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from eda.utils import (
    load_dataset,
    detect_target,
    get_numeric_columns
)

from eda.dashboard import (
    create_interactive_scatter
)

os.makedirs(
    "static/figures/",
    exist_ok=True
)

def make_plot(df, title=None):
    size = get_plot_size(df)

    plt.figure(figsize=size, dpi=75)

    if title:
        plt.title(title)

def get_plot_size(df):
    n_rows, n_cols = df.shape

    # Base size
    width = 1
    height = 0.5

    # Scale by dataset size
    if n_rows > 10000:
        height = 3

    if n_rows > 50000:
        height = 3.5

    if n_rows > 100000:
        height = 4

    if n_cols > 20:
        width = 6

    if n_cols > 50:
        width = 8

    return (width, height)

def run_eda(filepath):

    df = load_dataset(filepath)

    # -------------------------
    # SAMPLE LARGE DATASETS
    # -------------------------
    if len(df) > 100000:

        df = df.sample(
            100000,
            random_state=42
        )

    # -------------------------
    # TARGET DETECTION
    # -------------------------
    TARGET = detect_target(df)

    numeric_cols = (
        get_numeric_columns(
            df,
            TARGET
        )
    )

    # -------------------------
    # DATA QUALITY SUMMARY
    # -------------------------
    quality = {

        "rows":
        int(df.shape[0]),

        "columns":
        int(df.shape[1]),

        "duplicates":
        int(
            df.duplicated().sum()
        )
    }

    # -------------------------
    # MISSINGNESS REPORT
    # -------------------------
    make_plot(df,"Missingness")

    msno.matrix(df)

    missing_path = (
        "static/figures/missingness.png"
    )

    plt.savefig(
        missing_path,
        bbox_inches="tight"
    )

    plt.close()

    # -------------------------
    # CORRELATION HEATMAP
    # -------------------------
    heatmap_path = None

    try:

        if len(numeric_cols) > 1:

            make_plot(df,"Correlation Heatmap")

            corr = (
                df[numeric_cols]
                .corr()
            )

            sns.heatmap(
                corr,
                cmap="coolwarm"
            )

            plt.title(
                "Correlation Heatmap"
            )

            heatmap_path = (
                "static/figures/correlation.png"
            )

            plt.savefig(
                heatmap_path,
                bbox_inches="tight"
            )

            plt.close()

    except:
        pass

    # -------------------------
    # PCA VISUALIZATION
    # -------------------------
    pca_path = None

    try:

        if len(numeric_cols) >= 2:

            X = (
                df[numeric_cols]
                .dropna()
            )

            scaler = StandardScaler()

            X_scaled = scaler.fit_transform(X)

            pcs = PCA(
                n_components=2
            ).fit_transform(X_scaled)

            make_plot(df,"PCA Projection")

            plt.scatter(
                pcs[:, 0],
                pcs[:, 1]
            )

            plt.title(
                "PCA Projection"
            )

            pca_path = (
                "static/figures/pca.png"
            )

            plt.savefig(
                pca_path,
                bbox_inches="tight"
            )

            plt.close()

    except:
        pass

    # -------------------------
    # OUTLIER DETECTION
    # -------------------------
    outliers = {}

    for col in numeric_cols:

        try:

            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            count = (
                (
                    (df[col] < lower)
                    |
                    (df[col] > upper)
                )
                .sum()
            )

            outliers[col] = int(count)

        except:
            pass

    # -------------------------
    # FEATURE IMPORTANCE
    # -------------------------
    feature_plot = None

    try:

        if (
            TARGET is not None
            and
            len(numeric_cols) > 0
        ):

            X = (
                df[numeric_cols]
                .fillna(0)
            )

            y = df[TARGET]

            if y.nunique() <= 10:

                model = (
                    RandomForestClassifier(
                        n_estimators=50,
                        max_depth=8,
                        random_state=42
                    )
                )

            else:

                model = (
                    RandomForestRegressor(
                        n_estimators=50,
                        max_depth=8,
                        random_state=42
                    )
                )

            model.fit(X, y)

            importance_df = pd.DataFrame({

                "Feature":
                X.columns,

                "Importance":
                model.feature_importances_

            }).sort_values(

                "Importance",
                ascending=False
            )

            make_plot(df,"Feature importance ")

            sns.barplot(
                data=importance_df,
                x="Importance",
                y="Feature"
            )

            plt.title(
                "Feature Importance"
            )

            feature_plot = (
                "static/figures/feature_importance.png"
            )

            plt.savefig(
                feature_plot,
                bbox_inches="tight"
            )

            plt.close()

    except:
        pass

    # -------------------------
    # INTERACTIVE DASHBOARD
    # -------------------------
    dashboard_html = None

    try:

        dashboard_html = (
            create_interactive_scatter(df)
        )

    except:
        pass

    # -------------------------
    # RETURN RESULTS
    # -------------------------
    return {

        "quality":
        quality,

        "target":
        TARGET,

        "heatmap":
        heatmap_path,

        "missingness":
        missing_path,

        "pca":
        pca_path,

        "dashboard":
        dashboard_html,

        "outliers":
        outliers,

        "feature_plot":
        feature_plot
    }