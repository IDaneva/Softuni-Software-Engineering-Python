function revealWords(str, text){
    let words = str.split(", ")
    let textAsArray = text.split(" ")
    for (let index = 0; index < words.length; index++) {
        let word = words[index];
        for (let index = 0; index < textAsArray.length; index++) {
            if (word.length === textAsArray[index].length && textAsArray[index].includes("*")){
                textAsArray[index] = word;
            }   
        }
    }
    console.log(textAsArray.join(" "))
}

revealWords('great, learning',

'softuni is ***** place for ******** new programming languages')