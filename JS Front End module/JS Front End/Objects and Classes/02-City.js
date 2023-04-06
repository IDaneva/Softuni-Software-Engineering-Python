function cityInfo(cityObj){
    for (key in cityObj){
        console.log(`${key} -> ${cityObj[key]}`);
    }
}

cityInfo({

    name: "Sofia",
    
    area: 492,
    
    population: 1238438, 
})