function fruitCost(fruitType, weight, pricePerKg){
    let weightInKg = weight / 1000;
    let cost = weightInKg * pricePerKg;
    console.log(`I need $${cost.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruitType}.`)
}

fruitCost('apple', 1563, 2.35)