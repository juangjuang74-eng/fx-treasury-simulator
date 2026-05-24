"""
otc_mtm.py
──────────
OTC FX Forward book Mark-to-Market engine.
Calculates daily MTM P&L per contract vs contracted rate.
"""

import pandas as pd
from src.fx_pricing import calc_forward_rate


ALERT_THRESHOLD_USD = 50_000   # Flag contracts with |MTM| > this value


def calc_contract_mtm(notional: float, direction: str,
                      contracted_rate: float, current_fwd: float) -> float:
    """
    Calculate MTM P&L for a single FX forward contract.

    BUY  contract: bank gains when forward rises above contracted rate
    SELL contract: bank gains when forward falls below contracted rate
    """
    if direction.upper() == 'BUY':
        mtm = notional * (current_fwd - contracted_rate) / current_fwd
    else:
        mtm = notional * (contracted_rate - current_fwd) / current_fwd
    return round(mtm, 2)


def mark_to_market_book(forward_book: pd.DataFrame,
                        latest_spots: dict,
                        r_domestic: float = 0.053,
                        rates_foreign: dict = None) -> pd.DataFrame:
    """
    Mark-to-market an entire OTC forward book.

    Parameters
    ----------
    forward_book : pd.DataFrame
        Must contain: counterparty, pair, direction, notional_usd,
                      contracted_rate, days_remaining, r_foreign
    latest_spots : dict
        e.g. {'EUR/USD': 1.085, 'GBP/USD': 1.265, ...}
    """
    df = forward_book.copy()

    df['current_spot'] = df['pair'].map(latest_spots)
    df['current_fwd']  = df.apply(
        lambda r: round(calc_forward_rate(
            latest_spots.get(r['pair'], r['contracted_rate']),
            r_domestic, r.get('r_foreign', 0.04), r['days_remaining']
        ), 4), axis=1
    )
    df['mtm_pnl_usd']  = df.apply(
        lambda r: calc_contract_mtm(
            r['notional_usd'], r['direction'],
            r['contracted_rate'], r['current_fwd']
        ), axis=1
    )
    df['mtm_status']   = df['mtm_pnl_usd'].apply(
        lambda x: 'GAIN' if x > 0 else 'LOSS'
    )
    df['alert']        = df['mtm_pnl_usd'].apply(
        lambda x: 'REVIEW' if abs(x) > ALERT_THRESHOLD_USD else ''
    )
    return df


def book_summary(df: pd.DataFrame) -> dict:
    """Return summary statistics for a marked-to-market forward book."""
    return {
        'total_contracts' : len(df),
        'total_notional'  : df['notional_usd'].sum(),
        'net_mtm'         : df['mtm_pnl_usd'].sum(),
        'gross_gain'      : df[df['mtm_pnl_usd'] > 0]['mtm_pnl_usd'].sum(),
        'gross_loss'      : df[df['mtm_pnl_usd'] < 0]['mtm_pnl_usd'].sum(),
        'contracts_gain'  : (df['mtm_pnl_usd'] > 0).sum(),
        'contracts_loss'  : (df['mtm_pnl_usd'] < 0).sum(),
        'alerts'          : (df['alert'] != '').sum(),
    }
