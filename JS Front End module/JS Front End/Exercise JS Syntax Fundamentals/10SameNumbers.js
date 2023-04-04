function sameNumberChecker(number){
    let state = "true"
    let sum = 0
    let numberAsStr = String(number);
    let firstNum = numberAsStr[0];
    for (const el of numberAsStr) {
        sum += Number(el);
        if (el != firstNum){
            state = "false"
        }
    }
    console.log(state)
    console.log(sum)
}

sameNumberChecker(1234)