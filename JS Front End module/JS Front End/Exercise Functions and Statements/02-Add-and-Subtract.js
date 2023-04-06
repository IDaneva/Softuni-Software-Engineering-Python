function addAndSubtract(num1, num2, num3){
    sum = (num1, num2) => num1 + num2;
    subtract = (result, num3) => result - num3;
    console.log(subtract(sum(num1, num2), num3));
}
