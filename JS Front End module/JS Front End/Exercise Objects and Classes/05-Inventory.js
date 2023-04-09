function heroRegistration(heroData){
    let heros = [];
    for (const info of heroData) {
        [hero, level, items] = info.split(" / ");
        heros.push({hero, level, items});
    }

    let sortedHeros = heros.sort((heroA, heroB) =>{
        let heroALevel = heroA.level;;
        let heroBLevel = heroB.level;
        return heroALevel - heroBLevel
    });

    for (const iterator of sortedHeros) {
        console.log(`Hero: ${iterator.hero}\nlevel => ${iterator.level}\nitems => ${iterator.items}`);
    }
    
}

heroRegistration([

    'Isacc / 25 / Apple, GravityGun',
    
    'Derek / 12 / BarrelVest, DestructionSword',
    
    'Hes / 1 / Desolator, Sentinel, Antara'
    
    ])