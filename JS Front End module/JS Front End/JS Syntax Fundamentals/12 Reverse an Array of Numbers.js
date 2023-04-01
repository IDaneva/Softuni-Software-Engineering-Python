function reverseArr(num, arr){
    if (num === arr.length){
        console.log(arr.reverse().join(" "));
    } else {
        let newArr = [];
        for (let index = 0; index < num; index++) {
            const element = arr[index];
            newArr.unshift(element);
        }
        console.log(newArr.join(" "));
    }
}

reverseArr(3, [10, 20, 30, 40, 50])