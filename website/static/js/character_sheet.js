// Event listeners attached to parent class
$(document).ready(function() {
    loadCharacterData();
    // Execute the update function to load character data when the page loads
});

$(document).on("input", ".ability-score-input", debounce(function(e) {
    // Send AJAX request to save input data
    saveInputData(e.target.id, e.target.value);
}, 300)); // Delay of 300 milliseconds

function loadCharacterData() {
    $.ajax({
        url: "/get_character_data",
        method: "GET",
        success: function(characterData) {
            updateDivsWithValues(characterData);
        },
        error: function(xhr, status, error) {
            console.error("Error loading character data:", error);
        }
    });
}

function saveInputData(id, value) {
    // Save input data to the backend
    $.ajax({
        url: "/save_input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: value, type: id }),
        success: function(elementsToUpdateDict) {
            updateDivsWithValues(elementsToUpdateDict);
        },
        error: function(xhr, status, error) {
            console.error("Error saving input data:", error);
        }
    });
}


// Debounce function to delay execution of the input event handler
function debounce(func, delay) {
    let timeoutId;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(timeoutId);
        timeoutId = setTimeout(function() {
            func.apply(context, args);
        }, delay);
    };
}

// Update the divs with the specified IDs
function updateDivsWithValues(data) {
    for (const elementId in data) {
        if (Object.hasOwnProperty.call(data, elementId)) {
            const newValue = data[elementId];
            const element = document.getElementById(elementId);
            if (element) {
                element.innerText = newValue;
            }
        }
    }
}