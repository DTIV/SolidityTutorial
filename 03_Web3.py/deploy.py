import solcx
import json
from web3 import Web3

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

##################################
######         NETWORK      ######
##################################

#get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#connect to ganache rpc server
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

#network id
chain_id = 1337


address = "0x0266FE1fd54F0AcC16cE48439BC130cB960f695a"


#must add '0x' to private keys in python
#never hardcode private key
private_key = "0x" + config['pk']

#create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

#get nonce - tx count
nonce = w3.eth.getTransactionCount(address)


##################################
######     TRANSACTIONS     ######
##################################

#build transactions
# new addition to original tutorial add gasPrice to your transaction

transaction = SimpleStorage.constructor().buildTransaction({"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from":address, "nonce": nonce})

signed_tx = w3.eth.account.sign_transaction(transaction, private_key)