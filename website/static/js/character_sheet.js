

// Event listeners attached to parent class
$(document).ready(function() {
    loadCharacterData();
    // Execute the update function to load character data when the page loads
});

$(document).on("keydown blur", "input[type='text'], input[type='number'], textarea", debounce(function(e) {
    //check weather input was finished by pressing "Enter"
    if (e.type === 'keydown' && e.key !== 'Enter') {
        return;
    }
    // Send AJAX request to save input data of text and number
    saveCharacterData(e.target.id, e.target.value);
}, 300)); // Delay of 300 milliseconds

$(document).on("change", "input[type='checkbox']", function() {
    // Get checkbox ID and checked state
    const checkboxId = this.id;
    const isChecked = this.checked;
    // Send AJAX request to save checkbox state
    saveCharacterData(checkboxId, isChecked);
});

function loadCharacterData() {
    $.ajax({
        url: "/get_character_data",
        method: "GET",
        success: function(characterData) {
            updateElementsWithData(characterData);
        },
        error: function(xhr, status, error) {
            console.error("Error loading character data:", error);
        }
    });
}

function saveCharacterData(id, value) {
    // Save input data to the backend
    $.ajax({
        url: "/save_input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: value, type: id }),
        success: function(elementsToUpdateDict) {
            updateElementsWithData(elementsToUpdateDict);
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

// Update the elements with the specified IDs
function updateElementsWithData(data) {
    for (const elementId in data) {
        if (Object.hasOwnProperty.call(data, elementId)) {
            const newValue = data[elementId];
            const element = document.getElementById(elementId);
            console.log(elementId, " = ", newValue);
            if (element) {
                // Check if the element is an input or textarea
                if (element.type === 'text' || element.type === 'number' || element.tagName.toLowerCase() === 'textarea') {
                    // For input and textarea elements, set the value property instead of innerText
                    element.value = newValue;
                }
                else if (element.type === 'checkbox') {
                    element.checked = newValue;
                }
                else {
                    // For other elements, use innerText
                    element.innerText = newValue;
                }
                console.log(elementId, " assigned ", newValue);
            }
        }
    }
}

