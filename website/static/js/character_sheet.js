// Event listeners attached to parent class
$(document).ready(function() {
    // Load character data when the page is ready
    loadCharacterData();

    // Event listener for input elements (text, number, textarea)
    $(document).on("keydown blur", "input[type='text'], input[type='number'], textarea", debounce(function (e) {
        // Only update character data on blur or when Enter is pressed
        if (e.type === 'keydown' && e.key !== 'Enter') {
            return;
        }
        updateCharacterData(e.target.id, e.target.value);
    }, 300));

    // Event listener for checkbox elements
    $(document).on("change", "input[type='checkbox']", function () {
        // Update character data when the checkbox state changes
        const checkboxId = this.id;
        const isChecked = this.checked;
        updateCharacterData(checkboxId, isChecked);
    });
    $(document).on("change", "select", function() {
        // Update character data when the select option changes
        const selectId = this.id;
        const selectedValue = $(this).val();  // Get the selected value of the select element
        updateCharacterData(selectId, selectedValue);
    });
});

// Function to save input data to the backend
function updateCharacterData(id, value) {
    $.ajax({
        url: "/save-input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: value, type: id }),
        success: function(responseData) {
            // Update elements with the processed character data
            updateElementsWithData(responseData["elementsToUpdate"]);
            // Save character data to local storage
            saveToLocalStorage("character", JSON.stringify(responseData["packedCharacterData"]));
        },
        error: function(xhr, status, error) {
            console.error("Error saving input data:", error);
        }
    });
}

// Function to load character data from local storage
function loadCharacterData() {
    const characterData = getFromLocalStorage("character");
    console.log("Retrieved from storage data:", characterData);
    $.ajax({
        url: "/load-character-from-storage",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ characterData: characterData}),
        success: function(responseData) {
            // Update elements with the processed character data
            updateElementsWithData(responseData["elementsToUpdate"]);
            // Save character data to local storage
            saveToLocalStorage("character", JSON.stringify(responseData["packedCharacterData"]));
        },
        error: function(xhr, status, error) {
            console.error("Error loading character data:", error);
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

// Function to update elements with character data
function updateElementsWithData(data) {
    for (const elementId in data) {
        if (Object.hasOwnProperty.call(data, elementId)) {
            const newValue = data[elementId];
            const element = document.getElementById(elementId);
            console.log(elementId, " = ", newValue);
            if (element) {
                // Update element value based on its type or tagName
                if (element.type === 'text' || element.type === 'number' || element.tagName.toLowerCase() === 'textarea') {
                    element.value = newValue;
                } else if (element.type === 'checkbox') {
                    element.checked = newValue;
                } else if (element.tagName.toLowerCase() === 'select') {
                    // Find the option with the matching value and set it as selected
                    const option = element.querySelector(`option[value="${newValue}"]`);
                    if (option) {
                        option.selected = true;
                    }
                } else {
                    element.innerText = newValue;
                }
                console.log(elementId, " assigned ", newValue);
            }
        }
    }
}