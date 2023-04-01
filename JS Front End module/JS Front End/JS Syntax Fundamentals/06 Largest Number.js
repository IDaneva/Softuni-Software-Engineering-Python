function largestNumber(...numbers){
    let maxNumber = Math.max.apply(null, numbers);
    console.log(`The largest number is ${maxNumber}.`);
}

largestNumber(5, -3, 16)