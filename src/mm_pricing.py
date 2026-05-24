"""
mm_pricing.py
─────────────
Money market instrument pricing functions.
Covers T-Bills, Commercial Paper (CP), Certificates of Deposit (CD).
All on discount basis (Act/360).
"""

import pandas as pd
import numpy as np


def tbill_price(face_value: float, discount_rate: float, days: int) -> float:
    """
    Convert T-Bill / CP discount yield to price.
    Price = FV × (1 - d × t)  where t = days/360
    """
    return face_value * (1 - discount_rate * days / 360)


def bond_equivalent_yield(face_value: float, price: float, days: int) -> float:
    """
    Convert discount price to Bond-Equivalent Yield (BEY).
    BEY = (FV - Price) / Price × (365 / days)
    """
    return (face_value - price) / price * (365 / days)


def discount_to_yield(discount_rate: float, days: int) -> float:
    """Convert discount rate to money market yield."""
    return discount_rate / (1 - discount_rate * days / 360)


def price_mm_portfolio(instruments: list[dict]) -> pd.DataFrame:
    """
    Price a portfolio of MM instruments.

    Each instrument dict must contain:
        instrument, type, face_value, discount_rate, days_to_maturity, counterparty
    """
    df = pd.DataFrame(instruments)
    df['price']           = df.apply(
        lambda r: tbill_price(r.face_value, r.discount_rate, r.days_to_maturity), axis=1
    )
    df['discount_amount'] = df['face_value'] - df['price']
    df['bey']             = df.apply(
        lambda r: bond_equivalent_yield(r.face_value, r.price, r.days_to_maturity), axis=1
    )
    df['mm_yield']        = df.apply(
        lambda r: discount_to_yield(r.discount_rate, r.days_to_maturity), axis=1
    )
    return df
