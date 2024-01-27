document.addEventListener('DOMContentLoaded', function() {
    const surveyForm = document.getElementById('surveyForm');
    surveyForm.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Thank you for your feedback!');
        // Here you would normally handle the form submission, e.g., send it to the backend
    });
});
