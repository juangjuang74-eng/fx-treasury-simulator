"""
report.py
─────────
Daily treasury operations summary report generator.
"""

import pandas as pd
from datetime import date


def print_daily_report(latest_spots: dict, fwd_curve: pd.DataFrame,
                       mm_portfolio: pd.DataFrame, otc_summary: dict,
                       sofr_latest: float) -> None:
    """Print formatted daily treasury ops summary report."""

    mm_avg_rate  = float(mm_portfolio['discount_rate'].mean() * 100)
    sofr_pct     = float(sofr_latest)
    spread_bps   = (mm_avg_rate - sofr_pct) * 100

    print('=' * 65)
    print('         FX TREASURY OPERATIONS — DAILY SUMMARY REPORT')
    print(f'         Report Date : {date.today()}')
    print('=' * 65)

    print('\n[1] FX SPOT RATES')
    for pair, rate in latest_spots.items():
        print(f'    {pair:<10}: {rate:.4f}')

    print('\n[2] EUR/USD FORWARD CURVE')
    print(f'    {"Tenor":<8} {"Rate":>8} {"Pips":>8}')
    for _, row in fwd_curve.iterrows():
        print(f'    {row["tenor"]:<8} {row["rate"]:>8.4f} {row["pips"]:>+8.1f}')

    print('\n[3] MONEY MARKET PORTFOLIO')
    print(f'    Total Face Value  : ${mm_portfolio["face_value"].sum():>15,.0f}')
    print(f'    Total Price       : ${mm_portfolio["price"].sum():>15,.2f}')
    print(f'    Total Discount    : ${mm_portfolio["discount_amount"].sum():>15,.2f}')
    print(f'    Avg Discount Rate : {mm_portfolio["discount_rate"].mean():.3%}')
    print(f'    Avg BEY           : {mm_portfolio["bey"].mean():.3%}')

    print('\n[4] OTC FORWARD BOOK')
    print(f'    Active Contracts  : {otc_summary["total_contracts"]}')
    print(f'    Total Notional    : ${otc_summary["total_notional"]:>15,.0f}')
    print(f'    Net MTM P&L       : ${otc_summary["net_mtm"]:>15,.2f}')
    print(f'    Contracts in Gain : {otc_summary["contracts_gain"]}')
    print(f'    Contracts in Loss : {otc_summary["contracts_loss"]}')
    print(f'    Alerts (>$50K)    : {otc_summary["alerts"]}')

    print('\n[5] SOFR BENCHMARK')
    print(f'    SOFR (latest)     : {sofr_pct:.3f}%')
    print(f'    MM Portfolio Rate : {mm_avg_rate:.3f}%')
    print(f'    Spread vs SOFR    : {spread_bps:+.1f} bps')

    print('\n' + '=' * 65)
    print('✅ Report complete.')
