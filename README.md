# 🏦 FX Treasury Operations Simulator

> End-to-end treasury desk simulation covering FX spot/forward pricing, Money Market instruments,
> OTC FX forward Mark-to-Market, and daily ops reporting — built with live market data.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juangjuang74-eng/fx-treasury-simulator/blob/main/notebooks/fx_treasury_simulator.ipynb)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![yfinance](https://img.shields.io/badge/yfinance-live%20data-green)
![Plotly](https://img.shields.io/badge/Plotly-dashboard-purple)

---

## 📌 Project Overview

This project simulates workflows used by treasury operations desks at global banks —
covering **FX**, **Money Markets (MM)**, and **OTC Derivatives** — with live market data
pulled via `yfinance` and `FRED API`.

Directly relevant to **Treasury Operations Analyst** roles in securities services and global markets.

---

## 🗂️ Repository Structure

```
fx-treasury-simulator/
│
├── notebooks/
│   └── fx_treasury_simulator.ipynb     ← Main notebook (Google Colab ready)
│
├── src/
│   ├── fx_pricing.py                   ← FX spot/forward pricing functions
│   ├── mm_pricing.py                   ← Money market instrument pricing
│   ├── otc_mtm.py                      ← OTC forward mark-to-market engine
│   └── report.py                       ← Ops summary report generator
│
├── reports/
│   └── treasury_summary_sample.txt     ← Sample daily ops report output
│
├── assets/
│   └── product_reference.md            ← FX/MM/OTC product reference guide
│
├── data/
│   └── sample/
│       └── forward_book_sample.csv     ← Sample OTC forward book input
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Modules Covered

| Module | Description | Key Concept |
|---|---|---|
| **FX Spot** | Live rates via yfinance — EUR/USD, GBP/USD, USD/JPY, AUD/USD | Real-time market data |
| **FX Forward** | Interest Rate Parity pricing across 1M–1Y tenors | Covered IRP: F = S × (1+r_d)/(1+r_f) |
| **Money Markets** | T-Bill, CP, CD — discount yield → price → BEY conversion | Discount basis instruments |
| **SOFR Benchmark** | Risk-free rate from FRED API + portfolio spread | Benchmark vs MM portfolio |
| **OTC Forward MTM** | 6-contract forward book with daily mark-to-market | P&L = notional × (Fwd_current − Fwd_contracted) |
| **Dashboard** | 4-chart interactive Plotly dashboard | Spot/Fwd curve, maturity ladder, MTM bar, SOFR |
| **Excel Report** | Multi-sheet ops report (auto-export) | 5 sheets: FX, Fwd Curve, MM, OTC, SOFR |

---

## 📐 Key Formulas Implemented

```python
# 1. FX Forward Rate (Covered Interest Rate Parity)
Forward = Spot × (1 + r_domestic × days/360) / (1 + r_foreign × days/360)

# 2. Forward Points (Pips)
Pips = (Forward - Spot) × 10,000

# 3. T-Bill Price (Discount Basis)
Price = Face_Value × (1 - Discount_Rate × Days/360)

# 4. Bond-Equivalent Yield
BEY = (Face_Value - Price) / Price × (365 / Days)

# 5. OTC Forward MTM
MTM = Notional × (Forward_Current - Forward_Contracted) / Forward_Current
```

---

## 📊 Dashboard Output

Four interactive Plotly charts:
1. **EUR/USD Spot vs Forward Curve** — 90-day rolling with 1M/3M/6M overlays
2. **MM Portfolio Maturity Ladder** — face value by instrument and days-to-maturity
3. **OTC Forward Book MTM P&L** — per counterparty, green/red with alert threshold
4. **SOFR Rate Trend** — 250-day benchmark with MM portfolio rate overlay

---

## 🚀 How to Run

### Option A — Google Colab (Recommended)
1. Click the **Open in Colab** badge above
2. Runtime → Run all
3. No data download needed — live data pulled automatically

### Option B — Local
```bash
git clone https://github.com/juangjuang74-eng/fx-treasury-simulator.git
cd fx-treasury-simulator
pip install -r requirements.txt
jupyter notebook notebooks/fx_treasury_simulator.ipynb
```

---

## 💼 Relevance to Treasury & Custody Operations

| Project Feature | Real-World Ops Equivalent |
|---|---|
| FX forward pricing (IRP) | Treasury desk FX forward confirmation & valuation |
| Forward points calculation | Daily FX ops reporting — rate vs contracted spread |
| MM discount yield → price | MM ops: pricing T-Bills, CP, CD at settlement |
| BEY vs discount rate | Fixed income ops: yield comparison across instruments |
| OTC MTM calculation | Daily P&L reporting to risk/compliance |
| Alert flag (MTM > $50K) | Threshold-based exception reporting |
| SOFR spread analysis | Benchmark monitoring for MM portfolio |
| Multi-sheet Excel export | Daily ops report for treasury/compliance teams |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![yfinance](https://img.shields.io/badge/yfinance-0.2-green)
![pandas--datareader](https://img.shields.io/badge/pandas--datareader-FRED-orange)
![Plotly](https://img.shields.io/badge/Plotly-5.x-purple)
![openpyxl](https://img.shields.io/badge/openpyxl-Excel-brightgreen)

**Data Sources:**
- `yfinance` — live FX spot rates (Yahoo Finance)
- `FRED API` — SOFR risk-free rate (Federal Reserve)

---

## 📄 License

MIT License
