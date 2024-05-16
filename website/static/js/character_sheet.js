// Event listeners attached to parent class
$(document).on("input", ".ability-score-input", debounce(function(e) {
    // Send AJAX request after a delay using debounce
    $.ajax({
        url: "/save_input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: e.target.value, type: e.target.id }),
        success: function(elements_to_update_dict) {
            updateDivsWithValues(elements_to_update_dict);
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error("AJAX Error:", error);
        }
    });
}, 300)); // Delay of 300 milliseconds


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