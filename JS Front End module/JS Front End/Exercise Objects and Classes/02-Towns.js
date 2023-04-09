function townInfoGenerator(townArr){
    for (const town of townArr) {
        [city, latitude, longitude] = town.split(" | ");
        console.log({"town": city, "latitude": String(Number(latitude).toFixed(2)), "longitude": String(Number(longitude).toFixed(2))});
    }
}


townInfoGenerator(
['Sofia | 42.696552 | 23.32601',

'Beijing | 39.913818 | 116.363625'])