function movieInfoParser(movieArr){
    let movies = [];
    for (const info of movieArr) {
        if (info.includes("addMovie")){
            let movieName = info.split("addMovie ").join("");
            movies.push({name: movieName});
        } else if (info.includes("directedBy")){
            let [movieName, directorName] = info.split(" directedBy ");
            let foundMovieIndex = movies.findIndex(m => m.name === movieName)
            if (foundMovieIndex === -1) {
                // movies.push({name: movieName, date: "", director: directorName});
            } else {
                movies[foundMovieIndex]["director"] = directorName;
            }

        } else if (info.includes("onDate")){
            let [movieName, directedDate] = info.split(" onDate ");
            let foundMovieIndex = movies.findIndex(m => m.name === movieName)

            if (foundMovieIndex === -1) {
                // movies.push({name: movieName, date: directedDate, director: ""});
            } else {
                movies[foundMovieIndex]["date"] = directedDate;
            }
        }
    }

    let fullMovieInfo = movies.filter(m => Object.keys(m).length === 3);
    for (const iterator of fullMovieInfo) {
        console.log(JSON.stringify(iterator));
    }
}

movieInfoParser([

    'addMovie Fast and Furious',
    
    'addMovie Godfather',
    
    'Inception directedBy Christopher Nolan',
    
    'Godfather directedBy Francis Ford Coppola',
    
    'Godfather onDate 29.07.2018',
    
    'Fast and Furious onDate 30.07.2018',
    
    'Batman onDate 01.08.2018',
    
    'Fast and Furious directedBy Rob Cohen'
    
    ])

