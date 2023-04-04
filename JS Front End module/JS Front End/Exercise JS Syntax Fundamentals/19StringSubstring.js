function findSubstring(word, text){
    textAsArr = text.split(" ")

    for (const text of textAsArr) {
        if (text.toLowerCase() === word.toLowerCase()){
            return word;
        }
    }
    return `${word} not found!`

    // if (text.toLowerCase().includes(word.toLowerCase())){
    //     console.log(word);
    // } else {
    //     console.log(`${word} not found!`);
    // }
}
console.log(findSubstring('Sython',

'Psython is the best programming language'))
