// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 < 0.90;

contract SimpleStorage {
    // DATATYPES 
    // https://docs.soliditylang.org/en/v0.8.7/types.html
    uint256 public favUint;
    bool favBool = true;
    string favString = "String";
    int256 favNegInt =  -5;
    address favAddress = 0x8a86f8b05291083fD4Cd5A53ea42cF71Fb907740;
    bytes32 favBytes = "cat";
    
    // LIKE DICTIONARY OBJECT
    struct People {
        uint256 favUint;
        string name;
    }
    
    // visibilities public , private, internal , external
    // ARRAY
    // Fixed size array
    // People[1] public poeple;
    People[] public people;
    
    // Find object in array with mapping
    mapping(string => uint256) public nameToFavUint;
    
    // Single public object variable
    People public person = People({favUint: 2, name: "Daniel"});
    
    // memory only stored during execution
    // storage persists data
    function addPerson(string memory _name, uint256 _favUint) public {
        // Add person to array
        people.push(People({favUint: _favUint, name: _name}));
        // Add object to mapping
        nameToFavUint[_name] = _favUint;
    }
    
    function store(uint256 _favUint) public {
        favUint = _favUint;
    }
    
    // view defines functions that dont have to make a transaction - read only
    // pure does not return - read only
    function retrieve() public view returns(uint256){
        return favUint;
    }
}