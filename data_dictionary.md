# Data Dictionary

## fact_nav

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique mutual fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | INTEGER | Transaction amount |
| state | TEXT | Investor state |
| kyc_status | TEXT | Verified/Pending |

---

## fact_performance

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Mutual fund identifier |
| return_1yr_pct | REAL | One-year return |
| return_3yr_pct | REAL | Three-year return |
| sharpe_ratio | REAL | Risk-adjusted return |
| alpha | REAL | Excess return over benchmark |
| beta | REAL | Volatility measure |
| max_drawdown_pct | REAL | Maximum downside loss |