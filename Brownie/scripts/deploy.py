from brownie import accounts
import json

with open('../config.json') as f:
    config = json.load(f)

# 3 ways to add acounts
def deploy_simple_storage(method=3):
    if(method==1):
        #Local Ganache
        account = accounts[0]
        print(account)
    elif(method==2):
        # Metamask - set with 'brownie accounts new NAME'
        account = accounts.load("tutorial")
        print("METHOD 2: ", account)
    else:
        account = accounts.add(config['pk'])
        print("METHOD 3", account)
    pass

def main():
    deploy_simple_storage()