import click

from src.services.dune_balances_service import DuneBalancesService

SERVICE: DuneBalancesService = DuneBalancesService()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--wallet", "-w", type=str)
def query_wallet_balance(wallet: str) -> None:
    result = SERVICE.get_wallet_balance(wallet)
    print(result)


@cli.command()
@click.option("--wallet", "-w", type=str)
@click.option("--blockchain", "-b", type=str)
def query_wallet_balance_for_blockchain(wallet: str, blockchain: str) -> None:
    result = SERVICE.get_wallet_balance_for_blockchain(wallet, blockchain)
    print(result)


@cli.command()
def query_blockchains() -> None:
    result = SERVICE.get_chains()
    print(result)


if __name__ == "__main__":
    cli()
