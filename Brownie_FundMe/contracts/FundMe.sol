// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

// brownie is not aware of NPM packages, brownie can get from github!
// edit brownie-config.yaml - if successfull adds dependancies to build/contracts
// getRoundData and latestRoundData should both raise "No data present"
  // if they do not have data to report, instead of returning unset values
  // which could be misinterpreted as actual reported values.

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract FundMe {
    // initializing safemath library for all uint256 in contract using a chainlink contract. not needed in versions > 0.8 - see overflow.sol as example
    using SafeMathChainlink for uint256;
    
    uint256 one_wei = 1000000000000000000;
    uint256 one_gwei = 1000000000;
    
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    
    // Create Global Aggregator;
    AggregatorV3Interface public priceFeed;

    address public owner;
    constructor(address _priceFeed) public {
        // msg.sender is who deployed the contract
        owner = msg.sender;

        // create priceFeed on deployment
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    function fund() public payable {
        uint256 minimumUSD = 20 * one_wei;
        require(getConversionRate(msg.value) >= minimumUSD, "Not enough ETH funded");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }
    
    function getUSDtoWei() public view returns(uint256){
        uint256 minimumUSD = 20 * one_wei;
        return minimumUSD;
    }
    
    function getVersion() public view returns(uint256){
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256){
        (
          uint80 roundId,
          int256 answer,
          uint256 startedAt,
          uint256 updatedAt,
          uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }
    
    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount)/ 1000000000000000000;
        return ethAmountInUsd;
    }
    
    modifier onlyOwner(){
        require(msg.sender == owner, "You are not the owner!");
        _;
    }
    
    function withdraw() payable onlyOwner public {
        msg.sender.transfer(address(this).balance);
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}