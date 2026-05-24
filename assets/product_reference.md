# FX / MM / OTC Product Reference Guide

## 1. FX Products

### Spot
- Settlement: T+2 (standard)
- Quote: bid/offer spread
- Used for: immediate currency exchange

### FX Forward
- Settlement: agreed future date (T+3 to T+1Y+)
- Pricing: Covered Interest Rate Parity (CIP)
  - `F = S × (1 + r_d × t) / (1 + r_f × t)`
- Forward Points (Pips): `(F - S) × 10,000`
- Used for: hedging FX exposure, client transactions

### Key Terms
| Term | Definition |
|---|---|
| Spot | Current market exchange rate |
| Forward | Agreed rate for future delivery |
| Pips | 1/10,000 of a currency unit |
| NDF | Non-Deliverable Forward (settled in USD) |
| Swap | Simultaneous spot + forward transaction |

---

## 2. Money Market Instruments

### Treasury Bills (T-Bills)
- Issuer: Government (US Treasury)
- Basis: Discount (Act/360)
- Maturities: 4W, 8W, 13W, 26W, 52W
- Formula: `Price = FV × (1 - d × days/360)`

### Commercial Paper (CP)
- Issuer: Corporate (short-term funding)
- Basis: Discount (Act/360)
- Maturities: 1–270 days
- Higher yield than T-Bills (credit risk)

### Certificate of Deposit (CD)
- Issuer: Bank
- Basis: Add-on (Act/360)
- Maturities: Overnight to 1Y

### Key Yields
| Yield Type | Formula |
|---|---|
| Discount Rate | `d = (FV - P) / FV × 360/days` |
| Bond-Equivalent Yield | `BEY = (FV - P) / P × 365/days` |
| MM Yield | `y = d / (1 - d × days/360)` |

---

## 3. OTC Derivatives

### FX Forward (OTC)
- Bilateral agreement (not exchange-traded)
- Mark-to-Market daily: `MTM = N × (F_current - F_contracted) / F_current`
- Settlement risk: counterparty credit exposure
- Reporting: EMIR / Dodd-Frank (trade reporting required)

### Key Risk Metrics
| Metric | Description |
|---|---|
| MTM P&L | Unrealised gain/loss vs contracted rate |
| DV01 | Dollar value of 1bp rate move |
| Delta | Sensitivity to spot rate change |
| Settlement Risk | Counterparty default before settlement |

---

## 4. Benchmarks

| Benchmark | Region | Replaces |
|---|---|---|
| SOFR | USD | LIBOR USD |
| €STR | EUR | EONIA |
| SONIA | GBP | LIBOR GBP |
| TONAR | JPY | TIBOR |
