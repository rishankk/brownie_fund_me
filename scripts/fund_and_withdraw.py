from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    # entrance_fee = 1
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    tx = fund_me.fund(
        {
            "from": account,
            "gas_limit": 6721975,
            "value": entrance_fee,
            "allow_revert": True,
        }
    )
    tx.wait(1)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    # fund_me.withdraw({"from": account, 'gas_limit': 6721975})
    tx = fund_me.withdraw({"from": account, "gas_limit": 6721975, "allow_revert": True})
    tx.wait(1)


def main():
    fund()
    withdraw()
