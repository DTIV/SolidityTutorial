from brownie import SimpleStorage, accounts

'''
test one function = 'brownie test -k FUNCTION'
run python terminal in test - 'brownie test --pdb'
more robust results - 'brownie test -s

brownie tests come from: https://docs.pytest.org/en/6.2.x/
'''
def test_deploy():
    #Arrange
    account = accounts[0]

    #Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    #Assert
    assert starting_value == expected

def test_updating_storage():
    #ARRANGE
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    #ACT
    expected = 15
    simple_storage.store(expected,{"from": account})
    #ASSERT
    assert expected == simple_storage.retrieve()