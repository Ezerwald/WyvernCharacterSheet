$(".ability-score-input").on("keyup", function(e) {
     $.ajax({
        url: "/save_input",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({value: e.target.value, type: e.target.id}),
        success: (response) => {
            console.log(response);
        }
    });
})