function splitPascalCase(str){
    let strAsArray = str.split("");
    let output = [];
    let startIndex = 0
    for (let index = 0; index < strAsArray.length; index++) {
        const element = strAsArray[index];
        if (element === element.toUpperCase() && index !== 0){
            output.push(strAsArray.slice(startIndex, index).join(""));
            startIndex = index
            continue
        }  else if (index === strAsArray.length-1){
            output.push(strAsArray.slice(startIndex, index+1).join(""));
        }
    }
    console.log(output.join(", "))
}

splitPascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan')