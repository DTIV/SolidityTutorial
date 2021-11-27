# Brownie Project
------------------

'brownie init'

## BUILD FOLDER
- low level info and compiled solidity code
- keeps track of deployments across multiple chains

## CONTRACTS FOLDER
-where contracts are stored

## INTERFACES
-where different interfaces are stores

## SCRIPTS
-automating functions

## TESTS
-running tests against code

1. Create SimpleStorage.sol in contracts FOLDER
2. Create deploy.py in scripts FOLDER
3. Add account to brownie with 'brownie accounts new NAME'
    - view accounts with 'brownie accounts list'
    - Always store real money in brownie with password -- not in .env
5. create brownie-config.yaml
    - tell brownie to pull data from .env file
    - add 'dotenv: .env'
    - add information for different wallets and when they are used
6. create simple_storage_test.py in test Folder
    - test must be first word in file name
    - tests are done in three catagories:
        1. Arrange
        2. Act
        3. Assert