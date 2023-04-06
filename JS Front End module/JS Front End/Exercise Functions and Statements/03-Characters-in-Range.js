function charactersInRange(ch1, ch2){
    let firstAsciiCode = ch1.charCodeAt(0);
    let secondAsciiCode = ch2.charCodeAt(0);
    let smallestChar = Math.min(firstAsciiCode, secondAsciiCode);
    let biggestChar = Math.max(firstAsciiCode, secondAsciiCode);
    let symbols = [];
    for (let start = smallestChar + 1; start < biggestChar; start++) {
        symbols.push(String.fromCharCode(start));
        
    }
    console.log(symbols.join(" "));
}


charactersInRange("#", ":")