# Aave V2 Wallet Credit Score Model

This project makes a machine learning pipeline that gives credit scores to wallets that use the Aave V2 protocol. The model uses historical transaction data from the blockchain to give each wallet a credit score between 0 and 1000, which shows how risky the wallet is. The more responsible the wallet behavior is, the higher the score.



Based on past transaction data, we need to:

- Create wallet-level features from raw transaction logs, such as deposits, loans, repayments, and liquidations.
- Use transaction behavior to make a scoring model.
- Make the result fit into a "credit score range of 0–1000."


## Set of Data

- Source: Aave V2 Protocol (Polygon network)
- Format: JSON (about 87MB), with one record for each transaction
- Fields: `userWallet`, `action`, `timestamp`, `amount`, `assetPriceUSD`, `actionData`, and so on.

Each transaction stands for actions like: - "deposit"
- "borrow" - "repay"
- "redeemunderlying"
- "liquidationcall"

  ## Feature Engineering

Features extracted per wallet:

- Total number of transactions
- Count of deposits, borrows, repayments, liquidations
- USD value deposited, borrowed, repaid
- Transaction activity span (days)
- Frequency of liquidations (risk signal)

## Model Architecture

- **Model**: RandomForestRegressor (unsupervised simulation of scoring)
- **Scoring Logic**: Model trained to regress aggregate wallet behavior → raw score
- **Normalization**: Scores scaled to range [0–1000] using `MinMaxScaler`
