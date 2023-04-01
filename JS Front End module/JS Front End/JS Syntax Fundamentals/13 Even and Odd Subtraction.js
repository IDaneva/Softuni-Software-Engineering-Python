function diffOfEvenAndOddSubtraction(arr){
    let evenSum = 0;
    let oddSum = 0;

    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        if (element % 2 === 0){
            evenSum += element;
        } else {
            oddSum += element;
        }
    }
    console,console.log(evenSum - oddSum);
}

diffOfEvenAndOddSubtraction([2,4,6,8,10])