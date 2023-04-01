function censorWords(text, word){
    let censored = text.replace(word, repeat(word));
    while (censored.includes(word)){
        censored.replace(word, repeat(word));
    }

    function repeat(word){
        let newWord = ""
        for (let index = 0; index < word.length; index++) {
            newWord += "*";
        }
        return newWord
    }

    console.log(censored);
}

censorWords('Find the hidden word', 'hidden')