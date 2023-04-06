function simpleCalculator(a, b, operator){
    let multiply = (num1, num2) => num1 * num2;
    let divide = (num1, num2) => num1 / num2;
    let add = (num1, num2) => num1 + num2;
    let subtract = (num1, num2) => num1 - num2;
    let operators = {multiply, divide, add, subtract};

    console.log(operators[operator](a, b));
}

simpleCalculator(5,5,"multiply")