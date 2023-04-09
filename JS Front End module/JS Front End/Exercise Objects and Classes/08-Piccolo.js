function piccolo(commands){
    let parkingLot = new Set;
    for (const iterator of commands) {
        [direction, carPlate] = iterator.split(", ");
        if (direction === "IN"){
            parkingLot.add(carPlate);
        } else if (direction === "OUT"){
            parkingLot.delete(carPlate);
        }  
    }
    if (!parkingLot){
        console.log("Parking Lot is Empty");
    } else {
    parkingLot = Array.from(parkingLot).sort((carA, carB) => carA.localeCompare(carB)).forEach(c => console.log(c));
    }
}

// Write a function that:

// · Records a car number for every car that enters the parking lot

// · Removes a car number when the car goes out

// · Input will be an array of strings in format [direction, carNumber]

// Print the output with all car numbers which are in the parking lot sorted in ascending by number.

// If the parking lot is empty, print: "Parking Lot is Empty".

piccolo(['IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA', 'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 'IN, CA2822UU'])

