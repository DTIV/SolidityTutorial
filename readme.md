# Solidity Tutorials
--------------------

This is my follow along from multiple solidity tutorials.

Info
------
CTRL+Shift+P > 'keyboard shortcuts'
VS KeyBoard Shortcuts:[here](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

- settings > 'python formatting' > 'python>formatting: black'

-pip install py-solc-x (more actively maintained than py-solc)

## 1. Simple Storage.
----
- basic set and retrieve contract 
- storage factory contract to create muliple simple storage contracts for different users.

## 2. Fund Me
---
- a contract that can get funding over a specific amount.

## 3. Web3.py
---
1. Deploy Simple Storage with Python
    - pip install black

    In VS Code,

## Brownie
----

- Interact with SimpleStorage using brownie framework
### Commands
    - init               Initialize a new brownie project
    - bake               Initialize from a brownie-mix template
    - pm                 Install and manage external packages
    - compile            Compile the contract source files
    - console            Load the console
    - test               Run test cases in the tests/ folder
    - run                Run a script in the scripts/ folder
    - accounts           Manage local accounts
        -list
    - networks           Manage network settings
        -list
    - gui                Load the GUI to view opcodes and test coverage
    - analyze            Find security vulnerabilities using the MythX API

-Deploying to testnet/mainnet
    brownie run SCRIPT --network rinkeby

## Brownie Fund Me
-------
- import FundMe contract and deploy.
- verify smart contract on Etherscan

### Manually Verify
---
1. Verify Contract: [HERE](https://rinkeby.etherscan.io/verifyContract)
2. Enter code for smart contract
    - imports with '@' wont work! Etherscan doesnt know NPM
    - Code needs to be flattened

### Brownie Verify
---
1. Get API Key from Etherscan.io
2. Add API key to .env file
3. Add Publish to contract deployment




