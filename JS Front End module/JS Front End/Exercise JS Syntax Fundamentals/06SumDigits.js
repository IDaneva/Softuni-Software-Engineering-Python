function sumDigits(number){
    let i = 0;
    let sum = 0;
    numberAsString = String(number)
    while (i < numberAsString.length){
        sum += Number(numberAsString[i])
        i += 1
    }
    console.log(sum)
}

sumDigits(245678)