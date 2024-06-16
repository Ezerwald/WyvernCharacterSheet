// Function to retrieve data from local storage
function getFromLocalStorage(key) {
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
}

// Function to save data to local storage
function saveToLocalStorage(key, json) {
    localStorage.setItem(key, json);
    console.log("Saved to local storage data:", json);
}