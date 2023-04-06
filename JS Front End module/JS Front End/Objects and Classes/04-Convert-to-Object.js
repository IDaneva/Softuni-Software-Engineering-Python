function convertToObject(input){
    let object = JSON.parse(input);
    for (info in object){
        console.log(`${info}: ${object[info]}`)
    }
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')