// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 < 0.90;

import "./SimpleStorage.sol";

// inherhit all contract function using is statement
contract StorageFactory is SimpleStorage{
    //create a public array for contracts
    SimpleStorage[] public simpleStorageArray;
    
    function createStorageContract() public {
        // creating a new contract and add to array.
        // || type ||   || name ||          || contract ||        
        SimpleStorage simpleStorage = new SimpleStorage();
        // push contract to simpleStorageArray
        simpleStorageArray.push(simpleStorage);
    }
    
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // function to call store function from imported contract
        // when interacting with another contract an Address and ABI are needed. The address can be found in the simpleStorageArray. 
        // create a contract instance from imported contract
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        // call store function from instance
        simpleStorage.store(_simpleStorageNumber);
    }
    
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
        // creating a contract instance from imported contract to retrieve stored value
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
    }
}