function predict() {
    let one = parseFloat(document.getElementById("input1").value);
    let two = parseFloat(document.getElementById("input2").value);
    let three = parseFloat(document.getElementById("input3").value);
    let four = parseFloat(document.getElementById("input4").value);
    let result = 4.16e-5 * one + 1.305 * two + 13.95 * three + 5.855 * four - 330.696;
    let eResult = Math.exp(result);
    let lastResult = eResult / (1 + eResult);
    document.getElementById("result").innerText = "预测结果: " + lastResult;
    console.log(lastResult);
}