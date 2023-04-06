function phoneBook(input){
    let phonesInfo = {};
    for (line of input){
        let [name, phone] = line.split(' ')
        phonesInfo[name] = phone;
}

for (n in phonesInfo){
    console.log(`${n} -> ${phonesInfo[n]}`);
}
}

phoneBook(['Tim 0834212554',

'Peter 0877547887',

'Bill 0896543112',

'Tim 0876566344']);