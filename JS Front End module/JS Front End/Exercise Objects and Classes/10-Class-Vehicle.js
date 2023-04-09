class Vehicle{
    constructor(type, model, parts, fuel){
        this.type = type;
        this.model = model;
        this.parts = {
            engine: parts.engine,
            power: parts.power,
            quality: parts.engine * parts.power
        }
        this.fuel = fuel;
    }
    drive(fuelLoss){
        this.fuel -= fuelLoss;
    }

}

// engine – number (quality of the engine)

// o power – number

// o quality – engine * power

let parts = { engine: 6, power: 100 };

let vehicle = new Vehicle('a', 'b', parts, 200);

vehicle.drive(100);

console.log(vehicle.fuel);

console.log(vehicle.parts.quality);
// · fuel – a number

// · drive – a method that receives fuel loss and decreases the fuel of the vehicle by that number
