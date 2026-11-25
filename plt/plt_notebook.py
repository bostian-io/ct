import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import marimo as mo

    messy = pd.DataFrame({
        "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                    "Widget A", " Widget C", "Widget D", None, "Widget A"],
        "sales": ["150", "200", "175", "300", "200",
                  "180", "250", "abc", "100", "-50"],
        "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
                 "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
        "region": ["North", "South", "north", "East", "South",
                   "West", "east", "North", "South", "West"],
    })

    df = pd.DataFrame(messy)

    print("=== Raw Data ===")
    print(df)
    # print(f"\nShape: {df.shape}")
    print(f"\nTypes: \n{df.dtypes}")
    # print(f"\nMissing values:\n{df.isnull().sum()}")

    # standardize names
    df["product"] = df["product"].str.strip()
    df["product"] = df["product"].str.title()

    df["region"] = df["region"].str.strip()
    df["region"] = df["region"].str.title()

    # convert types
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # handle missing and invalid values

    df = df.dropna(subset=["product"])

    df.loc[df["sales"] < 0, "sales"] = pd.NA
    df = df.dropna(subset=["sales"])

    print("\n=== Clean Data ===")
    print(df)
    print(f"\nTypes: \n{df.dtypes}")
    return df, mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > split up the sections here so that we're editing the plots below
    """)
    return


@app.cell
def _(df, plt):
    # plots
    fig, axes = plt.subplots(1, 3, figsize=(15,5))

    # Chart 1: Total sales by product (bar)
    sales_totals = df.groupby("product")["sales"].sum()
    axes[0].bar(sales_totals.index, sales_totals.values, color="steelblue", edgecolor="black")
    axes[0].set_title("Total Sales by Product")
    axes[0].set_ylabel("Total Sales ($)")
    axes[0].set_xlabel("Products")

    # Chart 2: Daily Trend (line/plot)
    daily_sales_totals = df.groupby("date")["sales"].sum()
    axes[1].plot(daily_sales_totals.index, daily_sales_totals.values, color="steelblue")
    axes[1].set_title("Daily Sales Trend Line")
    axes[1].set_ylabel("Total Sales ($)")
    axes[1].set_xlabel("Date")

    # Chart 3: Sales Distribution (histogram)
    axes[2].hist(df["sales"], bins=8, color="steelblue", edgecolor="black")
    axes[2].set_title("Sales Distribution")
    axes[2].set_xlabel("Sale Amount ($)")
    axes[2].set_ylabel("Number of Sales")

    # save and show figures
    plt.tight_layout()
    # plt.savefig("multi-panel.png")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
