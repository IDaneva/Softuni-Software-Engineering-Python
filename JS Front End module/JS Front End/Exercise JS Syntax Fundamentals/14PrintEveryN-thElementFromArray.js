function printNthElFromArray(array, step){
    let elements = []
    for (let index = 0; index < array.length; index+= step) {
        elements.push(array[index]);
    }
    return elements
}

printNthElFromArray(['dsa', 'asd', 'test', 'tset'], 2)