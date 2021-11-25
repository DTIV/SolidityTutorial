import solcx
import json
from web3 import Web3

'''
https://www.npmjs.com/package/ganache-cli
'''
##################################
######         COMPILE      ######
##################################

# opening simple storage contract
with open("../01_SimpleStorage/SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


with open('../config.json') as f:
    config = json.load(f)

print(config['pk'])

#compile solidity contract
print("Compiling Contract Started")

solcx.install_solc("0.8.0")
compiled_sol = solcx.compile_standard(
    {
        "language" : "Solidity",
        "sources" : { 
            "SimpleStorage.sol" : { 
                "content" : simple_storage_file
            }
        },
        "settings" : {
            "outputSelection" : {
                "*":{
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version = "0.8.0",
)


#output compiled solidity to file, if file does not format on save then use ALT-SHIFT-F
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

print("Compiling Contract Finished")
##################################
######         NETWORK      ######
##################################

#get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#connect to ganache rpc server
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#network id
chain_id = 1337

address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"

#must add '0x' to private keys in Ganche UI
#never hardcode private key
private_key = config['pk']

#create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

#get nonce - tx count
nonce = w3.eth.getTransactionCount(address)

#get gas price
gas_price = w3.eth.gas_price

##################################
######     TRANSACTIONS     ######
##################################

#build transactions
# new addition to original tutorial add gasPrice to your transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId": chain_id, "gasPrice": gas_price, "from":address, "nonce": nonce})

#sign transaction with private key
signed_tx = w3.eth.account.sign_transaction(transaction, private_key)

print("Deploying Contract")
#send tx
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

#wait for confirmation
tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract Deployed!")
##################################
######       CONTRACT       ######
##################################

#working with contract needs ABI and address
simple_storage = w3.eth.contract(address= tx_reciept.contractAddress, abi=abi)
'''
Two different ways to interact with contract functions: Call and Transact
    Call - simulates making the call and getting a return value (dont make state change)
    Transact - makes state changes
'''
#does NOT actually store the value on the contract
call_retrieve = simple_storage.functions.retrieve().call()
call_store = simple_storage.functions.store(15).call()

#will actually store the value set to contract
#nonce can only be used one per tx, so nonce+1

print("Updating Contract", simple_storage.functions.retrieve().call())

store_transaction = simple_storage.functions.store(15).buildTransaction(
    {"chainId":chain_id, "from": address, "nonce": nonce+1, "gasPrice": gas_price}
)

sign_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)

tx_hash = w3.eth.send_raw_transaction(sign_store_tx.rawTransaction)
tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract Updated!", simple_storage.functions.retrieve().call())


'''
now ganache shows contract call aswell as contract creation

intall ganache-cli with: 
    yarn global add ganache-cli
    npm install -g ganache-cli

start ganache-cli by running 'ganache-cli'
to always start with the same accounts run 'ganache-cli --deterministic"
update httpProvider and address
'''
