function arrayRotation(array, numberOfRotations){
    for (let index = 0; index < numberOfRotations; index++) {
        let firstNumber = array.shift();
        array.push(firstNumber);
    }
    console.log(array.join(" "))
}

arrayRotation([32, 21, 61, 1], 4)