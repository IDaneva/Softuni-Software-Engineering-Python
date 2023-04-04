function printAndSum(startNum, endNum){
    let numbers = []
    while (startNum <= endNum){
        numbers.push(startNum);
        startNum += 1
    }
    console.log(numbers.join(" "))
    sum = 0
    for (let i = 0; i < numbers.length; i += 1){
        sum += numbers[i]
    }

    console.log(`Sum: ${sum}`)

}

printAndSum(5, 10)
