from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.functions import deploy_mock, get_account

def deploy_fund_me():
    account = get_account()
    if(network.show_active() != "development"):
        price_feed_address = config['netoworks']['rinkeby']['eth_usd_price_feed']
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    # publish to etherscan using publish_source, set in brownie-config
    # pass price feed address before from address
    fund_me = FundMe.deploy(price_feed_address,{"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    pass

def main():
    deploy_fund_me()