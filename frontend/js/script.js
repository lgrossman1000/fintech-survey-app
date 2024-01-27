document.addEventListener('DOMContentLoaded', function() {
    const surveyForm = document.getElementById('surveyForm');
    surveyForm.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Thank you for your feedback!');
        
        // Here you would normally handle the form submission, e.g., send it to the backend
        document.addEventListener('DOMContentLoaded', function() {
            const surveyForm = document.getElementById('surveyForm');
            surveyForm.addEventListener('submit', function(event) {
                event.preventDefault();
                const formData = {
                    age: document.getElementById('age').value,
                    experience: document.getElementById('experience').value,
                    productUse: document.getElementById('productUse').value,
                    satisfaction: document.getElementById('satisfaction').value,
                    feedback: document.getElementById('feedback').value,
                };
                fetch('http://localhost:5000/submit-survey', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData),
                })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
            });
        });
        
    });
});
