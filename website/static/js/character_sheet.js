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
    updateCharacterData(e.target.id, e.target.value);
}, 300)); // Delay of 300 milliseconds

$(document).on("change", "input[type='checkbox']", function() {
    // Get checkbox ID and checked state
    const checkboxId = this.id;
    const isChecked = this.checked;
    // Send AJAX request to save checkbox state
    updateCharacterData(checkboxId, isChecked);
});

function loadCharacterData() {
    // Load character data from backend
    $.ajax({
        url: "/get-character-data",
        method: "GET",
        success: function(characterData) {
            updateElementsWithData(characterData);
        },
        error: function(xhr, status, error) {
            console.error("Error loading character data:", error);
        }
    });
}

function updateCharacterData(id, value) {
    // Save input data to the backend
    $.ajax({
        url: "/save-input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: value, type: id }),
        success: function(responseData) {
            updateElementsWithData(responseData["elementsToUpdate"]);
            saveToLocalStorage("character", responseData["packedCharacterData"]);
        },
        error: function(xhr, status, error) {
            console.error("Error saving input data:", error);
        }
    });
}

function saveToLocalStorage(id, data) {
    // Save data to browser's local storage
    localStorage.setItem(id, JSON.stringify(data));
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

// Buttons event listeners
document.addEventListener('DOMContentLoaded', (event) => {
    // Save character button
    const saveButton = document.getElementById('save-character-button');
    if (saveButton) {
        saveButton.addEventListener('click', () => {
            window.location.href = '/download-character';
        });
    }

    //Upload character button
    const uploadButton = document.getElementById('upload-character-button');
    if (uploadButton) {
        uploadButton.addEventListener('click', () => {
            window.location.href = '/upload-character';
        });
    }
});

window.addEventListener('beforeunload', function (e) {
    e.preventDefault();
    fetch('/end-session', { method: 'POST' });
});
