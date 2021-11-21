// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    // payable functions can be used to pay for things specifically with Ethereum
    function fund() public payable {
        // msg.sender and msg.value are keywords in every contract call and tx 
        // msg.sender is the sender of the contract call
        // msg.value is the amount sent
        addressToAmountFunded[msg.sender] += msg.value;
    }
}


