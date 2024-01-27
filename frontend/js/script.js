document.addEventListener('DOMContentLoaded', function() {
    let selections = []; // Array to store selected options

    // Function to toggle selection
    function toggleSelection(option) {
        const index = selections.indexOf(option);
        if (index === -1) {
            selections.push(option); // Add to selections if not already present
        } else {
            selections.splice(index, 1); // Remove from selections if present
        }
    }

    // Add event listeners to option buttons
    document.querySelectorAll('.option-button').forEach(function(button) {
        button.addEventListener('click', function(event) {
            this.classList.toggle('active'); // Toggle the 'active' class visually
            toggleSelection(this.textContent); // Update the selections array
        });
    });

    // Event listener for 'Other' option input when user presses Enter
    const otherInput = document.getElementById('other');
    otherInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent form submission
            toggleSelection(otherInput.value); // Update the selections array
            otherInput.value = ''; // Clear the input field
        }
    });

    // Event listener for 'Next' button
    const nextButton = document.getElementById('nextButton');
    nextButton.addEventListener('click', function() {
    // Check if there's any input in the 'Other' box and add it to selections
        const otherValue = document.getElementById('other').value.trim();
        if (otherValue) {
            selections.push(otherValue);
        }
        
        console.log("Selected options:", selections);
        // Here you would send the selections to the server
        // For example, using fetch or another method to submit the data
        sendResponse(selections);
        // Clear the 'Other' input box
        document.getElementById('other').value = '';
        // Clear selection
        selections = [];
        //Remove the 'active' class from all option bottons
        document.querySelectorAll('.option-button.active').forEach(function(button) {
            button.classList.remove('active');
        });
        
        
    });
});

// Function to send the response to the server
function sendResponse(response) {
    // This is where you would handle sending the response to your backend
    console.log('Sending response:', response);
    // Example fetch call (you would replace the URL with your actual endpoint)
    fetch('http://localhost:5000/submit-survey', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ responses: response }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    
    // Reset selections after sending
    selections = [];
    // Reset all active classes
    document.querySelectorAll('.option-button.active').forEach(function(button) {
        button.classList.remove('active');
    });
}
