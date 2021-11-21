// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 < 0.90;

import "./SimpleStorage.sol";

contract StorageFactory{
    SimpleStorage[] public simpleStorageArray;
    
    function createStorageContract() public {
        // creating a new contract and add to array.
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }
    
}