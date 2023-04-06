function palindromeIntegers(arr){
    for (let index = 0; index < arr.length; index++) {
        const elementAsArr = String(arr[index]).split("");
        let normalArr = elementAsArr
        let reversedAr = normalArr.map(x => x).reverse();
        if (normalArr.join("") === reversedAr.join("")){
            console.log("true");
        } else {
            console.log("false");
        }        
    }
}

palindromeIntegers([123, 423, 424])