function subtract() {
    const input1 = Number(document.getElementById('firstNumber').value);
    const input2 = Number(document.getElementById('secondNumber').value);
    const divResult = document.getElementById('result');
    divResult.textContent = input1 - input2;
}