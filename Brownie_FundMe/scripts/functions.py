from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
PRICE = 2000
def get_account():
    if(network.show_active() == 'development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
        
def deploy_mock():
    # DEPLOY MOCK
    print(f"Active network is {network.show_active()}")
    print("Deploying Mock!")
    if(len(MockV3Aggregator) <= 0):
        # only if there are no other deployments deploy another mock
        mock = MockV3Aggregator.deploy(DECIMALS, Web3.toWei(PRICE, "ether"), {"from": get_account()})
        print("Mocks Deployed")