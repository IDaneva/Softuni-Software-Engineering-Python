function sortingNumbers(array){
    let output = []
    array = array.filter(element => typeof element === "number");

    while (array.length > 0){
        let smallestNumber = Math.min.apply(Math, array);
        let maxNumber = Math.max.apply(Math, array);
        if (smallestNumber === maxNumber){
            output.push(smallestNumber);
        } else{
        output.push(smallestNumber, maxNumber);
        }
        array = array.filter(function(e) {return e!== smallestNumber});
        array = array.filter(function(e) {return e!== maxNumber});
    }

    return output;
}


sortingNumbers([21, 2, 70000, "a"])