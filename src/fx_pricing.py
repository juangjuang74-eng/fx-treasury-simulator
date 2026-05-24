"""
fx_pricing.py
─────────────
FX spot and forward pricing functions.
Based on Covered Interest Rate Parity (CIP).
"""

import pandas as pd
import numpy as np
import yfinance as yf


# Default interest rate assumptions (approximate central bank rates)
DEFAULT_RATES = {
    'USD': 0.053,   # Federal Reserve
    'EUR': 0.040,   # ECB
    'GBP': 0.052,   # Bank of England
    'JPY': 0.001,   # Bank of Japan
    'AUD': 0.043,   # RBA
}

TICKERS = {
    'EUR/USD': 'EURUSD=X',
    'GBP/USD': 'GBPUSD=X',
    'USD/JPY': 'USDJPY=X',
    'AUD/USD': 'AUDUSD=X',
}


def fetch_spot_rates(period: str = '1y', interval: str = '1d') -> pd.DataFrame:
    """Pull live FX spot rates via yfinance."""
    raw = yf.download(list(TICKERS.values()), period=period,
                      interval=interval, auto_adjust=True)
    df = raw['Close'].copy()
    df.columns = list(TICKERS.keys())
    return df.dropna()


def calc_forward_rate(spot: float, r_domestic: float,
                      r_foreign: float, days: int) -> float:
    """
    Calculate FX forward rate using Covered Interest Rate Parity.

    F = S × (1 + r_d × t) / (1 + r_f × t)
    where t = days / 360
    """
    t = days / 360
    return spot * (1 + r_domestic * t) / (1 + r_foreign * t)


def calc_forward_points(spot: float, forward: float) -> float:
    """Calculate forward points (pips)."""
    return (forward - spot) * 10_000


def build_forward_curve(spot: float, r_domestic: float, r_foreign: float,
                        tenors: dict = None) -> pd.DataFrame:
    """
    Build full forward curve for a currency pair.

    Parameters
    ----------
    tenors : dict, optional
        e.g. {'1M': 30, '3M': 90, '6M': 180, '1Y': 360}
    """
    if tenors is None:
        tenors = {'1M': 30, '2M': 60, '3M': 90, '6M': 180, '1Y': 360}

    rows = [{'tenor': 'Spot', 'days': 0, 'rate': spot, 'pips': 0.0}]
    for label, days in tenors.items():
        fwd  = calc_forward_rate(spot, r_domestic, r_foreign, days)
        pips = calc_forward_points(spot, fwd)
        rows.append({'tenor': label, 'days': days, 'rate': fwd, 'pips': pips})

    return pd.DataFrame(rows)
