document.getElementById('diabetes-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get input values
    const glucose = document.getElementById('glucose').value;
    const bloodPressure = document.getElementById('bloodPressure').value;
    const skinThickness = document.getElementById('skinThickness').value;
    const insulin = document.getElementById('insulin').value;
    const bmi = document.getElementById('bmi').value;
    const age = document.getElementById('age').value;

    // Send data to backend API
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ glucose, bloodPressure, skinThickness, insulin, bmi, age })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-result').style.display = 'block';
        document.getElementById('result-text').innerText = data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
