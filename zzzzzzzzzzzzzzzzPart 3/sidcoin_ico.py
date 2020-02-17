// Solidity file
// Sidcoins ICO

// Version of compiler
pragma solidity ^0.4.11;

contract sidcoin_ico {
    
    // Introducing the max number of Sidcoins available for sealed
    uint public max_sidcoins = 1000000;
    
    // Introducing the USD to Sidcoin conversion rate
    uint public usd_to_sidcoins = 1000;
    
    // Introducing the total no of Sidcoins that have been bought by the investors
    uint public total_sidcoins_bought = 0; 
    
    // Mapping from the investor address to its equity in Sidcoins and USD
    mapping(address => uint) equity_sidcoins;
    mapping(address => uint) equity_usd;
    
    // Checking if an investor can buy Sidcoins
    modifier can_buy_sidcoins(uint usd_invested){
        require (usd_invested * usd_to_sidcoins + total_sidcoins_bought <= max_sidcoins);
        _;
    }
    
    // Getting the equity in sidcoins of an investor
    function equity_in_sidcoins(address investor) external constant return (uint) {
        return equity_sidcoins[investor];
    }
    
    //Getting the equity in USD of an investor
    function equity_in_usd(address investor) external constant return (uint) {
        return equity_usd[investor];
    }
    
    //Buying Sidcoins
    function buy_sidcoins(address investor, uint usd_invested) external 
    can_buy_sidcoins(usd_invested){
        uint sidcoins_bought = usd_invested * usd_to_sidcoins;
        equity_sidcoins[investor] += sidcoins_bought;
        equity_usd[investor] = equity_sidcoins[investor] / 1000;
        total_sidcoins_bought += sidcoins_bought;
    }
    
    //Selling Sidcoins
    function sell_sidcoins(address investor, uint sidcoins_sold) external {
        equity_sidcoins[investor] -= sidcoins_sold;
        equity_usd[investor] = equity_sidcoins[investor] / 1000;
        total_sidcoins_bought -= sidcoins_sold;
    }
    
}
