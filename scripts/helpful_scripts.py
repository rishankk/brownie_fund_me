from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "maninnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache-local1"]

DECIMALS = 8
Starting_value = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"active network is {network.show_active()}")
    print("deploying mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Starting_value, {"from": get_account()})
    print("mocks deployed")
