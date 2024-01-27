document.addEventListener('DOMContentLoaded', function() {
    const surveyForm = document.getElementById('surveyForm');
    surveyForm.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Thank you for your feedback!');
        
        document.addEventListener('DOMContentLoaded', function() {
            // Add event listeners to option buttons
            document.querySelectorAll('.option-button').forEach(function(button) {
                button.addEventListener('click', function(event) {
                    const value = this.textContent;
                    sendResponse(value); // Function to handle the response
                });
            });
        
            // Event listener for 'Other' option input when user presses Enter
            const otherInput = document.getElementById('other');
            otherInput.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    const value = otherInput.value;
                    sendResponse(value); // Function to handle the response
                }

            const nextButton = document.getElementById('nextButton');
            nextButton.addEventListener('click', function() {
                print("next clicked")
                // Logic to handle "Next" button click
                // This could be sending data, navigating to another page, etc.
                alert('Next button clicked!');
            });

            });
        });
        
        function sendResponse(response) {
            fetch('http://localhost:5000/submit-survey', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ response }),
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        
            alert('Thank you for your response: ' + response);
        }
        
        
    });
});
