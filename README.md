## Dune Token Balances API (Alpha) Playground
- https://duneanalytics.notion.site/Dune-Token-Balances-API-Alpha-40ec30913bbd43e3b745dc89c1daa342

## Dune Balances API Layer

A simple backend proxy server, that queries the dune analytics API

We can build on top of this, to persist the data in Postgres for easier analytics

### Project Setup

Create virtual environment

```commandline
poetry shell
```

Install dependencies

```commandline
poetry install --no-root
```

### API 1: Get the balances belonging to a wallet address, across all blockchains
- https://balances.dev.dunetech.io/balance/0x9d84ce0306f8551e02efef1680475fc0f1dc1344

Use Case 1: Allows us to see the exact smart contracts a given wallet has money in

Use Case 2: Allows us to see what new smart contracts a whale recently invested in; Get the diff / new contracts from last time we query and now

Use Case 3: Allow us to see how active a wallet / user is on a given blockchain

#### To make an API call to API 1, run the following command

```commandline
PYTHONPATH=. python src/query_wallet_balance.py query-wallet-balance -w "0x9d84ce0306f8551e02efef1680475fc0f1dc1344"
```

### API 2: Same as API 1, but allows you filter for wallets within a blockchain
- https://balances.dev.dunetech.io/balance/polygon/0x9d84ce0306f8551e02efef1680475fc0f1dc1344

We filter for only balances belonging to polygon

Same use case as API 1, just with filtering

Use API 2, if you are only interested in analytics for a dedicated blockchain e.g Polygon

#### To make an API call to API 2, run the following command

```commandline
PYTHONPATH=. python src/query_wallet_balance.py query-wallet-balance-for-blockchain -w "0x9d84ce0306f8551e02efef1680475fc0f1dc1344" -b "polygon"
```

### API 3: Used to get possible blockchains to filter balances for a wallet by; Used for metadata / just to know what blockchains we filter on
- https://balances.dev.dunetech.io/chains

#### To make an API call to API 3, run the following command

```commandline
PYTHONPATH=. python src/query_wallet_balance.py query-blockchains
```

Use Case: More of a metadata query, used in tandom with query 2; Without this API, you won't know the possible blockchains you filter on