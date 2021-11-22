# Fund Me
--------
Learn how to call contracts and functions from external contracts, and then using Chainlink Aggregator V3 Interface and SafeMath create a contract that accepts ETH funding over a specified amount of USD value. 
- A Mapping is created linking a user address to the amount funded.
- create a payable function called 'fund' that checks the value sent and then adds to mapping
- get version from AggregatorV3Interface
- get price from a tuple using AggregatorV3Interface
- create a conversion rate function

## Conversion Logic

```solidity
uint256 one_wei = 1000000000000000000; // 18 decimals
uint256 one_gwei = 1000000000; // 9 decimals
```
- minimum USD value requried, in this case $20, down to the 18th decimal

```solidity
uint256 minimumUSD = 20 * one_wei;
```

