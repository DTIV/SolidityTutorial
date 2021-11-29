from brownie import accounts, config, SimpleStorage, network
import json

# USE 'brownie console' to easily interact with brownie project

def get_account():
    if(network.show_active() == 'development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
        
# 3 ways to add acounts
def deploy_simple_storage(method=1):
    if(method==1):
        # 1. Local Ganache(default) = accounts[0]
        
        account = get_account()
        # always need from
        storage = SimpleStorage.deploy({"from": account})
        # call retrieve function
        store_val = storage.retrieve()
        print(store_val)
        #call store function to update value
        transaction = storage.store(15, {"from": account})
        transaction.wait(1)
        # retrieve updated store value
        updated_val = storage.retrieve()
        print(updated_val)
    elif(method==2):
        #2. testnet/mainnet - set with 'brownie accounts new NAME'
        account = accounts.load("tutorial")
        print("METHOD 2: ", account)
    else:
        #3. from brownie-config.yaml and .env
        account = accounts.add(config['wallets']["from_key"])
        print("METHOD 3", account)
    pass


def main():
    deploy_simple_storage()