var file_content = '';

$(document).ready(function() {
    // Handle file input change event
    $('#file-input').on('change', function(event) {
        var file = event.target.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var contents = e.target.result;
                file_content = contents;
                console.log("File successfully read.");
            };

            reader.onerror = function(e) {
                console.error('Error reading file', e);
                alert('Error reading file');
            };

            reader.readAsText(file);
        } else {
            alert('No file selected');
        }
    });

    // Handle form submission event
    $('#upload-form').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission
        if (file_content) {
            saveToLocalStorage("character", file_content);
            window.location.href = window.location.origin + '/character-sheet';
        } else {
            alert('No file content to upload');
        }
    });
});
