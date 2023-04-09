function storeProvision(arr1, arr2){
    let newArr = arr1.concat(arr2);
    let store = {};
    for (let index = 0; index < newArr.length - 1; index += 2) {
        const product = newArr[index];
        const quantity = Number(newArr[index+1]);
        if (!(product in store)){
            store[product] = quantity;
        } else {
            store[product] += quantity;
        }
    }
    for (const info in store) {
        console.log(`${info} -> ${store[info]}`);
    }

}

storeProvision([

    'Chips', '5', 'CocaCola', '9', 'Bananas',
    
    '14', 'Pasta', '4', 'Beer', '2'
    
    ],
    
    [
    
    'Flour', '44', 'Oil', '12', 'Pasta', '7',
    
    'Tomatoes', '70', 'Bananas', '30'
    
    ])


