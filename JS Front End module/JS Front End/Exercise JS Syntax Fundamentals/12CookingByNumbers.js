function cookingByNumbers(number, param1, param2, param3, param4, param5){
    numAsNumber = Number(number)
    let operators = [param1, param2, param3, param4, param5]

    for (const el in operators) {
        if (operators[el] === "chop"){
            numAsNumber /= 2
        } else if (operators[el] === "dice"){
            numAsNumber = Math.sqrt(numAsNumber)
        } else if (operators[el] === "spice"){
            numAsNumber += 1
        } else if (operators[el] === "bake"){
            numAsNumber *= 3
        } else if (operators[el] === "fillet"){
            numAsNumber *= 0.8
        }
        console.log(numAsNumber)
    }
}


cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake','fillet')