function speedLimitChecker(speed, area){
    let motorway = {"limit": 130};
    let interstate = {"limit": 90};
    let city = {"limit": 50};
    let residential = {"limit": 20};

    if (area === "motorway"){
        if (speed > motorway.limit){
            let difference = speed - motorway.limit
            let status = "reckless driving"
            if (difference <= 20){
                status = "speeding"
            } else if (difference <= 40){
                status = "excessive speeding"
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${motorway.limit} - ${status}`)
        } else{
            console.log(`Driving ${speed} km/h in a ${motorway.limit} zone`)
        }
    } else if (area ==="interstate"){
        if (speed > interstate.limit){
            let difference = speed - interstate.limit
            let status = "reckless driving"
            if (difference <= 20){
                status = "speeding"
            } else if (difference <= 40){
                status = "excessive speeding"
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${interstate.limit} - ${status}`)
        } else{
            console.log(`Driving ${speed} km/h in a ${interstate.limit} zone`)
        }
    } else if (area ==="city"){
        if (speed > city.limit){
            let difference = speed - city.limit
            let status = "reckless driving"
            if (difference <= 20){
                status = "speeding"
            } else if (difference <= 40){
                status = "excessive speeding"
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${city.limit} - ${status}`)
        } else{
            console.log(`Driving ${speed} km/h in a ${city.limit} zone`)
        }
    } else if (area ==="residential"){
        if (speed > residential.limit){
            let difference = speed - residential.limit
            let status = "reckless driving"
            if (difference <= 20){
                status = "speeding"
            } else if (difference <= 40){
                status = "excessive speeding"
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${residential.limit} - ${status}`)
        } else{
            console.log(`Driving ${speed} km/h in a ${residential.limit} zone`)
        }
    }

}

speedLimitChecker(1201, "interstate")