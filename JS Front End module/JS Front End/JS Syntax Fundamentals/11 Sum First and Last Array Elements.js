function sumFirstAndLast(arr){
    let firstEl = arr.shift();
    let lastEl = arr.pop();
    console.log(firstEl + lastEl);
}

sumFirstAndLast([10, 17, 22, 33])