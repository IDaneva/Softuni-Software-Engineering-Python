function pianistCreator(musicArr){
    let countOfStartMusic = musicArr.shift();

    musicDict = {}

    for (let index = 0; index < countOfStartMusic; index++) {
        let [piece, composer, key] = musicArr.shift().split("|");
        musicDict[piece] = {composer, key};
    };

    while (true){
        let currentLine = musicArr.shift();

        if (currentLine === "Stop"){
            break; 
        }

        currentLine = currentLine.split("|");
        let command = currentLine.shift();

        if (command === "Add"){
            let [piece, composer, key] = currentLine;
            
            if (musicDict.hasOwnProperty(piece)){
                console.log(`${piece} is already in the collection!`);
            } else {
                musicDict[piece] = {composer, key};
                console.log(`${piece} by ${composer} in ${key} added to the collection!`);
            }

        } else if (command === "Remove"){
            let [piece] = currentLine;
            if (musicDict.hasOwnProperty(piece)){
                delete musicDict[piece];
                console.log(`Successfully removed ${piece}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }

        } else if (command === "ChangeKey"){
            let [piece, newKey] = currentLine;
            if (musicDict.hasOwnProperty(piece)){
                musicDict[piece].key = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`);
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            }
        }
    }

    for (const currentPiece in musicDict) {
        console.log(`${currentPiece} -> Composer: ${musicDict[currentPiece].composer}, Key: ${musicDict[currentPiece].key}`);
    }
    
}

pianistCreator([ '3', 'Fur Elise|Beethoven|A Minor', 'Moonlight Sonata|Beethoven|C# Minor', 'Clair de Lune|Debussy|C# Minor', 'Add|Sonata No.2|Chopin|B Minor', 'Add|Hungarian Rhapsody No.2|Liszt|C# Minor', 'Add|Fur Elise|Beethoven|C# Minor', 'Remove|Clair de Lune', 'ChangeKey|Moonlight Sonata|C# Major', 'Stop' ])