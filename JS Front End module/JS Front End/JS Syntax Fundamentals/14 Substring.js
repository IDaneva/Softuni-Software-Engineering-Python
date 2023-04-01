function substring(word, startIndex, countOfElements){
    let wordAsArr = word.split("")
    let output = wordAsArr.splice(startIndex, countOfElements);
    console.log(output.join(""))
}


substring("SkipWord", 4, 7)