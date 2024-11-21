// List of symptoms (you can dynamically fetch this if needed from the server)
const symptoms = [
    'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'malaise'
];

// Populate symptom dropdowns
document.addEventListener("DOMContentLoaded", function () {
    const symptomSelects = ['symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5'];
    
    symptomSelects.forEach(selectId => {
        const selectElement = document.getElementById(selectId);
        symptoms.forEach(symptom => {
            let option = document.createElement('option');
            option.value = symptom;
            option.text = symptom;
            selectElement.add(option);
        });
    });
});

function submitForm() {
    const selectedSymptoms = [];
    for (let i = 1; i <= 5; i++) {
        const symptomValue = document.getElementById(`symptom${i}`).value;
        if (symptomValue) {
            selectedSymptoms.push(symptomValue);
        }
    }

    if (selectedSymptoms.length === 0) {
        alert("Please select at least one symptom.");
        return;
    }

    // Send selected symptoms to the backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ symptoms: selectedSymptoms }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the results
        const resultDiv = document.getElementById('result');
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
            <h3>Predicted Diseases:</h3>
            <p>Decision Tree: ${data.DecisionTree}</p>
            <p>Random Forest: ${data.RandomForest}</p>
            <p>Naive Bayes: ${data.NaiveBayes}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
}
