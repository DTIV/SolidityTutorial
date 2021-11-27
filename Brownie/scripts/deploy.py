from brownie import accounts, config, SimpleStorage
import json

# 3 ways to add acounts
def deploy_simple_storage(method=1):
    if(method==1):
        #Local Ganache
        account = accounts[0]
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
        # Metamask - set with 'brownie accounts new NAME'
        account = accounts.load("tutorial")
        print("METHOD 2: ", account)
    else:
        #from brownie-config.yaml and .env
        account = accounts.add(config['wallets']["from_key"])
        print("METHOD 3", account)
    pass

def main():
    deploy_simple_storage()