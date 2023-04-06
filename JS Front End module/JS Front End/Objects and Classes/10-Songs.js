function songSolver(arr){
    let songs = arr.slice(1, arr.length - 1);
    let type = arr[arr.length - 1];
    for (songInfo of songs){
        let [typeList, name, length] = songInfo.split("_");
        if (type === "all"){
            console.log(name);
        } else {
        if (typeList === type){
            console.log(name);
        }
    }
}
}


songSolver([4,

    'favourite_DownTown_3:14',
    
    'listenLater_Andalouse_3:24',
    
    'favourite_In To The Night_3:58',
    
    'favourite_Live It Up_3:48',
    
    'listenLater'])