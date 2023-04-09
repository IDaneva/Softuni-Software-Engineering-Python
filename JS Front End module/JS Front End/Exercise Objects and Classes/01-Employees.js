function employeePersonalNumber(namesArr){
    for (const name of namesArr) {
        let personalNumber = name.length;
        console.log(`Name: ${name} -- Personal Number: ${personalNumber}`)
    }
}

employeePersonalNumber([

    'Silas Butler',
    
    'Adnaan Buckley',
    
    'Juan Peterson',
    
    'Brendan Villarreal'
    
    ])