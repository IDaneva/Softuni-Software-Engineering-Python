function signCheck(...numbers){
    let negatives = numbers.filter((e)=> e < 0)
    if (negatives.length % 2 === 0){
        console.log("Positive")
    } else {
        console.log("Negative")
    }
}

signCheck(-5, 12, 3)