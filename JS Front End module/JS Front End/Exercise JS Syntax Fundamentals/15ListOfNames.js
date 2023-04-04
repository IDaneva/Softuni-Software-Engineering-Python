function sortAlphabetically(array){
    let sortedArray = array.sort()
    let message = []
    for (let index = 0; index < array.length; index++) {
        message.push(`${index+1}.${sortedArray[index]}`);
    }
    console.log(message.join(`\n`));
}

sortAlphabetically(["John",

"Bob",

"Christina",

"Ema"])