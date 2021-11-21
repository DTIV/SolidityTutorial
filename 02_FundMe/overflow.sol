/* 
    Demonstrating the overflow when int capacity is exceeded.
    if using versions less than 6.0 use openZeppelin safeMath
    https://docs.openzeppelin.com/contracts/2.x/api/math 
*/
    
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.6 <0.9.0;

contract Overflow{
    function overflow() public pure returns(uint8){
        // uint8 -- largest 255
        // uint8 big = 256; => 0
        uint8 big = 255;
        return big;
    }
}