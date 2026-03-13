from pathlib import Path

from src.variance_analysis import calculate_variance, load_data, summarize_by_department


def test_variance_columns_and_summary() -> None:
    root = Path(__file__).resolve().parents[1]
    df = load_data(root / "data" / "budget_actuals.csv")
    variance_df = calculate_variance(df)
    summary = summarize_by_department(variance_df)

    assert "variance_amount" in variance_df.columns
    assert "variance_pct" in variance_df.columns
    assert not summary.empty
