from brownie import accounts

# 3 ways to add acounts
def deploy_simple_storage(method=1):
    #Local account setting
    if(method==1):
        account = accounts[0]
        print(account)
    elif(method==2):
        print("METHOD 2")
    else:
        print("METHOD 3")
    pass

def main():
    deploy_simple_storage()