function catsCreator(arr){
    let cats = []; 

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow(){
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    for (info of arr){
        let [name, age] = info.split(" ");
        cats.push(new Cat(name, age));
    }

    for (cat of cats) {
        cat.meow()
    }
}

catsCreator(['Mellow 2', 'Tom 5'])