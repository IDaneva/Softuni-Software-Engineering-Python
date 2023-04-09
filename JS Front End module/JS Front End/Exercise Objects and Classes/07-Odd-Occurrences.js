function oddOccurrences(words){
    let wordsArr = words.split(" ").map(w => w.toLowerCase());
    let result = new Set;
    for (const word of wordsArr) {
        let filtered = wordsArr.filter(w => w === word);
        if (filtered.length % 2 !== 0) {
            result.add(word);
        }
    }
    console.log(Array.from(result).join(" "));
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')