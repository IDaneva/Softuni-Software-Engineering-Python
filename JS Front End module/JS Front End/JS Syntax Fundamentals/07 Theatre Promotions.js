function theaterTicketCost(day, age){
    let ageGroup
    if (age < 0 || age > 122){
        console.log("Error!");
    } else if (age >= 0 && age <= 18){
        ageGroup = "child";
    } else if (age > 18 && age <= 64){
        ageGroup = "adult";
    } else if (age > 64 && age <= 122){
        ageGroup = "elderly";
    }
    let weekDay = {"child": 12, "adult": 18, "elderly": 12};
    let weekend = {"child": 15, "adult": 20, "elderly": 15};
    let holiday = {"child": 5, "adult": 12, "elderly": 10};

    if (day === 'Weekday' && age >= 0 && age <= 122){
        console.log(`${weekDay[ageGroup]}$`);
    } else if (day === "Weekend" && age >= 0 && age <= 122){
        console.log(`${weekend[ageGroup]}$`);
    } else if (day === "Holiday" && age >= 0 && age <= 122){
        console.log(`${holiday[ageGroup]}$`);
    }
}   

theaterTicketCost('Weekday',

-42)