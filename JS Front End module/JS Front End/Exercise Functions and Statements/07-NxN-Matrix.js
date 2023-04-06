function matrixGenerator(num){
    for (let index = 0; index < num; index++) {
       console.log(`${String(num)} `.repeat(num));
    }
}

matrixGenerator(3)