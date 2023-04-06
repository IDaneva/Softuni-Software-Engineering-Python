function factorialDivision(num1, num2){

    return (getFactorial(num1)/getFactorial(num2)).toFixed(2);

    function getFactorial(num){
        if (num === 1){
            return num;
        }
        return num * getFactorial(num-1);
    }
}

factorialDivision(5, 2)