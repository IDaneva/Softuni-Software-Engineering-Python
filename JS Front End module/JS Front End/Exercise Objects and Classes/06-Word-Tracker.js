function wordTracker(Arr){
    let searchedWords = Arr[0].split(" ");
    let text = Arr.slice(1);
    let result = []
    for (const word of searchedWords) {
        let filtered = text.filter(w => w === word);
        result.push({word: word, count: filtered.length});
    }

    let sorted = result.sort((a, b) => b.count - a.count);
    for (const iterator in sorted) {
        console.log(`${sorted[iterator]["word"]} - ${sorted[iterator]["count"]}`)
    }
}

wordTracker([

    'is the',
    
    'first', 'sentence', 'Here', 'is',
    
    'another', 'the', 'And', 'finally', 'the',
    
    'the', 'sentence'])