# Credit Score Analysis: Aave Wallets

## Score Distribution (0–1000)

A histogram of the credit scores reveals a fairly continuous distribution from low-risk to high-risk users.

- **Mean Score**: ~490
- **Median Score**: ~480
- **Min Score**: 0
- **Max Score**: 1000

Wallets are assigned scores using a linear transformation of the model's predicted "user responsibility" metric.

---

## Range-Based Summary

| Score Range | Description                              | Behavior Pattern                                        |
|-------------|------------------------------------------|----------------------------------------------------------|
| 0–200       |  Very risky                             | Frequent liquidations, high borrowing, low repayment     |
| 201–400     |  Caution advised                        | More borrowing than repaying, little deposit activity     |
| 401–600     |  Average / Neutral                      | Balanced usage, some repayment, moderate activity        |
| 601–800     |  Trusted                                | Strong deposit behavior, low risk of default             |
| 801–1000    |  Highly reliable                        | Consistent depositor, full repayment, no liquidations    |

---

## Key Observations

- High scorers had **no liquidations**, strong **repayment patterns**, and long activity spans.
- Low scorers often interacted only to **borrow**, with **minimal repayment or deposits**, and high **liquidation activity**.
- The model shows good separation between behavior clusters without being overly skewed.

---

## Visualizations

### Histogram
![Histogram]([Screenshot 2025-07-15 174921.png](https://github.com/Ayush-shaw27/-Aave-credit-score/blob/main/Screenshot%202025-07-15%20174921.png))

- Shows smooth score distribution.
- Red line = Mean, Green line = Median.

---

## Improvements for Future Work

- Incorporate external wallet behavior (e.g. from other protocols)
- Factor in volatility or asset risk
- Track wallet-to-wallet interactions (sybil or bot detection)

---

## Conclusion

The final scoring model distributes scores evenly and provides a reliable way to assess DeFi wallet risk using Aave V2 data. This method is extensible, explainable, and avoids black-box pitfalls common in ML systems.

