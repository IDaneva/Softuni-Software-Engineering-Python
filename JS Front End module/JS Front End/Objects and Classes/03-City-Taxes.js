function cityTaxes(name, population, treasury){
    let city = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes(){
            this.treasury += Math.floor(this.taxRate * population);
        },
        applyGrowth(percentage){
            this.population += Math.floor(percentage/100 * this.population);
        },
        applyRecession(percentage){
            this.treasury -= Math.floor(percentage/100 * this.treasury);
    }
    }
    return city;
}

const city =

cityTaxes('Tortuga',

7000,

15000);

console.log(city);


