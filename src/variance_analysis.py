from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def calculate_variance(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["variance_amount"] = out["actual_amount"] - out["budget_amount"]
    out["variance_pct"] = (out["variance_amount"] / out["budget_amount"]) * 100
    return out


def summarize_by_department(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["month", "department"], as_index=False)
        .agg(
            budget_amount=("budget_amount", "sum"),
            actual_amount=("actual_amount", "sum"),
            variance_amount=("variance_amount", "sum"),
        )
        .sort_values(["month", "variance_amount"], ascending=[True, False])
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_path = root / "data" / "budget_actuals.csv"

    df = load_data(data_path)
    variance_df = calculate_variance(df)
    summary = summarize_by_department(variance_df)

    top_over = variance_df.sort_values("variance_amount", ascending=False).head(3)
    top_under = variance_df.sort_values("variance_amount", ascending=True).head(3)

    print("=== Department Monthly Variance Summary ===")
    print(summary.to_string(index=False))
    print("\n=== Top 3 Over-Budget Lines ===")
    print(top_over[["month", "department", "account", "variance_amount", "variance_pct"]].to_string(index=False))
    print("\n=== Top 3 Under-Budget Lines ===")
    print(top_under[["month", "department", "account", "variance_amount", "variance_pct"]].to_string(index=False))


if __name__ == "__main__":
    main()
