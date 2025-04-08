let history = [];

function appendValue(value) {
    document.getElementById('result').value += value;
}

function clearResult() {
    document.getElementById('result').value = '';
}

function performOperation(operator) {
    document.getElementById('result').value += ` ${operator} `;
}

function performUnaryOperation(operation) {
    const value = parseFloat(document.getElementById('result').value);
    if (operation === 'sqrt') {
        document.getElementById('result').value = Math.sqrt(value);
    }
    addToHistory(`${operation}(${value})`);
}

function calculateResult() {
    try {
        const expression = document.getElementById('result').value;
        const result = eval(expression.replace('^', '**')); // Replace ^ with JS syntax
        document.getElementById('result').value = result;
        addToHistory(`${expression} = ${result}`);
    } catch {
        alert('Invalid Expression');
    }
}

function addToHistory(entry) {
    history.push(entry);
    const historyList = document.getElementById('history');
    const listItem = document.createElement('li');
    listItem.textContent = entry;
    historyList.appendChild(listItem);
}

function openUnitConverter() {
    document.getElementById('unitConverter').style.display = 'block';
}

function performConversion() {
    const inputValue = parseFloat(document.getElementById('unitInput').value);
    const conversionType = document.getElementById('conversionType').value;

    let result = 0;
    if (conversionType === 'metersToFeet') {
        result = inputValue * 3.28084;
    } else if (conversionType === 'feetToMeters') {
        result = inputValue / 3.28084;
    } else if (conversionType === 'kgToPounds') {
        result = inputValue * 2.20462;
    } else if (conversionType === 'poundsToKg') {
        result = inputValue / 2.20462;
    } else if (conversionType === 'celsiusToFahrenheit') {
        result = (inputValue * 9/5) + 32;
    } else if (conversionType === 'fahrenheitToCelsius') {
        result = (inputValue - 32) * 5/9;
    }

    document.getElementById('unitResult').value = result;
}