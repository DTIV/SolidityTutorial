// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;
/* 
@chainlink/contracts is importing from npm package
https://www.npmjs.com/package/@chainlink/contracts

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
use import link above instead of writing functions manually as done below

interface github repo from https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol

ABI = Application Binary interface : tells solidity and programming languages how it can interact with another contract
  -- Anytime you want to interact with a deployed smart contract you need and ABI
*/



interface AggregatorV3Interface {
  function decimals() external view returns (uint8);

  function description() external view returns (string memory);

  function version() external view returns (uint256);

  // getRoundData and latestRoundData should both raise "No data present"
  // if they do not have data to report, instead of returning unset values
  // which could be misinterpreted as actual reported values.
  function getRoundData(uint80 _roundId)
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );

  function latestRoundData()
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );
}

// Must be deployed to a network and not javascript vm because chainlink contracts dont exist there.
contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    // payable functions can be used to pay for things specifically with Ethereum
    function fund() public payable {
        // msg.sender and msg.value are keywords in every contract call and tx 
        // msg.sender is the sender of the contract call
        // msg.value is the amount sent
        addressToAmountFunded[msg.sender] += msg.value;
    }
    
    function getVersion() public view returns(uint256){
        /* 
            making a contract call to a chainlink contract from this contract and calling version function from chainlink datafeed
            - getting datafeed address for desired network (currently rinkeby) at:
                https://docs.chain.link/docs/ethereum-addresses/
        */
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    
    function getPrice() public view returns(uint256){
        // Create a tuple of all returned values from latestRoundData
        // if int types are different that returns int type ie int/uint then typewrap the value to change int256(uint256)
        // Alternativly: (,int256 answer,,,) = priceFeed.latestRoundData();
        
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (
          uint80 roundId,
          int256 answer,
          uint256 startedAt,
          uint256 updatedAt,
          uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return uint256(answer * 1000000000);
    }
    
    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        // get price from getPrice function
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount);
        return ethAmountInUsd;
    }
}


