import logging
from typing import Any

import requests
from retry import retry

from src.models.chain import SingleChain, AllChains
from src.models.token_balance import WalletBalance, SingleBalance
from src.utils.logging_utils import setup_logger


class DuneBalancesService:
    def __init__(self):
        self._logger = logging.Logger("DuneBalancesService")
        setup_logger(self._logger)

    """
    Service responsible for making API requests to Dune Balances API
    """

    @retry(
        exceptions=requests.HTTPError,
        tries=5,
        delay=0.01,
        max_delay=0.08,
        backoff=2,
        jitter=(-0.001, 0.001),
    )
    def get_wallet_balance(self, wallet: str) -> WalletBalance:
        """
        Makes an API call to Dune Token Balances API
        - Fetches all balances, across all blockchains for a given wallet
        1st try
        2nd try after 0.01
        3rd try after 0.02
        4th try after 0.04
        5th try after 0.08
        """
        url: str = "https://balances.dev.dunetech.io/balance/{wallet}".format(
            wallet=wallet
        )
        self._logger.info(f"Making API call to {url}")
        try:
            response: requests.Response = requests.get(url)
        except requests.HTTPError:
            self._logger.exception(f"Request to {url} failed. Retrying...")
            raise

        response_json: dict[str, Any] = response.json()
        response_balances_json: list[dict[str, Any]] = response_json["balances"]
        single_balances: list[SingleBalance] = [
            SingleBalance.parse_obj(single_dict)
            for single_dict in response_balances_json
        ]
        wallet_balance: WalletBalance = WalletBalance.parse_obj(
            {
                "request_time": response_json["request_time"],
                "response_time": response_json["response_time"],
                "wallet_address": response_json["wallet_address"],
                "balances": single_balances,
            }
        )
        return wallet_balance

    @retry(
        exceptions=requests.HTTPError,
        tries=5,
        delay=0.01,
        max_delay=0.08,
        backoff=2,
        jitter=(-0.001, 0.001),
    )
    def get_wallet_balance_for_blockchain(
        self, wallet: str, blockchain: str
    ) -> WalletBalance:
        """
        Makes an API call to Dune Token Balances API
        - Fetches all balances, for a given blockchain, for a given wallet
        1st try
        2nd try after 0.01
        3rd try after 0.02
        4th try after 0.04
        5th try after 0.08
        """
        url: str = (
            "https://balances.dev.dunetech.io/balance/{blockchain}/{wallet}".format(
                wallet=wallet, blockchain=blockchain
            )
        )
        self._logger.info(f"Making API call to {url}")
        try:
            response: requests.Response = requests.get(url)
        except requests.HTTPError:
            self._logger.exception(f"Request to {url} failed. Retrying...")
            raise

        response_json: dict[str, Any] = response.json()
        response_balances_json: list[dict[str, Any]] = response_json["balances"]
        single_balances: list[SingleBalance] = [
            SingleBalance.parse_obj(single_dict)
            for single_dict in response_balances_json
        ]
        wallet_balance: WalletBalance = WalletBalance.parse_obj(
            {
                "request_time": response_json["request_time"],
                "response_time": response_json["response_time"],
                "wallet_address": response_json["wallet_address"],
                "balances": single_balances,
            }
        )
        return wallet_balance

    @retry(
        exceptions=requests.HTTPError,
        tries=5,
        delay=0.01,
        max_delay=0.08,
        backoff=2,
        jitter=(-0.001, 0.001),
    )
    def get_chains(self) -> AllChains:
        """
        Makes an API call to Dune Token Balances API, to get possible blockchains
        1st try
        2nd try after 0.01
        3rd try after 0.02
        4th try after 0.04
        5th try after 0.08
        """
        url: str = "https://balances.dev.dunetech.io/chains"
        self._logger.info(f"Making API call to {url}")
        try:
            response: requests.Response = requests.get(url)
        except requests.HTTPError:
            self._logger.exception(f"Request to {url} failed. Retrying...")
            raise

        response_json: dict[str, Any] = response.json()
        chains_json: list[dict[str, Any]] = response_json["chains"]
        single_chains: list[SingleChain] = [
            SingleChain.parse_obj(single_dict) for single_dict in chains_json
        ]
        all_chains: AllChains = AllChains.parse_obj({"chains": single_chains})
        return all_chains


if __name__ == "__main__":
    service: DuneBalancesService = DuneBalancesService()
    # ken: str = "0x9d84ce0306f8551e02efef1680475fc0f1dc1344"
    # wallet_balance: WalletBalance = service.get_wallet_balance(ken)
    # print(wallet_balance)
    # blockchain: str = "polygon"
    # wallet_balance_for_polygon: WalletBalance = (
    #     service.get_wallet_balance_for_blockchain(ken, blockchain)
    # )
    # print(wallet_balance_for_polygon)
    all_chains: AllChains = service.get_chains()
    print(all_chains)
