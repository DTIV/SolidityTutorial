# Fund Me
--------
Learn how to call contracts and functions from external contracts, and then using Chainlink Aggregator V3 Interface and SafeMath create a contract that accepts ETH funding over a specified amount of USD value. 
- A Mapping is created linking a user address to the amount funded.
- create a payable function called 'fund' that checks the value sent and then adds to mapping
- get version from AggregatorV3Interface
- get price from a tuple using AggregatorV3Interface
- create a conversion rate function

## Conversion Logic

- minimum USD value requried, in this case $20

```solidity
uint256 minimumUSD = 20 * one_wei;
```

