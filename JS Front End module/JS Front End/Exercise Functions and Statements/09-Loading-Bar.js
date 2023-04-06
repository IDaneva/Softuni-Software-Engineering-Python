function loadingBar(number){
    if (number === 100){
        console.log("100% Complete!")
    } else {
        let firstNum = Number(String(number).split("")[0]);
        let rest = 10 - firstNum;
        console.log(`${number}% [${'%'.repeat(firstNum)}${'.'.repeat(rest)}]`);
        console.log("Still loading...");
    }
}

loadingBar(100);
loadingBar(0)