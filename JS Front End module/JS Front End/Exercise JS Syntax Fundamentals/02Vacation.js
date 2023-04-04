function vacationCalculator(numberOfPeople, groupType, dayOfWeek){
    let student = {"Friday": 8.45, "Saturday": 9.8, "Sunday": 10.46}
    let business = {"Friday": 10.9, "Saturday": 15.6, "Sunday": 16}
    let regular = {"Friday": 15, "Saturday": 20, "Sunday": 22.5}

    let cost = undefined
    if (groupType === "Students"){
        cost = student[dayOfWeek] * numberOfPeople
    } else if (groupType === "Business"){
        cost = business[dayOfWeek] * numberOfPeople
    } else if (groupType === "Regular"){
        cost = regular[dayOfWeek] * numberOfPeople
    }

    if (groupType === "Students" && numberOfPeople >= 30){
        cost -= cost * 0.15
    }

    if (groupType === "Business" && numberOfPeople >= 100){
        cost -= business[dayOfWeek] * 10
    }

    if (groupType === "Regular" && numberOfPeople >= 10 && numberOfPeople <= 20){
        cost -= cost * 0.05
    } 

    console.log(`Total price: ${cost.toFixed(2)}`)
}

vacationCalculator(30,

    "Students",
    
    "Sunday")