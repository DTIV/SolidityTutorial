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
1. minimum USD value requried declared inside fund function, in this case $20, down to the 18th decimal.

```solidity
uint256 minimumUSD = 20 * one_wei; // 20.000000000000000000
```
2. getPrice Function is used to get the current datafeed price from selected contract. The returned value is rounded to only 8 decimal places, so we must multiply the returned value by 10 ** 10 to get 18 decimal places

```solidity
// returned value directly from chainlink - 8 decimals
return uint256(answer); // 4325.23423453

//returned value after - 18 decimals
return uint256(answer * 10000000000); // 4178.385269520000000000
```

3. getConversion function is now created. The current Eth price is now multiplied by Eth amount
For this example, 

```solidity
uint256 ethAmount = 1000000000 // 1gwei
uint256 ethAmountInUsd = (ethPrice * ethAmount); // $ 4154111272270.000000000000000000 USD
```
However the returned amount is too large, it has an additional 18 decimals, so the amount must be divided by 10 ** 18
```solidity
uint256 ethAmount = 1000000000 // 1gwei
uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000; // 4154111272270 returned value
// true value:
// $ .000004154111272270 USD // 18 decimal places
```

4. Confirm conversion is correct:

```
//      USD AMOUNT    X     ETH AMOUNT    =     ETH PRICE
$ .000004154111272270 x 1000000000(1gwei) = 4,154.11127227 ETH
```








