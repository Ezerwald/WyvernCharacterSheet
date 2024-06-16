$(document).ready(function() {
    $('#create-character-button').on('click', function() {
        console.log('clicked');
        saveToLocalStorage("character",  null);
        window.location.href = window.location.origin + '/character-sheet';
    });
});