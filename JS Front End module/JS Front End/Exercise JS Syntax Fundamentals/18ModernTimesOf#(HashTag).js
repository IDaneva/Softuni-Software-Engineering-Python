function findSpecialWords(text){
    let textAsArray = text.split(" ");
    let specialWords = [];
    for (let index = 0; index < textAsArray.length; index++) {
        let word = textAsArray[index];
        const regex = /^#[a-zA-Z]+$/;
        if (regex.test(word)){
            specialWords.push(word.slice(1));
        }
    }
    console.log(specialWords.join(`\n`));
}

findSpecialWords('The symbol # is known #variously in English-speaking #regions as the #number sign')