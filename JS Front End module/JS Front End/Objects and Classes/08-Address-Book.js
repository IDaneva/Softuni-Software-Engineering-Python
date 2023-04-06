function addressBookParser(infoArr){
    let addressBook = {};

    for (line of infoArr){
        let [name, address] = line.split(":");
        addressBook[name] = address;
    }

    let entries = Object.entries(addressBook);
    let sortedByName = entries.sort( (personA, personB) => {
        let personAName = personA[0];
        let personBName = personB[0];
        return personAName.localeCompare(personBName);
    }
    );

    for ([n, a] of sortedByName){
        console.log(`${n} -> ${a}`);
    }
}


addressBookParser(['Tim:Doe Crossing',

'Bill:Nelson Place',

'Peter:Carlyle Ave',

'Bill:Ornery Rd'])