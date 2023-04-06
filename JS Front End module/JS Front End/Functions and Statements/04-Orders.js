function totalOrderPriceCalculator(product, quantity){
    let prices = {"coffee": 1.5, "water": 1, "coke": 1.4, "snacks": 2};
    let finalPrice = prices[product] * quantity;
    console.log(finalPrice.toFixed(2));
}

totalOrderPriceCalculator("water", 5)