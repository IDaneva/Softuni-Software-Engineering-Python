function oddAndEvenSum(number){
    let numbersAsArr = String(number).split("");
    let oddSum = 0;
    let evenSum = 0;
    for (let index = 0; index < numbersAsArr.length; index++) {
        const element = Number(numbersAsArr[index]);
        if (element % 2 === 0){
            evenSum += element;
        } else {
            oddSum += element;
        }
    }
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

oddAndEvenSum(1000435)