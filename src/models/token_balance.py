from pydantic import BaseModel


class SingleBalance(BaseModel):
    """
    Represents a single Balance belonging to a wallet
    """

    chain: str
    address: str
    amount: str
    symbol: str | None = None
    decimals: int | None = None
    price_usd: float | None = None
    value_usd: float | None = None


class WalletBalance(BaseModel):
    """
    Represents response from Token Balance API
    Represents the balances for a given wallet, e.g Ken from Polymarket
    """

    request_time: str
    response_time: str
    wallet_address: str
    balances: list[SingleBalance]
