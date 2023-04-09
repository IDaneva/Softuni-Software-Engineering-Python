function dictionaryCreator(strArr){
    let result = [];
    for (const jsonStr of strArr) {
        let obj = JSON.parse(jsonStr);
        result.push(obj);
    }

    let sorted = result.sort((termA, termB) =>{
        let wordA = Object.keys(termA)[0];
        let wordB = Object.keys(termB)[0];
        return wordA.localeCompare(wordB);
    })
    
    for (const iterator of sorted) {
        let word = Object.keys(iterator)[0];
        console.log(`Term: ${word} => Definition: ${iterator[word]}`);
    }

}


dictionaryCreator([

    '{"Cup":"A small bowl-shaped container for drinking from,typically having a handle"}',
    
    '{"Cake":"An item of soft sweet sometimes iced or decorated."}'
    
    ])